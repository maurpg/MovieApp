# Generated by Django 2.2 on 2019-06-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviesApp', '0007_auto_20190607_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default=None, upload_to='media'),
        ),
    ]
