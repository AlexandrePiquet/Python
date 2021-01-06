
def soleil_leve (heure_lever, heure_coucher, heure_actuelle):
    """ vérifie si 2 nombres sont égaux
    """

    if heure_lever < heure_coucher:
        resultat = (heure_lever <= heure_actuelle and heure_actuelle < heure_coucher)
    elif heure_coucher < heure_lever:
        resultat = (heure_actuelle < heure_coucher or heure_actuelle >= heure_lever)
    else:
        if heure_lever == 12:
            resultat = (heure_actuelle > 23)
        elif heure_lever == 0:
            resultat = (heure_actuelle < 24)


    return resultat

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

for h in range (0, 24):
    print(h, end="")
    if soleil_leve(n1, n2, h) or soleil_leve(n3, n4, h):
        print(end="\n")
    else:
        print(" *", end="\n")


