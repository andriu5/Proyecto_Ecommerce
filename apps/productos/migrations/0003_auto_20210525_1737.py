# Generated by Django 2.2.4 on 2021-05-25 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_uploaded_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_uploaded', to=settings.AUTH_USER_MODEL),
        ),
    ]
