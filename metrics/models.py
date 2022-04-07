from django.db import models
from django.contrib.auth import get_user_model

from notes.models import Article

User = get_user_model()


class ArticleVisitAction(models.Model):
    article = models.ForeignKey(to=Article, related_name="visits", on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name="visited_articles", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

