from MoviesApp.models import Movie

def search(request):
    """Method to search movie for label sended"""
    label  =  request['search_for']
    value = request['search']
    values = {label:value}
    movies  = Movie.objects.filter(**values)
    return movies

