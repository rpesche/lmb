from django.db.models import Model, CharField, DateField, IntegerField, ForeignKey, CASCADE, UniqueConstraint
from django.db.models import Count

from .monobasket import Equipe, Joueur


class Match(Model):
    libelle = CharField(max_length=255)
    date = DateField()
    formation1 = ForeignKey('Formation', on_delete=CASCADE)
    formation2 = ForeignKey('Formation', on_delete=CASCADE)
    regle_formation1 = CharField(max_length=32)  # TODO What is that ?
    regle_formation2 = CharField(max_length=32)  # TODO What is that ?
    resultat = IntegerField(choices=[0, 1, 2, 3])
    score1 = IntegerField()
    score2 = IntegerField()
    arbitre1_id = IntegerField()  # TODO -> joueur
    arbitre2_id = IntegerField()  # TODO -> joueur

    class Meta:
        db_table = 'monobasket_match'


class Formation(Model):
    match = ForeignKey(Match, on_delete=CASCADE)
    equipe = ForeignKey(Equipe, on_delete=CASCADE)

    class Meta:
        db_table = 'monobasket_formation'


class Participant(Model):

    formation = ForeignKey(Formation, primary_key=True, on_delete=CASCADE)
    joueur = ForeignKey(Joueur, on_delete=CASCADE)
    gne = UniqueConstraint(name="plop", fields=['formation', 'joueur'])

    class Meta:
        db_table = 'monobasket_formation_joueur'
        unique_together = (('formation_id', 'joueur_id'),)


def get_match_played_by_team(joueur):

    infos = (Participant.objects.filter(joueur=joueur)
                                .select_related('formation')
                                .select_related('formation__match')
                                .values('formation__equipe__nom')
                                .annotate(nb_match=Count('formation__match__id'))
                                .values_list('formation__equipe', 'nb_match'))
    return {(equipe_id, {'played': played}) for equipe_id, played in infos}
