from rest_framework.routers import SimpleRouter, Route


class CategorySettingsRouter(SimpleRouter):

    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'retrieve', 'put': 'update'},
            name='{basename}-detail',
            detail=False,
            initkwargs={}
        ),
    ]