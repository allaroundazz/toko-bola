from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import TokoForm
from main.models import Toko
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    context = {
        'aplikasi' : 'tokobola',
        'nama': 'Diaz Prayodhi Iskandar',
        'class': 'PBP D',
        'product_list': product
    }

    return render(request, "main.html", context)

def create_product(request):
    form = TokoForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Toko, pk=id)
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

