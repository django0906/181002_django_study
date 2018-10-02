from django.urls import path, include
from polls.views import index

urlpatterns = [
    path('', index, name='index')
]