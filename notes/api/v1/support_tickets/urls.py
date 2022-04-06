from django.urls import path, include

from notes.api.v1.support_tickets.router import SupportTicketRouter
from notes.api.v1.support_tickets.views import SupportTicketViewSet

supportTicketRouter = SupportTicketRouter()
supportTicketRouter.register('support-tickets', SupportTicketViewSet, basename="support-tickets")

urlpatterns = [path('', include(supportTicketRouter.urls))]