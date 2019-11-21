from django.urls import path

from lmb.views.joueurs import JoueursView, JoueursRechercheView
from lmb.views.misc import Index, Menu

urlpatterns = [
    path('index.php', Index.as_view()),
    path('joueurs.php', JoueursView.as_view()),
    path('joueurs/joueurs.recherche.joueur.php', JoueursRechercheView.as_view()),

    path('menu/menu.login.php', Menu.as_view()),
]
