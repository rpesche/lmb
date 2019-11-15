from django.db.models import Model, CharField, DateField, IntegerField


class Joueur(Model):

    SEXES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

    nom = CharField(max_length=64)
    prenom = CharField(max_length=64)
    pseudo = CharField(max_length=64)
    naissance = DateField()
    sexe = CharField(max_length=1, choices=SEXES)
    photo = CharField(max_length=255)
    nom_utilisateur = CharField(max_length=255)
    md5_mdp = CharField(max_length=255)
    droits = IntegerField()

    class Meta:
        db_table = 'monobasket_joueur'


class Equipe(Model):
    couleur_base = CharField(max_length=6)
    photo = CharField(max_length=255)
    nom = CharField(max_length=255)

    class Meta:
        db_table = 'monobasket_equipe'
