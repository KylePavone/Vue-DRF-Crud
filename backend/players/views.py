from rest_framework.viewsets import ModelViewSet
from .models import Players
from .serializers import PlayersSerializer


class PlayersViewSet(ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
