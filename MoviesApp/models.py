from django.db import models
from  django.contrib.auth import get_user_model

user = get_user_model()

class Director(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    genere_select = (
        ('Drama', 'Drama'),
        ('Action', 'Action'),
        ('Terror' , 'Terror'),
        ('Animate' , 'Aminate')
    )

    languaje_select = (
        ('Spanish', 'Spanish'),
        ('English', 'English'),
        ('France', 'France')
    )

    title = models.CharField(max_length = 50)
    duration = models.CharField(max_length=50)
    detail = models.CharField(max_length = 50)
    trailer_url = models.URLField(null=True )
    director = models.ForeignKey(Director , on_delete=models.CASCADE)
    genere = models.CharField(max_length=50 , choices=genere_select)
    languaje = models.CharField(max_length=50 , choices=languaje_select)
    country = models.CharField(max_length=50)
    #actors = models.ManyToManyField(Actor)
    image = models.ImageField(upload_to = 'images/', default = None)

    def __str__(self):
        return self.title


class Movie_Rate(models.Model):

    cualifity = (
        ('1', 'Mala'),
        ('2', 'Regular'),
        ('3', 'Buena'),
        ('4', 'Muy buena'),
        ('5', 'Excelente'),
    )
    movie = models.ForeignKey(Movie , on_delete=models.CASCADE)
    user = models.ForeignKey(user , on_delete=models.CASCADE)
    coment = models.CharField(max_length=30 , choices=cualifity)
