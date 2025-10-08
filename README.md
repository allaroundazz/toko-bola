1. cara saya mengimplementasikan checklist secara bertahap adalah seperti berikut:
    1. Saya membuat project Django baru lalu menyesuaikan settings.py dan file-file lain
    2. Lalu saya membuat aplikasi main di dalam direktori project saya
    3. Merouting project kepada aplikasi main
    4. Membuat model yang sesuai
    5. Memigrasi database
    6. setelah itu saya membuat fungsi berikut di views.py : from django.http import HttpResponse

    def home(request):
        return HttpResponse("<h1>Aplikasi: Toko Bola</h1><p>Nama: Diaz Prayodhi - Kelas: IS-xx</p>")


    7. Lalu saya membuat routing baru dengan membuat urls.py baru di main
    8. Terakhir saya melakukan deployment ke PWS dengan push kode ke github dan menghubungkannya dengan PWS

2. Bagan
    Client (Browser)
      │
      ▼
 urls.py (project) → arahkan ke urls.py (main)
      │
      ▼
 urls.py (main) → panggil views.py
      │
      ▼
   views.py 
      │
      ▼
 render halaman (HTML)
      │
      ▼
 Response kembali ke client


3. peran settings.py dalam project django adalah sebagai pusat konfigurasi seperti database, aplikasi yang akan digunakan,
   middleware, dan lain-lain. Jadi settings.py menjadi tempat utama untuk mengatur komponen proyek django sesuai dengan kebutuhan.

4. Cara kerja migrasi di django adalah dengan menyamakan model yang telah kita definisikan di main dengan apa yang ada di database.
   Jadi, saat makeimigrations django akan membuat catatan perubahan yang telah kita lakukan, sedangkan saat "migrate", django akan 
   mengeksekusi hasil dari perubahan tersebut. Saat mengerjakan saya sempat mengalami error saat ingin melakukan migrate dan setelah saya telusuri, error tersbeut disebabkan oleh adanya module yang tidak ditemukan. Saya baru ingat bahwa saya sempat merubah folder saya namun belum saya rubah kembali di bagian settings.py dan itulah penyebabnya, hal ini membuat saya menjadi lebih mengerti terkait
   migrate.

5. Menurut saya, Django dijadikan framework untuk pembelajaran awal karena django lah yang paling mudah untuk dipahami 
   oleh pemula, selain itu django sudah memiliki fitur yang lengkap seperti panel admin sampai sistem autentifikasi yang
   pertama saya temui pada tutorial 0. Dikarenakan kita sudah mengenal python sejak semester 1 dan django juga menggunakan 
   python, jadi menurut saya itu juga menjadi alasan mengapa django menjadi pilihan yang tepat sebagai framework pengenalan.

6. Menurut saya tutorial 0 dan 1 sangat membantu saya untuk dapat mulai memahami alur dasar dari penggunaan django, saya juga 
   penjelasan bertahap yang disajikan dengan pemberian tips juga menjadi insight yang cukup penting untuk saya kedepannta.




1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
   karena dalam platform, antara pengguna dan client membutuhkan cara untuk mengirim dan nerima data.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   menurut saya JSON lebih baik karena lebih sederhana dan efisien

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
   untuk memastikan apakah data yang dikirim oleh user sudah sesuai agar data yang amsuk ke sistem sudah sesuai.

   






Tugas 4

1.  Menurut pemahaman saya, Django AuthenticationForm adalah form bawaan dari django untuk membuat interface login.
   kelebihannya adalah sudah terintegrasi dengan sistem authentication django dan sudah ada validasi
   secara otomatis jadi tidak perlu menulis validasi dari 0, namun menurut saya tampilannya kurang menarik

2. Autentikasi berarti memverifikasi identitas user (seperti login) sedangkan otorisasi menentukan apa saja yang 
   bisa dilakukan oleh user. Django melakukan autentikasi terlebih dahulu, setelah pass django melakukan otorisasi.

3. Cookies bisa tetap tersimpan dan datanya bisa teatp ada walaupun browsernya sudah ditutup atau dibuka lagi, namun 
   tidak direkomendasikan untuk menyimpan data dengan ukuran yang besar. Kelebihan dari session adalah keamanannya yang 
   tinggi dikarenakan tidak bisa dimodifikasi user sehingga cocok untuk menyimpan data sensitif, namun menurut sumber yang
   saya temukan di internet session memakan memory yang cukup tinggi.

4. Django secara default sudah cukup aman, namun tetap ada risiko potensial yang perlu diwaspadai. 

