from django.contrib import admin
from .models import Brewery, Beer, ShoppingCartlist
# Register your models here.

admin.site.register(Brewery)
admin.site.register(Beer)
admin.site.register(ShoppingCartlist)