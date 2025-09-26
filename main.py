
"""
Module de lecture et traitement de listes à partir d'un fichier CSV.
"""
#### Imports et définition des variables globales

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
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # On enlève le retour à la ligne et on split
            list_line = line.strip().split(";")
            # Conversion en int si possible
            try:
                list_line = [int(x) for x in list_line]
            except ValueError:
                pass  # Si ce n'est pas convertible, on garde en str
            l.append(list_line)
    return l

def get_list_k(data, k):
    """Retourne la k-ième sous-liste de data."""
    return data[k]

def get_first(l):
    """Retourne le premier élément de la liste l."""
    return l[0]

def get_last(l):
    """Retourne le dernier élément de la liste l."""
    return l[len(l)-1]

def get_max(l):
    """Retourne la valeur maximale de la liste l."""
    return max(l)

def get_min(l):
    """Retourne la valeur minimale de la liste l."""
    return min(l)

def get_sum(l):
    """Retourne la somme des éléments de la liste l."""
    return sum(l)


#### Fonction principale


def main():
    """Fonction principale d'exécution du module."""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
