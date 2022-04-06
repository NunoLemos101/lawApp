from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(default='Categoria', max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.TextField()
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{} ({})'.format(self.title, self.category.name)


class SupportTicket(models.Model):

    TICKET_STATES = [
        ('Enviado', 'Enviado'),
        ('Respondido', 'Respondido'),
        ('Fechado', 'Fechado'),
    ]

    TYPES = [
        ('BUG_REPORT', 'Reportar um Bug na aplicação'),
        ('CONTENT_REPORT', 'Reportar um erro no conteúdo de Direito'),
        ('CONTENT_SUGGESTION', 'Sugerir algo que gostavas de ver na aplicação'),
    ]

    title = models.CharField(max_length=128)
    # Device that created the SupportTicket
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=False)
    state = models.CharField(max_length=10, choices=TICKET_STATES, null=False)
    type = models.CharField(max_length=100, choices=TYPES, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} ({}) @{}-{}-{}'.format(self.title, self.email, self.date.day, self.date.month, self.date.year)


class SupportTicketMessage(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ticket = models.ForeignKey(related_name="ticket_messages", to=SupportTicket, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    was_seen = models.BooleanField(default=False)


class PersonalNote(models.Model):

    title = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return '{} ({}) | id: {}'.format(self.title, self.user.__str__(), self.pk)
