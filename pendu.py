#############################################################################
"""
 Le jeu du pendu
"""
#############################################################################
from random import randrange

#
# Constantes
#
minuscules = "abcdefghijklmnopqrstuvwxyz"
mots = ["gateau", "chantilly", "frite","sandwichs","grenadine","citron","poisson","viande","fourchette","orange","pomme","poire","amer","tarte au citron", ]
dessins = [
"""
---------
 |     |
 |
 |
 |
 |
 |""",
 """
 ---------
 |     |
 |     0
 |
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |    -+-
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |
 |
 |""",
 """
 ---------
 |     |
 |     O
 |   /-+-/
 |    |
 |    
 |""",
 """
 --------
 |     |
 |     O
 |   /-+-/
 |    | |
 |
 |"""]

max_erreurs = len(dessins) - 1

def lire_lettre(propositions):
    #########################################################################
    """
     Demande une lettre à l'utilisateur en s'assurant qu'elle n'a pas déjà
     été proposée, puis ajoute cette lettre à la liste des lettres déjà
     proposées.

     >>> liste=['a', 'b', 'c']
     >>> lire_lettre(liste)
     Entrez une proposition de lettre : A
     Une seule lettre en minuscule, s'il vous plaît.
     Entrez une proposition de lettre : a
     Cette lettre a déjà été proposée.
     Entrez une proposition de lettre : qsdf
     Une seule lettre en minuscule, s'il vous plaît.
     Entrez une proposition de lettre : e
     'e'
     >>> print(liste)
     ['a', 'b', 'c', 'e']     
    """
    #########################################################################

    while True:
        lettre = input("Entrez une lettre : ")

        if lettre in propositions:
            print("Cette lettre a déjà été proposée.")
        elif lettre not in minuscules or len(lettre) != 1:
            print("Une seule lettre en minuscule, s'il vous plaît.")
        else:
            break;

    propositions.append(lettre)
    return lettre

def mot_avec_tirets(mot, propositions):
    #########################################################################
    """
     Renvoie un mot dont les lettres inconnues sont remplacées par des tirets
     
     >>> mot_avec_tirets('tirets', ['t', 'i'])
     'ti--t-'
    """
    #########################################################################
    m = ''
    for lettre in mot:
        if lettre in propositions:
            m = m + lettre
        else:
            m = m + '-'
    return m

def partie():
    #########################################################################
    """
     Joue une partie de pendu
     retourne True si gagné, False si perdu
    """
    #########################################################################

    #
    # Initialisations
    #
    erreurs = 0
    mot = mots[randrange(len(mots))]
    propositions = []

    #
    # Boucle d'interrogation de l'utilisateur
    #
    print(dessins[erreurs])

    while True:
        print("Lettres déjà proposées :", propositions)
        print("Réponse courante :", mot_avec_tirets(mot, propositions))

        lettre = lire_lettre(propositions)

        if lettre in mot:
            if mot_avec_tirets(mot, propositions) == mot:
                print("Bravo, vous avez gagné. Le mot était :", mot)
                print("Nombre d'erreurs:", erreurs)
                return True
        else:
            erreurs = erreurs + 1
            print(dessins[erreurs])
            if erreurs >= max_erreurs:
                print("vous êtes pendu, le mot était :", mot)
                return False

#############################################################################
# Programme principal
#############################################################################
print("Bienvenue sur notre pendu en python")
print("les régles de notre pendu sont:- le theme est la nourriture\n -en proposant strictement des lettres en minuscule essayer de trouver le mot qui se cache derriere\n -si une lettre est correcte nous vous afficherons sa place dans le mot\n -si au contraire elle n'est pas dans le mot une partie du pendu s'affichera\n -vous avez 6 chances maintenant à vous de jouer ")
parties = 0
victoires = 0


while True:
    parties = parties + 1
    if partie():
        victoires = victoires + 1

    while True:
        cont = input("v pour continuer, e pour arrêter : ")
        if cont == 'v' or cont == 'e':
            break;

    if cont == 'e':
        break;

print("Vous avez joué", parties, "partie(s)")
print("Vous en avez gagné", victoires)
print("Au revoir et merci")
print("Valentin DESCHAMPS et Emeline DERUE")
