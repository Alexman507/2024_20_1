# Generated by Django 5.0.6 on 2024-05-15 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_manufactured_at_alter_product_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='manufactured_at',
        ),
    ]
