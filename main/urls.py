from django.urls import path
from main.views import show_main, create_product, show_product, show_xml, show_json, show_json_by_id, show_xml_by_id, register
from main.views import login_user, logout_user, edit_product, delete_product, login_ajax, register_ajax, edit_product_ajax, get_product_by_id,create_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('news/<str:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:news_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:news_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>/', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>/', delete_product, name='delete_product'),
    path('login-ajax/', login_ajax, name='login_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),    
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('get-product-by-id/<uuid:id>/', get_product_by_id, name='get_product_by_id'),
    path('create-product-ajax/', create_product_ajax, name='create_product_ajax')
]