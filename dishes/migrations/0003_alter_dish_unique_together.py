# Generated by Django 5.0.6 on 2024-06-21 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_alter_dish_name_alter_dish_price_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dish',
            unique_together={('name', 'restaurant')},
        ),
    ]