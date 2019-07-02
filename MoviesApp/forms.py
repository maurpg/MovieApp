from django import forms
from .models import Movie , Movie_Rate , Actor , Director

class MovieForm(forms.ModelForm):

    class Meta:
        model =  Movie
        fields = '__all__'


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

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'})
        }


class MovieDirectorForm(forms.ModelForm):

    class Meta:
        model = Director

        fields = [
            'name',
            'age'
        ]

        labels = {
            'name':'Name',
            'age':'Age'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'})
        }


class MovieRateForm(forms.ModelForm):

    class Meta:
        model = Movie_Rate

        fields = [
            'movie',
            'coment'
        ]

        labels = {
            'name':'Name',
            'coment':'coment'
        }

        widgets = {
            'movie': forms.Select(attrs={'class': 'form-control'}),
            'coment': forms.Select(attrs={'class': 'form-control'}),
        }


class RateForm(forms.Form):

    class Meta:
        model = Movie_Rate
        fields = ['cualifity','movie','coment']

        labels = {'cualifity':'Rate','movie':'movie','coment':'Coment'}

        widgets = {
            'cualifity':forms.Select(attrs={'class':'form-class'}),
            'movie':forms.TextInput(attrs={'class':'form-class'}),
            'coment':forms.TextInput(attrs={'class':'form-class'})
        }

class LoginForm(forms.Form):
    user_name = forms.CharField(label='user_name' , max_length=100)
    password = forms.CharField(label='password' , widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    user_name = forms.CharField(label = 'user_name' , max_length=100)
    password =  forms.CharField(label='password' , widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)

class SearchMovieForm(forms.Form):

    types = (
        ('title','Name'),
        ('director','Director'),
        ('genere' , 'Genere')
    )

    search_for = forms.ChoiceField(choices=types)

    search =  forms.CharField(label = 'Search' , max_length=100)
