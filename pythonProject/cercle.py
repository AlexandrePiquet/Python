"""
    Auteur : Alexandre Piquet
    Date : 10/11/2020
    But : Le programme demande le rayon et calcule la circonférence et l'aire
    Entrée : rayon
    Sorties : circonférence, aire
"""

from math import pi

# Lecture du rayon
rayon = float(input('rayon ?'))
circ = pi * rayon*2 # circonférence
aire = pi * rayon**2 # aire
# affichage
print("Circonférence : ", circ)
print("Aire          : ", aire)
