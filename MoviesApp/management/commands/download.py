import requests
from django.core.management.base import BaseCommand

class Comand(BaseCommand):
    help = 'fetch movie from OMDB API'

    def add_arguments(self, parser):
        #positional arguments
        parser.add_argument('title', type=str)

        #kwargs like arguments
        parser.add_argument('-s', '--search', action='store_true', default=False)

    def handle(self, *args, **options):
        search = options['search']
        title = options['title']
        print(search)
        print(title)
