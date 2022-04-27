from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class CategorySettingsViewSet(ViewSet):

    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        return Response(data=request.user.profile.category_settings, status=200)


    def update(self, request, *args, **kwargs):
        request.user.profile.category_settings = request.data["categorySettings"]
        request.user.profile.save()
        return Response(data=request.user.profile.category_settings, status=200)
