from django.urls import path
from core.views import *
from core import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
]