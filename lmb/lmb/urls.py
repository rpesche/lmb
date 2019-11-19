from django.urls import path

from lmb.views import JoueursView, JoueursRechercheView

urlpatterns = [
    path('joueurs.php', JoueursView.as_view()),
    path('joueurs/joueurs.recherche.joueur.php', JoueursRechercheView.as_view()),
]
