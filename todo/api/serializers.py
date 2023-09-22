from rest_framework import serializers as ser

from todo import models as t_m


class TaskSerializer(ser.ModelSerializer):
    created_at = ser.DateTimeField(read_only=True, format="%Y-%m-%d")

    class Meta:
        model = t_m.Task
        fields = 'id title description slug completed created_at'.split()
        read_only_fields = 'created_at slug'.split()
