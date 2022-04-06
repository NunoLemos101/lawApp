from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import HttpResponse
from notes.models import Article, PersonalNote


class ArticleViewSet(ViewSet):

    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk, *args, **kwargs):
        article = Article.objects.get(id=pk)
        response = {"body": article.body, "has_access": request.user.profile.has_access()}
        return Response(data=response, status=200)

    def add_to_favorites(self, request, *args, **kwargs):
        article = Article.objects.get(pk=request.data['id'])
        PersonalNote.objects.create(title=article.title, body=article.body, user=request.user)
        return HttpResponse(status=200)
