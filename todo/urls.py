from django.urls import path
from .views import *

urlpatterns = [
   path('groups/', GroupGenerate.as_view(), name='groups'),
   path('todo/', TodoGenerate.as_view(), name='todos'),
   path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name='group-detail'),
   path('todo/<int:pk>/', ToDoDetail.as_view(), name='todo-detail'),

]