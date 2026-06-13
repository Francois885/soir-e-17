"""Module catalogue - Squelette à compléter (soirée 17).

Ce fichier fournit la STRUCTURE des fonctions à écrire : nom, paramètres
et contrat (ce qui entre, ce qui sort). Il ne contient AUCUN algorithme.

Les spécifications complètes (comportement attendu, cas limites, exemples)
figurent dans l'énoncé de l'atelier TP, qui fait seul autorité. Remplacez
chaque « raise NotImplementedError » par votre implémentation.

Aucune fonction ne doit modifier la liste reçue en argument.

Fichier distribué aux étudiants - à compléter.

Programmation Orientée Objet - EICPN 2025-2026.
"""

from collections import defaultdict  # noqa: F401 (utile selon votre choix)

from livre_s17 import Livre

CATALOGUE = [
Livre("1984", "Orwell", "9780451524935", 328, 1949),
Livre("La Ferme des animaux", "Orwell", "9780141036137", 112, 1945),
Livre("Le Meilleur des mondes", "Huxley", "9780060850524", 311, 1932),
Livre("Fahrenheit 451", "Bradbury", "9781451673319", 256, 1953),
]
DOUBLON = Livre("1984 (réédition)", "Orwell", "9780451524935", 328, 1949)
AVEC_DOUBLON = CATALOGUE + [DOUBLON]
# ──────────────────────────────────────────────────────────────────────
# 1. Tris
# ──────────────────────────────────────────────────────────────────────

def trier_par_titre(livres):
    """Trie une liste de Livre par titre croissant.

    Args:
        livres (list): Liste de Livre à trier.

    Returns:
        list: Une nouvelle liste triée (l'originale reste intacte).
    """
    return sorted(livres, key=lambda l: l.titre)

def trier_par_auteur_puis_titre(livres):
    """Trie par auteur, puis par titre à auteur égal.

    Args:
        livres (list): Liste de Livre à trier.

    Returns:
        list: Une nouvelle liste triée.
    """
    return sorted(livres, key=lambda l: (l.auteur, l.titre))

def trier_par_annee(livres, recents_dabord=False):
    """Trie par année de publication.

    Args:
        livres (list): Liste de Livre à trier.
        recents_dabord (bool): Si True, les plus récents en premier.

    Returns:
        list: Une nouvelle liste triée.
    """
    return sorted(livres, key=lambda l: l.titre, reverse=recents_dabord)


def trier_par_auteur_puis_annee_recente(livres):
    """Trie par auteur croissant, puis par année décroissante.

    Args:
        livres (list): Liste de Livre à trier.

    Returns:
        list: Une nouvelle liste triée.
    """
    return sorted(livres, key=lambda l: (l.auteur, not l.titre))

# ──────────────────────────────────────────────────────────────────────
# 2. Recherches
# ──────────────────────────────────────────────────────────────────────

def rechercher_par_auteur(livres, auteur):
    """Retourne tous les livres d'un auteur donné.

    Args:
        livres (list): Liste de Livre.
        auteur (str): Nom d'auteur recherché.

    Returns:
        list: Les Livre correspondants (liste éventuellement vide).
    """
    liste = []
    for i in livres:
        if i.auteur == auteur:
            liste.append(i)
    return liste

def rechercher_par_isbn(livres, isbn):
    """Retrouve un livre par son ISBN en parcourant la liste.

    Args:
        livres (list): Liste de Livre.
        isbn (str): ISBN recherché.

    Returns:
        Livre: Le livre correspondant, ou None s'il est absent.
    """
    for i in livres:
        if i.isbn == isbn:
            return i

# ──────────────────────────────────────────────────────────────────────
# 3. Ensembles
# ──────────────────────────────────────────────────────────────────────

def compter_distincts(livres):
    """Compte le nombre de livres distincts.

    Args:
        livres (list): Liste de Livre, doublons éventuels.

    Returns:
        int: Nombre de livres distincts.
    """
    return len(set(livres))

def dedoublonner(livres):
    """Supprime les doublons en conservant l'ordre de première apparition.

    Args:
        livres (list): Liste de Livre, doublons éventuels.

    Returns:
        list: Liste sans doublon, ordre de première apparition préservé.
    """
    liste = []
    
    for i in livres:
        if i not in liste:
            liste.append(i)
    return liste

# ──────────────────────────────────────────────────────────────────────
# 4. Dictionnaires
# ──────────────────────────────────────────────────────────────────────

def indexer_par_isbn(livres):
    """Construit un index {isbn: livre}.

    Args:
        livres (list): Liste de Livre.

    Returns:
        dict: Dictionnaire {isbn (str): livre (Livre)}.
    """
    dic = {}
    for i in livres:
        dic[i.isbn] = i
    return dic

def regrouper_par_auteur(livres):
    """Regroupe les livres par auteur.

    Args:
        livres (list): Liste de Livre.

    Returns:
        dict: Dictionnaire {auteur (str): [Livre, ...]}.
    """
    dic = {}
    for i in livres:
        dic.setdefault(i.auteur, []).append(i)
    return dic

if __name__ == "__main__":
    print("Squelette non implémenté : complétez les fonctions, "
          "puis lancez la suite de tests.")