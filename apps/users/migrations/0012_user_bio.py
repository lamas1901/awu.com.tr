# Generated by Django 4.0.4 on 2022-07-07 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_price_consultacy'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default='', verbose_name='Bio?'),
            preserve_default=False,
        ),
    ]