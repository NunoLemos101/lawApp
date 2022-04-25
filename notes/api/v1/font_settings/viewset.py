from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class FontSettingsViewSet(ViewSet):

    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        return Response(data=request.user.fontsettings.serialize(), status=200)


    def update(self, request, *args, **kwargs):
        font_settings = request.user.fontsettings
        font_settings.font_family = request.data["fontFamily"]
        font_settings.font_size = request.data["fontSize"]
        font_settings.font_color = request.data["color"]
        font_settings.font_weight = request.data["fontWeight"]
        font_settings.font_style = request.data["fontStyle"]
        font_settings.save()
        return Response(data=font_settings.serialize(), status=200)
