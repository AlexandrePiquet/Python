from CONFIGS import *

def lire_matrice(fichier):

    matrice = []
    f = open(fichier)
    for ligne in f:
        element = ligne.split()
        element = [int(i) for i in element]
        #print(element)
        matrice.append(element)

    #print(matrice)

    return matrice

def calculer_pas(matrice):

    print("calculer_pas")
    #print(ZONE_PLAN_MINI[0])
    #print(ZONE_PLAN_MAXI[0])

    #print("2")

    a = (ZONE_PLAN_MAXI[0] - ZONE_PLAN_MINI[0])
    b = (ZONE_PLAN_MAXI[1] - ZONE_PLAN_MINI[1])

    #print("a, b", a, b)

    largeur = a // len(matrice[0])
    hauteur = b // len(matrice)

    #print("largeur, hauteur", largeur, hauteur)

    dimension = min(largeur, hauteur)

    #print("dimension", dimension)

    return dimension

def coordonnees(case, pas):

    a = int(pas * case[0] - ZONE_PLAN_MINI[0] )
    b = int(pas * case[1] - ZONE_PLAN_MAXI[1] )

    coordonnees = (a, b)

    return coordonnees

def tracer_carre(dimension):

    return resultat

def tracer_case(case, couleur, pas):

    return resultat





def afficher_plan(matrice):

    import turtle

    dimension = calculer_pas(matrice)


    return resultat

matrice = lire_matrice("plan_chateau.txt")

#print("matrie", matrice)

#print("test")

print("calculer_pas", calculer_pas(matrice))

print(coordonnees((1,2), calculer_pas(matrice)))


