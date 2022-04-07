from rest_framework.response import Response
from metrics.models import ArticleVisitAction


class ArticleRetrieveResponse(Response):
    """
    Overrides the Response class
    takes in two extra arguments (article & user)
    creates the metrics object after the connection is closed
    therefore giving the User a faster response
    """

    def __init__(self, data, article, user, **kwargs):
        super().__init__(data, **kwargs)
        self.article = article
        self.user = user

    def close(self):
        super().close()
        ArticleVisitAction.objects.create(article=self.article, user=self.user)
