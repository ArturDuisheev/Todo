from django.urls import path

from todo.api import views as v

urlpatterns = [
    path('list_todo/', v.TodoListAPIView.as_view(), name='list_todo'),
    path('create_todo/', v.TodoCreateAPIView.as_view(), name='create_todo'),
    path('all_actions_api/<int:id>/', v.TodoAllActionsAPIView.as_view(), name='update_todo'),

]
