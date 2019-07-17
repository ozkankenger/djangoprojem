# Generated by Django 2.0.9 on 2019-05-13 06:15

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Haberler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Başlık')),
                ('metin', ckeditor.fields.RichTextField(verbose_name='Açıklama')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_ad', models.CharField(max_length=30, verbose_name='Haber Türü')),
            ],
        ),
        migrations.AddField(
            model_name='haberler',
            name='kategori',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uygulama.Kategori', verbose_name='Kategori'),
        ),
    ]
