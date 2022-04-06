"""
Deprecated

Will be removed soon
"""


from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import PersonalNote, SupportTicket, SupportTicketMessage

User = get_user_model()


class SupportTicketMessageSerializer(serializers.ModelSerializer):
    from_who = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SupportTicketMessage
        fields = ['body', 'from_who', 'date']

    def get_from_who(self, obj):
        return "ADMIN" if obj.user == User.objects.get(pk=1) else "USER"


class SupportTicketDetailSerializer(serializers.ModelSerializer):
    ticket_messages = SupportTicketMessageSerializer(read_only=True, many=True)

    class Meta:
        model = SupportTicket
        fields = ['title', 'state', 'type', 'date', 'ticket_messages', 'pk']


class SupportTicketListSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupportTicket
        fields = ['id', 'title', 'state', 'date']


class PersonalNoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalNote
        fields = ['title', 'body', 'created_at', 'id']
