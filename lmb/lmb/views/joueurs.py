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


class JoueurView(View):

    def get(self, request):

        joueur_id = int(request.GET.get('id', None))

        if not joueur_id:
            raise  # FIXME raise something more interessing

        joueur = Joueur.objects.get(id=joueur_id)

        template = get_template('joueur.jinja')

        if joueur.photo:
            photo_path = f'images/{joueur.photo}'
        else:
            photo_path = f'images/joueur_default_{joueur.sexe}.jpg'

        equipe_a = Equipe.objects.get(id=3)
        equipe_b = Equipe.objects.get(id=6)

        datas = {
            'joueur': joueur,
            'fullname': f'{joueur.prenom} {joueur.nom}',
            'photo_path': photo_path,
            'equipe_infos': [
                (equipe_b, 5, 3, 0, 2, 0, 5),
                (equipe_a, 42, 25, 3, 12, 5, 47),

            ]
        }

        res = template.render(datas)
        return HttpResponse(res)
# Participant.objects.filter(joueur=joueur).select_related('formation').select_related('formation__match').values('formation__equipe__nom').annotate(Count('formation__match__id'))