5. Implementasi dimulai dengan setup konfigurasi dasar di settings.py untuk mengaktifkan authentication apps dan middleware,     kemudian menjalankan migrasi database. Buat views untuk login/logout menggunakan AuthenticationForm dan decorator @login_required untuk proteksi views, serta template HTML yang include {% csrf_token %} dan conditional rendering berdasarkan status user.


   

   


   TUGAS 5

   1. Menurut pemahaman saya, prioritas selector CSS ditentukan oleh tingkat specificity-nya. Saya mengurutkan kekuatannya dari yang tertinggi yaitu inline style, diikuti oleh ID, class, hingga element selector sebagai aturan yang paling umum untuk diterapkan.

   2. esponsive design adalah sebuah pendekatan fundamental yang krusial. Tujuannya adalah untuk memastikan sebuah website mampu memberikan pengalaman pengguna yang optimal dan konsisten di berbagai ukuran layar, mulai dari perangkat mobile hingga desktop.

   3. Saya membedakan ketiga komponen box model ini berdasarkan lingkupnya terhadap elemen. Padding saya pahami sebagai ruang internal antara konten dan border, border sebagai bingkai elemen itu sendiri, dan margin sebagai ruang eksternal untuk menciptakan jarak dengan elemen lainnya.

   4.  Flexbox saya gunakan untuk mengatur komponen dalam satu dimensi (sebaris atau sekolom), sedangkan grid saya terapkan untuk membangun struktur layout halaman yang kompleks dan bersifat dua dimensi.

   5.  Pendekatan implementasi yang saya terapkan bersifat sistematis. Saya selalu mengawalinya dengan membangun struktur HTML yang semantik, dilanjutkan dengan styling dasar melalui pendekatan mobile-first, dan diakhiri dengan penyesuaian responsive untuk layar yang lebih besar menggunakan media queries.


   TUGAS 6

   1. Synchronous Request (Sinkron) bekerja seperti panggilan telepon. Saat browser mengirim permintaan ke server, ia harus menunggu sampai server memberikan jawaban penuh sebelum bisa melakukan hal lain. Selama menunggu, halaman akan "terkunci" atau tidak responsif. Inilah yang menyebabkan halaman me-reload seluruhnya saat Anda menekan sebuah tombol atau tautan.

   Asynchronous Request (Asinkron) bekerja seperti mengirim pesan chat. Browser mengirim permintaan di latar belakang, dan pengguna tetap bisa berinteraksi dengan halaman (menggulir, mengetik, dll.) tanpa harus menunggu. Saat server selesai memproses dan mengirim balasan, JavaScript akan menangani data tersebut dan memperbarui hanya bagian halaman yang relevan.

   2. Aksi Pengguna: Pengguna memicu sebuah event, misalnya mengklik tombol "Simpan".

   JavaScript Mengintersep: Event listener pada JavaScript mencegah aksi bawaan browser (seperti mengirimkan form dan me-reload halaman).

   Fetch Request: JavaScript mengumpulkan data yang dibutuhkan dan mengirimkannya ke sebuah URL spesifik di Django menggunakan fetch di latar belakang.

   View Django Memproses: View di Django yang terhubung dengan URL tersebut menerima data, memprosesnya (misalnya, menyimpan data ke database), dan menyiapkan respons.

   JsonResponse Dikirim: Alih-alih me-render template HTML, view tersebut mengembalikan JsonResponse yang hanya berisi data yang relevan (misalnya, status sukses atau pesan error).

   Pembaruan DOM: JavaScript di browser menerima JsonResponse, membacanya, dan secara dinamis memanipulasi atau memperbarui elemen HTML di halaman (seperti menambahkan kartu baru atau menampilkan pesan error) tanpa refresh.

   3. Pengalaman Pengguna (UX) Lebih Baik: Aplikasi terasa jauh lebih cepat dan responsif karena tidak ada full-page reload yang mengganggu. Interaksi terasa instan dan mulus, mirip aplikasi desktop.

   Efisiensi: Mengurangi beban kerja server dan penggunaan bandwidth karena server hanya mengirimkan data kecil dalam format JSON, bukan seluruh halaman HTML beserta asetnya.

   Interaktivitas Tinggi: Memungkinkan pembuatan fitur yang dinamis, seperti notifikasi real-time, auto-saving, dan pembaruan konten tanpa mengganggu aktivitas pengguna.


   4. roteksi CSRF (Cross-Site Request Forgery): Ini adalah yang terpenting. Setiap request POST dari AJAX harus menyertakan CSRF token. JavaScript mengambil token ini dari halaman dan mengirimkannya sebagai header (X-CSRFToken) pada fetch request.

   Gunakan HTTPS: Semua komunikasi yang mengirimkan data sensitif seperti password wajib dienkripsi menggunakan HTTPS.

   Validasi di Sisi Server: Jangan pernah mempercayai data yang dikirim dari frontend. View Django harus selalu melakukan validasi ulang semua data (misalnya, menggunakan AuthenticationForm atau UserCreationForm) sebelum menyimpannya ke database.

   5. Membuat Aplikasi Terasa Cepat: Meskipun ada jeda saat mengambil data, antarmuka pengguna tetap responsif. Menampilkan indikator loading membuat pengguna tahu sistem sedang bekerja, dan penantian terasa lebih singkat daripada melihat layar putih saat reload.

   Menjaga Konteks Pengguna: Karena halaman tidak pernah me-reload, pengguna tidak kehilangan posisi atau konteks mereka. Misalnya, setelah menambahkan produk dari modal, mereka tetap berada di halaman utama dan bisa langsung melanjutkan aktivitasnya.

   Memberikan Umpan Balik Instan: Aksi pengguna mendapatkan respons visual langsung. Saat item dihapus, item tersebut langsung hilang. Saat item disimpan, notifikasi toast muncul. Ini memberikan kepastian kepada pengguna bahwa aksi mereka berhasil.