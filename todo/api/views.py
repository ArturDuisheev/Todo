from rest_framework import generics as rest_gen

from todo import models as t_m
from todo.api import serializers as t_s


class TodoListAPIView(rest_gen.ListAPIView):
    queryset = t_m.Task.objects.all()
    serializer_class = t_s.TaskSerializer


class TodoCreateAPIView(rest_gen.CreateAPIView):
    queryset = t_m.Task.objects.all()
    serializer_class = t_s.TaskSerializer


class TodoAllActionsAPIView(rest_gen.RetrieveUpdateDestroyAPIView):
    queryset = t_m.Task.objects.all()
    serializer_class = t_s.TaskSerializer
    lookup_field = 'id'
