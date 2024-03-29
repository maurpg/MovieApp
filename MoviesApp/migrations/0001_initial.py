# Generated by Django 2.2 on 2019-06-06 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('detail', models.CharField(max_length=50)),
                ('trailer_url', models.CharField(max_length=100)),
                ('genere', models.CharField(max_length=50)),
                ('languaje', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('actors', models.ManyToManyField(to='MoviesApp.Actor')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MoviesApp.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Movie_Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('coment', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MoviesApp.Movie')),
            ],
        ),
    ]
