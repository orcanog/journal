"""
Cours "Advanced 2" - Exercice "Journal"
Réalisé par Xxxxx XXXXX
"""

import argparse
import random

# Import des variables "articles" et "interviews" depuis le module donnees

from donnees import articles, interviews

# Classe contenant les champs en commun entre les articles et interviews


class ElementJournal():

    # Variables communes aux articles et interviews
    date = ""
    edition = ""
    auteur = ""
    contenu = ""
    # Constructeur __init__ à écrire

    def __init__(self, date, edition, auteur, contenu):
        self.date = date
        self.edition = edition
        self.auteur = auteur
        self.contenu = contenu


class Article(ElementJournal):
    # Ecrire ici les variables spécifiques aux articles
    titre = ""
    # Ecrire ici le constructeur __init__ qui acceptera tous les champs d'un article

    def __init__(self, date, edition, auteur, contenu, titre):
        super().__init__(date, edition, auteur, contenu)
        self.titre = titre


class Interview(ElementJournal):
    # Ecrire ici les variables spécifiques aux interviews
    invite = ""
    # Ecrire ici le constructeur __init__ qui acceptera tous les champs d'une interview

    def __init__(self, date, edition, auteur, contenu, invite):
        super().__init__(date, edition, auteur, contenu)
        self.invite = invite
# Classe servant à importer et traiter les articles et interviews,
# avant de les afficher dans le terminal


class Generateur():
    date = None
    edition = None

    # Ecrire ici le constructeur __init__ qui acceptera "date" et "edition"
    def __init__(self, date, edition):
        self.date = date
        self.edition = edition

    def importer(self, articles, interviews):
        elements = []
        # Créer des instances de chaque article
        for dict in articles:
            elements.append(Article(dict, dict, dict, dict, dict))
        # Créer des instances de chaque interview
        for dict in interviews:
            elements.append(Interview(dict, dict, dict, dict, dict))
        # On rends aléatoire la liste des éléments
        elements = random.shuffle(elements)
        # On retourne la liste des éléments
        return elements

    def afficher(self, elements):
        # Affichage des détails du journal généré
        print(f"==================================")
        print(f"*-*-*-*-*-* LeLutécien *-*-*-*-*-*")
        print(f"==================================")

        """for dict in elements:
            print(dict)"""


        # Parcours de chaque élément de la liste "elements", en précisant si c'est un article ou
        # une interview, et en affichant ses détails (titre, édition, contenu...)
        for dict in elements:
            if (dict['date'] == dict[args.date]) and (dict['edition'] == dict[args.edition]):
                print("================================")
                print(dict.date, dict.edition, dict.auteur,
                    dict.contenu, dict.titre, sep=' ')
                print("================================")

        for dict in elements:
            print("================================")
            print(dict.date, dict.edition, dict.auteur,
                  dict.contenu, dict.titre, sep=' ')
            print("================================")

        # Ouverture du fichier "credits.txt" et affichage de ce dernier
        fichier = open('credits.txt', 'r', encoding="utf-8")
        try:
            contenu = fichier.read()
            print(contenu)
        finally:
            fichier.close()


if __name__ == "__main__":
    # On crée l'instance de ce qui nous permets d'accepter des arguments à l'aide de la bibliothèque argparse
    parser = argparse.ArgumentParser(
        description="Génère le journal du jour selon une date et une région.")
    # On demande deux arguments positionnels (obligatoires) lors de l'appel de ce script
    parser.add_argument(
        "date", help="Date du journal à générer, sous le format 'annee-mois-jour'")
    parser.add_argument("edition", help="Édition du journal à générer", choices=[
                        "national", "idf", "paca"])
    # Argparse nous renvoie ensuite un objet contenant les valeurs des arguments
    args = parser.parse_args()

    # On crée une instance de Générateur en lui passant la date et l'édition du journal que l'on veut voir
    # selon ce qui a été écrit dans le terminal lors de l'exécution de ce fichier python
    generateur = Generateur(args.date, args.edition)

    # On appelle la méthode du générateur en lui passant les articles et interviews (importés au tout début de ce fichier)
    elements = generateur.importer(articles, interviews)

    # On renvoie les éléments récupérés à la ligne précédente pour afficher le journal dans le terminal
    generateur.afficher(elements)
