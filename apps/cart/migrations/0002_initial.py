# Generated by Django 5.0.4 on 2024-07-13 13:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accessories', '0001_initial'),
        ('cart', '0001_initial'),
        ('fish', '0001_initial'),
        ('fish_food', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='item',
            name='accessory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items_accessory', to='accessories.accessory', verbose_name='Аксессуары'),
        ),
        migrations.AddField(
            model_name='item',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_cart', to='cart.cart', verbose_name='Корзина'),
        ),
        migrations.AddField(
            model_name='item',
            name='ffood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items_ffood', to='fish_food.fishfood', verbose_name='Корм для рыбы'),
        ),
        migrations.AddField(
            model_name='item',
            name='fish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cart_items_fish', to='fish.fish', verbose_name='Рыбы'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='cart.item'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
