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


   

   