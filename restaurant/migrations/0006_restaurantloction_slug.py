# Generated by Django 2.1.7 on 2019-03-12 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20190309_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantloction',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]