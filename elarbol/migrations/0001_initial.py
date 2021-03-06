# Generated by Django 3.1.3 on 2020-11-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(blank=True, max_length=50, null=True)),
                ('precio', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=200, unique=True)),
                ('activo', models.IntegerField(blank=True, null=True)),
                ('foto_producto', models.ImageField(blank=True, null=True, upload_to='foto_producto')),
            ],
            options={
                'ordering': ['-nombre_producto'],
            },
        ),
    ]
