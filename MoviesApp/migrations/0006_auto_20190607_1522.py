# Generated by Django 2.2 on 2019-06-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0005_auto_20190607_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]