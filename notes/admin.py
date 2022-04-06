from django.contrib import admin
from . import models

class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 2000


admin.site.register(models.PersonalNote)
admin.site.register(models.Category)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.SupportTicket)
admin.site.register(models.SupportTicketMessage)

# Register your models here.
