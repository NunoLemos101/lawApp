from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from .serializers import ReactNativeArticlesSerializer
from notes.models import Category, Article
from customAdmin.api.utils.pagination import articles_pagination


@api_view(['POST'])
@permission_classes([IsAdminUser])
def save_article(request):
    article = Article.objects.get(pk=request.data['article_id'])
    article.title = request.data['title']
    article.body = request.data['body']
    article.save()
    return Response(data={"active": True, "message": "Article successfully updated"}, status=200)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_article(request):
    article = Article.objects.create(title=request.data['title'], body=request.data['body'], category=Category.objects.get(pk=request.data['category_id']))
    return Response(data={"active": True, "message": "Article created, don't forget to update React Native Static Data ID#{}".format(article.id)}, status=200)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def delete_article(request):
    Article.objects.get(pk=request.data['id']).delete()
    return Response(data={"active": True, "message": "Article Deleted, Don't forget to update React Native Static Data, also you might need to update the page in order to don't see the item in the list anymore"}, status=200)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_articles(request, category_id):
    articles = Article.objects.filter(category=Category.objects.get(id=category_id)).order_by('id')
    return articles_pagination(articles, request)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_detail_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return Response({"title": article.title, "body": article.body, "id": article.pk}, status=200)



@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_categories(request):
    categories = Category.objects.all()
    data = []
    for category in categories:
        data.append({
            'name': category.name,
            'article_count': Article.objects.filter(category=category).count(),
            'id': category.id,
        })
    return Response(data=data, status=200)


class ReactNativeDataView(APIView):

    renderer_classes = (BrowsableAPIRenderer, JSONRenderer,)

    def get(self, request, category_id):
        articles = Article.objects.filter(category__id=category_id).order_by('id')
        serialized_data = ReactNativeArticlesSerializer(articles, many=True).data
        return Response(data=serialized_data, status=200)

