import json

from django.core.management.base import BaseCommand
from notes.models import Article, Category


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('create-articles', nargs='+', type=int)

    def handle(self, *args, **options):
        json_file = open("json_data", "r")
        string_data = json_file.read()
        x = json.loads(string_data)
        category = Category.objects.get(name="Código do trabalho")
        for article in x:
            print(Article.objects.create(title=article["title"], body=article["body"], category=category))
        self.stdout.write(self.style.SUCCESS(str(len(x)) + " Articles created"))