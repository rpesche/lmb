from django.http import HttpResponse
from django.views import View
from django.template.loader import get_template
from django.db.models import Count

from lmb.models.monobasket import Joueur, Equipe
from lmb.models.tournois import Participant


class JoueursView(View):

    def get(self, request):
        template = get_template('joueurs.jinja')
        return HttpResponse(template.render())


class JoueursRechercheView(View):

    def post(self, request):

        joueurs = Joueur.objects.order_by('prenom').all()[:25]

        for joueur in joueurs:
            equipes_ids = (Participant.objects.filter(joueur=joueur)
                                              .select_related('formation')
                                              .values('formation__equipe_id')
                                              .annotate(Count('formation__equipe_id'))
                                              .values_list('formation__equipe_id', flat=True))

            joueur.equipes = Equipe.objects.filter(id__in=equipes_ids)

        template = get_template('joueurs.recherche.jinja')
        res = template.render({'joueurs': joueurs})
        return HttpResponse(res)
