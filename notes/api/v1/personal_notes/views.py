import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import HttpResponse

from notes.api.serializers import PersonalNoteSerializer
from notes.models import PersonalNote


class PersonalNoteViewSet(ViewSet):

    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return Response(data=PersonalNoteSerializer(PersonalNote.objects.filter(user=request.user).order_by('title'), many=True).data, status=200)

    def create(self, request, *args, **kwargs):
        personal_note = PersonalNote.objects.create(title=request.data['title'], body=request.data['content'], user=request.user)
        return Response(data={"id": personal_note.id}, status=201)

    def destroy(self, request, *args, **kwargs):
        ids = request.GET.get('ids').split(',')

        for note_id in ids:
            personal_note = PersonalNote.objects.get(pk=note_id)
            if personal_note.user == request.user:
                personal_note.delete()
        return Response(data={"message": 'Notas eliminadas com sucesso'}, status=200)

    def retrieve(self, request, pk, *args, **kwargs):
        personal_note = PersonalNote.objects.get(pk=pk)
        response_data = PersonalNoteSerializer(personal_note).data

        if personal_note.user != request.user: return HttpResponse(status=403)

        response_data['has_access'] = True

        return Response(data=response_data, status=200)

    def update(self, request, pk, *args, **kwargs):
        personal_note = PersonalNote.objects.get(pk=pk)

        if personal_note.user == request.user:
            personal_note.body = request.data['new_text']
            personal_note.save()
            return Response(data={"message": "Note saved successfully"}, status=200)

