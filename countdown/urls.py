from django.urls import path
from . views import event_detail

urlpatterns = [
    path('', event_detail, name='event_detail'),
]
