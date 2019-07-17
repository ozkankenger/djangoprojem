from django.contrib import admin
from .models import Haberler
from .models import Kategori
# Register your models here.
class adminhaberler(admin.ModelAdmin):
    list_display=["kategori","title","image"]

admin.site.register(Haberler,adminhaberler) 

class adminkategori(admin.ModelAdmin):
    list_display=["id","kategori_ad"]

admin.site.register(Kategori,adminkategori) 
