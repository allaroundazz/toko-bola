from django.forms import ModelForm
from main.models import Item

class TokoForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price','description','thumbnail', 'category', 'is_featured', 'stock', 'rating']