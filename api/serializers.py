from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField,
    CharField)

from robots.models import Robot


class NewRobotSerializer(ModelSerializer):
    model = CharField(min_length=2, max_length=2)
    version = CharField(min_length=2, max_length=2)
    serial = SerializerMethodField()

    class Meta:
        model = Robot
        fields = ('serial', 'model', 'version', 'created')

    def get_serial(self, obj):
        return f'{obj.model}{obj.version}'

    def create(self, validated_data):
        model = validated_data.get('model')
        version = validated_data.get('version')
        created = validated_data.get('created')
        serial = f'{model}{version}'

        return Robot.objects.create(
            model=model,
            version=version,
            created=created,
            serial=serial
        )
