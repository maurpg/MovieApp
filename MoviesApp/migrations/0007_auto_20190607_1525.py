# Generated by Django 2.2 on 2019-06-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0006_auto_20190607_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
