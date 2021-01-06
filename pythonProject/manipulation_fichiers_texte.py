def liste_des_mots(fichier):

    liste = []

    f = open(fichier)
    for mot in f:
        liste.append(mot)

    return liste