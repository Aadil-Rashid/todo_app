from django.urls import path
from todo_app.views import GetTodoView

urlpatterns = [
    path('todo/', GetTodoView.as_view()),
]