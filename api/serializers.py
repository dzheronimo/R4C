from rest_framework.serializers import ModelSerializer

from robots.models import Robot


class NewRobotSerializer(ModelSerializer):

    class Meta:
        model = Robot
        fields = ('model', 'version', 'created')