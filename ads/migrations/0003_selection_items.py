# Generated by Django 4.1.3 on 2022-11-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='selection',
            name='items',
            field=models.ManyToManyField(to='ads.ad'),
        ),
    ]
