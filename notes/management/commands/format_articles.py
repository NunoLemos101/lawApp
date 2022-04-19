
from django.core.management.base import BaseCommand
from notes.models import Article, Category


def format_article(body):
    array = body.split("\n")
    empty = ""
    for index in range(len(array)):
        try:
            if len(array[index]) == 0 and len(array[index + 1]) == 0:
                break
        except:
            break
        if len(array[index]) != 0:
            empty = empty + array[index] + "\n\n"
    print(body)
    print("----- // -----")
    print(empty)
    return empty

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('category_name', nargs='+', type=str)

    def handle(self, *args, **options):
        category = Category.objects.get(name=options["category_name"][0])
        articles = Article.objects.filter(category=category)
        for article in articles:
            article.body = format_article(article.body)
            article.save()
            self.stdout.write(self.style.SUCCESS(article.title + " --> formatted"))
