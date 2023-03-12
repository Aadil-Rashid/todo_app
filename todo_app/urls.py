from django.urls import path
from todo_app.views import GetTodoView
from todo_app.views import TodoView

urlpatterns = [
    path('todo/', GetTodoView.as_view()),
    path('', TodoView.as_view()),
    
]