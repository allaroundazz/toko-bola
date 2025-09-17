from django.forms import ModelForm
from main.models import Toko

class TokoForm(ModelForm):
    class Meta:
        model = Toko
        fields = ['price', 'size', 'type', 'stock', 'thumbnail', 'description']