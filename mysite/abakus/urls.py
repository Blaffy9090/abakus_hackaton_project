from django.urls import path, include
from .views import *

urlpatterns = [
    path('', event_list, name='event_list'),
    path('<int:id>', event_detail, name='event_detail'),
    path('<int:id>/register/', event_register, name='event_register'),
    path('<int:id>/content/', event_content, name='event_content'),
    path('<int:id>/login/', event_login, name='event_login'),
]
