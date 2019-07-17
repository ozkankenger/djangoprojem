from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Haberler(models.Model):
    kategori=models.ForeignKey('Kategori', on_delete=models.CASCADE, verbose_name="Kategori", related_name="posts")
    title=models.CharField(max_length=150, verbose_name="Başlık")
    metin=RichTextField(verbose_name="Açıklama")
    image=models.ImageField(null=True, blank=True)

    def get_absolute_url(self):
       return reverse('detail', kwargs={'id':self.id})


    def get_gundem_url(self):
        return reverse('gundem')

    def get_ekonomi_url(self):
        return reverse('ekonomi')

    def get_siyaset_url(self):
        return reverse('siyaset')

    def get_spor_url(self):
        return reverse('spor')

    class Meta:
        ordering = ['-id']    

class Kategori(models.Model):
    kategori_ad=models.CharField(max_length=30, verbose_name="Haber Türü")

    def __str__(self):
        return self.kategori_ad