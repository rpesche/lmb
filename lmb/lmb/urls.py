from django.contrib import admin
from django.urls import path

from lmb.views import JoueursView

urlpatterns = [
    path('joueurs/', JoueursView.as_view()),
]
