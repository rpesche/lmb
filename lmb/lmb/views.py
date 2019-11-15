from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template

from lmb.models.monobasket import Joueur, Equipe
from lmb.models.tournois import Participant


class JoueursView(View):

    def get(self, request):

        joueurs = Joueur.objects.all()

        for joueur in joueurs:
            equipes_ids = (Participant.objects.filter(joueur=joueur)
                                              .select_related()
                                              .values('formation__equipe_id')
                                              .distinct()
                                              .values_list('formation__equipe__id', flat=True))

            joueur.equipes = Equipe.objects.filter(id__in)

        template = get_template('joueurs.recherche.jinja')
        res = template.render({'joueurs': joueurs})
        return HttpResponse(res)
