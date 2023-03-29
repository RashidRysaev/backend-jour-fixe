from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import HeroSerializer, TeamSerializer
from .models import Hero, Team


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.order_by('created_at')
    serializer_class = HeroSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_200_OK, data={'message': 'Hero deactivated!'})


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def create(self, request, *args, **kwargs):
        teams_count = self.get_queryset().count()
        if teams_count >= 6:
            return Response(
                {"message": "Max heroic teams on Earth limit exceeded!"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)
