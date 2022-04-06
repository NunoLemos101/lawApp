from rest_framework.pagination import PageNumberPagination
from customAdmin.api.serializers import ArticleSerializer


def articles_pagination(qs, request):
    paginator = PageNumberPagination()
    paginator.page_size = 100
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = ArticleSerializer(paginated_qs, many=True)
    return paginator.get_paginated_response(serializer.data)
