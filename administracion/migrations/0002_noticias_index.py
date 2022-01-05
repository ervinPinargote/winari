# Generated by Django 3.1.7 on 2021-07-14 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='noticias_index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo noticia')),
                ('imagen', models.ImageField(upload_to='')),
                ('link', models.CharField(max_length=50, null=True, verbose_name='link')),
                ('descripcion', models.TextField()),
            ],
        ),
    ]