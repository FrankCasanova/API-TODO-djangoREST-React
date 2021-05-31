from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path('<int:pk>', DetailTodo.as_view()), #endpoint /api/1 it is conect with a view
    path('', ListTodo.as_view()) #endpoint /api/
]
