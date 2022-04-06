from rest_framework.routers import SimpleRouter, Route


class PersonalNoteRouter(SimpleRouter):

    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list', 'post': 'create', 'delete': 'destroy'},
            name='{basename}-list',
            detail=False,
            initkwargs={}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve', 'put': 'update'},
            name='{basename}-detail',
            detail=True,
            initkwargs={}
        ),
    ]