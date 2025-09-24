import uuid
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('sportswear', 'Sportswear'),
        ('bola', 'Bola'),
        ('booster', 'Booster'),
        ('headband', 'Headband'),
        ('others', 'Others'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)  # nama item
    price = models.IntegerField()            # harga item
    description = models.TextField()         # deskripsi item
    thumbnail = models.URLField(blank=True, null=True)  # gambar item
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='others')
    is_featured = models.BooleanField(default=False)    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    # contoh atribut tambahan
    stock = models.PositiveIntegerField(default=0)      # stok item
    rating = models.FloatField(default=0.0)             # rating item
    
    def __str__(self):
        return self.name

    
    @property
    def is_item_hot(self):
        return self.item_views > 20
        
    def increment_views(self):
        self.news_item += 1
        self.save()