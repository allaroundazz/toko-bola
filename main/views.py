from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import TokoForm
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_POST


# 
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get('filter', "all") 

    if filter_type == "all":
        product_list = Item.objects.all() 
    else:
        product_list = Item.objects.filter(user=request.user) 
    context = {
        'appname':'Takobala',
        'class': 'PBP D',
        'product_list': product_list, 
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = TokoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Item, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        product_item = product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        product_item = product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_item])
        return HttpResponse(json_data, content_type="application/json")
    except:
        return HttpResponse(status=404)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Item, pk=id) 
    
    if request.method == 'POST':
        form = TokoForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:show_product', id=id)
    else:
        form = TokoForm(instance=product) 

    context = {
        'form': form,
        'product': product
    }
    return render(request, 'main/edit_product.html', context)

def delete_product(request, id):
    product = get_object_or_404(Item, pk=id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('main:show_main')

    context = {'product': product}
    return render(request, 'main/delete_product.html', context)

@csrf_exempt 
def login_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Format data tidak valid'}, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": "success",
                "message": "Login berhasil!",
                "username": user.username
            })
        else:
            return JsonResponse({
                "status": "error",
                "message": "Username atau password salah."
            }, status=401)
            
    return JsonResponse({'status': 'error', 'message': 'Metode request tidak valid'}, status=405)


@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Format data tidak valid'}, status=400)

        form = UserCreationForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Pendaftaran berhasil! Silakan login.'}, status=201)
        else:
            # Mengirimkan error form dalam format JSON
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Metode request tidak valid'}, status=405)

@csrf_exempt
@require_POST
def create_product_ajax(request):
    name = request.POST.get("name")
    price = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    stock = request.POST.get("stock")
    user = request.user

    
    new_item = Item(
        name=name,
        price=price,
        description=description,
        category=category,
        stock=stock,
        user=user
    )
    new_item.save()

    # Mengembalikan respons sederhana
    return HttpResponse("CREATED", status=201)

@require_POST
def delete_product(request, id):
    try:
        product = Item.objects.get(pk=id)
        product.delete()
        return JsonResponse({'status': 'success', 'message': 'Produk berhasil dihapus.'}, status=200)
    except Item.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Produk tidak ditemukan.'}, status=404)
    

def get_product_by_id(request, id):
    product = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', product), content_type="application/json")


@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    try:
        product = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Produk tidak ditemukan.'}, status=404)

    form = TokoForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
        updated_product = form.save()
        # Mengembalikan data produk yang sudah diupdate
        product_json = serializers.serialize('json', [updated_product])
        return JsonResponse({'status': 'success', 'product': product_json})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)