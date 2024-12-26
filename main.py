"""
LE Programme
"""
#### Imports et définition des variables globales
#import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f:
        return [[ int(i) for i in l.strip().split(';') ] for l in f.readlines()]
        #l = f.readlines()
        #   while i < len(l):
        #    l.split(';')
        #for i in l:
        #    i.strip().split(';')

def get_list_k(data, k):
    """returne la k eme liste
    Args:
        data (liste): toutes les listes
    
    Returns:
        k eme liste
    """
    return data[k]

def get_first(l):
    """retourne la premiere element
    Args:
        l (liste)
    
    Returns:
        1er elelement
    """
    return l[0]

def get_last(l):
    """retourne le dernier element
    Args:
        l (liste)
    
    Returns:
        dernier elelement
    """
    return l[-1]

def get_max(l):
    """Le plus grand element de la liste
    Args:
        l (liste)
    
    Returns:
        le plus grand elelement
    """
    x = 0
    for j in l:
        x = max(x, j)
    return x


def get_min(l):
    """
    le plus petit element
    """
    x = 1000000
    for j in l:
        x = min(x, j)
    return x

def get_sum(l):
    """
    la somme de tout les element dans une liste
    """
    x = 0
    for i in l:
        x +=i
    return x


#### Fonction principale


def main():
    """
    appele des fonctions secondaires
    """
    #pass

    data = read_data(FILENAME)
    #print (data)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
