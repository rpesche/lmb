{% if user %}

    Connecté en temps que {{ user.nom }}
    <DIV class="champ_a_cliquer" onmouseover="this.style.cursor='pointer'" onclick="seDelogge();">Se déconnecter</DIV>

{% else %}

    Utilisateur :
    <INPUT class="champTexte" id="menu.login.nom_utilisateur" type="text" maxlength="255" size="10">
     Mot de passe : 
    <INPUT class="champTexte" id="menu.login.mdp" type="password" maxlength="255" size="10">"
    <DIV class="champ_a_cliquer" onmouseover="this.style.cursor='pointer'" onclick="seLogge();">Se connecter</DIV>

{% endif %}
