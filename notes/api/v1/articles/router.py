from rest_framework.routers import SimpleRouter, Route


class ArticleRouter(SimpleRouter):

    routes = [
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/add-to-favorites/$',
            mapping={'post': 'add_to_favorites'},
            name='{basename}-detail',
            detail=False,
            initkwargs={}
        ),
    ]