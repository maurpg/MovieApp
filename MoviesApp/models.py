from django.db import models

class Director(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

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
    trailer_url = models.CharField(max_length = 100)
    director = models.ForeignKey(Director , on_delete=models.CASCADE)
    genere = models.CharField(max_length=50 , choices=genere_select)
    languaje = models.CharField(max_length=50 , choices=languaje_select)
    country = models.CharField(max_length=50)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        info = f'title:{self.title} , duration : {self.duration} , year: {self.year} , director : {self.director}'
        return info


class Movie_Rate(models.Model):
    movie = models.ForeignKey(Movie , on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    coment = models.TextField()
