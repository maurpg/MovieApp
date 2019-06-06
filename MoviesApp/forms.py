from django import forms
from .models import Movie , Movie_Rate , Actor , Director

class MovieForm(forms.ModelForm):

    class Meta:
        model =  Movie

        fields = [
            'title',
            'duration',
            'detail',
            'trailer_url'
            'director',
            'genere',
            'languaje',
            'country',
            'actors'
         ]

        labels = {
            'title':'Title',
            'duration':'Duration',
            'detail':'Detail',
            'trailer_url':'Url triler',
            'director':'Director',
            'genere':'Genere',
            'languaje':'Languaje',
            'country':'Country',
            'actors':'Actor',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.TextInput(attrs={'class': 'form-control'}),
            'trailer_url': forms.TextInput(attrs={'class': 'form-control'}),
            'director': forms.Select(attrs={'class': 'form-control'}),
            'genere':forms.Select(attrs={'class': 'form-control'}),
            'languaje': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'actors':forms.MultipleChoiceField(attrs={'class': 'form-control'})


        }


class MovieActorForm(forms.ModelForm):

    class Meta:
        model =  Actor

        fields = [
            'name',
            'age'
        ]

        labels = {
            'name':'Name',
            'age':'Age'
        }

        
