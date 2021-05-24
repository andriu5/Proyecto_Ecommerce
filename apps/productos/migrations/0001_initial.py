# Generated by Django 2.2.4 on 2021-05-24 13:02

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
                ('nombre', models.CharField(max_length=100)),
                ('cantidad_vendida', models.PositiveIntegerField(default=0)),
                ('precio', models.PositiveIntegerField(default=0)),
                ('categoria', models.CharField(max_length=50)),
                ('inventario', models.PositiveIntegerField(default=0)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(default='none.jpg', upload_to='media')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]