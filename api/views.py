from rest_framework.viewsets import ModelViewSet

from robots.models import Robot
from .serializers import NewRobotSerializer


class NewRobot(ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = NewRobotSerializer

    class Meta:
        model = Robot
