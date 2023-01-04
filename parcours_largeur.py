import numpy as np

def traite_sommet(s, g, file, couleurs, resultat):
    """
    Traite un sommet
    :param s: sommet à traiter
    :param g: graphe
    :param file: file à traiter
    :param couleurs: couleurs
    :param resultat: dictionnaire des résultats
    :return: file, résultat
    """
    couleurs[s]="traitement"# on passe le sommet en traitement
    fils=g.get(s)
    for f in fils:
        if couleurs[f]=="non découvert":
            #print("ajout du sommet "+f+" dans la file")
            couleurs[f]="découvert"
            resultat[f]=s
            file.append(f)
    couleurs[s]="traité"
    return file, couleurs, resultat



def parcours_largeur(g, depart):
    """
    Parcours en largeur, on suppose que les noms de sommets sont des entiers
    :param g: graphe sous la forme d'un dictionnaire de lsite d'adj
    :param depart: sommet de départ
    :return:
    """
    n=len(g) #nombre de sommets dans le graphe
    #liste des sommets
    s=[]
    for a in g:
        fils=g.get(a)
        if not(a in s):
            s.append(a)
        for f in fils:
            if not(f in s):
                s.append(f)
    #print("liste des sommets dans le graphe :")
    #print(s)
    if not(depart in s):
        print("Le sommet n'est pas dans le graphe")
        return 0

    # dictionnaire de couleurs et des resultats
    couleurs={}
    resultat={}
    for sommet in s:
        couleurs[sommet]="non découvert"
        resultat[sommet]=None
    couleurs[depart]="traitement"
    resultat[depart]=depart

    file=[depart]
    #print("départ")
    while len(file)>0:
        sommet=file.pop()
        file, couleurs, resultat=traite_sommet(sommet, g, file, couleurs, resultat)

    return resultat

def graph_include(g, target):
    s=[]
    for a in g:
        fils=g.get(a)
        if not(a in s):
            s.append(a)
        for f in fils:
            if not(f in s):
                s.append(f)
    i=0
    while (i<len(s)):
        parents=parcours_largeur(g,s[i])
        if parents[target]!=None:
            return True
        i+=1
    return False