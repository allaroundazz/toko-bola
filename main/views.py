from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'aplikasi' : 'tokobola',
        'nama': 'Diaz Prayodhi Iskandar',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
