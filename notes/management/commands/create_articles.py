import json

from django.core.management.base import BaseCommand
from notes.models import Article, Category


class TempArticle:
    def __init__(self, number, body):
        self.title = "Artigo " + number
        self.body = body

    def get_object_as_dictionary(self):
        return {"title": self.title, "body": self.body}

    def set_title_from_body(self):
        splitted_array = self.body.split("\n")
        self.title = splitted_array[0] + " - " + splitted_array[1]
        return self


def remove_non_wanted_stuff(artigo):
    index = artigo.find("Contém as alterações introduzidas pelos seguintes diplomas:")
    return artigo[:index]


def get_article_number(artigo):
    index = artigo.find(".")
    return artigo[:index]


def write_to_file(array):
    x = json.dumps(array)
    json_file = open("json_data", "w")
    json_file.write(x)
    json_file.close()


def start_process():
    f = open("raw_data", "r")
    lista_de_artigos = f.read().split("  Artigo ")
    lista_de_objetos_class = []
    del lista_de_artigos[0]
    for artigo in lista_de_artigos:
        body = remove_non_wanted_stuff(artigo)
        body = "Artigo" + " " + body
        artigo = get_article_number(body)
        lista_de_objetos_class.append(TempArticle(artigo, body).set_title_from_body().get_object_as_dictionary())

    write_to_file(lista_de_objetos_class)
    f.close()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('category_name', nargs='+', type=str)

    def handle(self, *args, **options):
        start_process()
        json_file = open("json_data", "r")
        string_data = json_file.read()
        formatted_data = json.loads(string_data)
        category = Category.objects.get(name=options["category_name"][0])
        for article in formatted_data:
            print(Article.objects.create(title=article["title"], body=article["body"], category=category))
        self.stdout.write(self.style.SUCCESS(str(len(formatted_data)) + " Articles created"))
        