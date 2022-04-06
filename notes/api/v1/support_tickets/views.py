from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from notes.api.serializers import SupportTicketListSerializer, SupportTicketDetailSerializer
from notes.api.utils.override import ResponseThen
from notes.models import SupportTicket, SupportTicketMessage

User = get_user_model()


class SupportTicketViewSet(ViewSet):
    """
    A viewset that provides the standard actions
    related to Support Tickets
    """

    permission_classes = [IsAuthenticated]

    def answer(self, request):
        """
        Custom Method
        """

        ticket = SupportTicket.objects.get(pk=request.data['ticket_id'])
        if request.user.is_superuser and ticket.state != "Fechado":
            SupportTicketMessage.objects.create(user=request.user, ticket=ticket, body=request.data['body'])
            ticket.state = "Respondido"
            ticket.save()
            return HttpResponse(status=201)

        if ticket.state == "Respondido":
            SupportTicketMessage.objects.create(user=request.user, ticket=ticket, body=request.data['body'])
            ticket.state = "Enviado"
            ticket.save()
            return HttpResponse(status=201)

        if ticket.state == "Enviado":
            return Response(data={"message": "Voce tem de esperar até receber uma resposta da nossa Staff"}, status=200)

        else:
            return Response(data={"message": "This ticket is closed"}, status=200)

    def create(self, request):
        """
        Overridden
        """

        ticket = SupportTicket.objects.create(user=request.user, title=request.data['title'], email=request.data['email'], type=request.data['type'], state="Enviado")
        SupportTicketMessage.objects.create(user=request.user, ticket=ticket, body=request.data['body'])
        return HttpResponse(status=201)

    def list(self, request, *args, **kwargs):
        """
        Overridden
        """
        def then(*args):
            query = SupportTicketMessage.objects.filter(user=User.objects.get(pk=1), was_seen=False, ticket__user=request.user)
            for ticket_message in query:
                ticket_message.was_seen = True
                ticket_message.save()

        return ResponseThen(SupportTicketListSerializer(SupportTicket.objects.filter(user=request.user), many=True).data, then_callback=then, status=200)

    def retrieve(self, request, pk, *args, **kwargs):
        """
        Overridden
        """
        ticket = SupportTicket.objects.get(pk=pk)
        if request.user == ticket.user:
            return Response(SupportTicketDetailSerializer(ticket).data, status=200)
        else:
            return HttpResponse(403)
        