

""" programme qui enregistre les valeurs quotidiennes
   des pluies pour septembre, entrées (input)
   et affiche en sortie les valeurs de pluie demandées
   (0 pour le cumul des valeurs)"""

# 1) collecte des données
pluie_septembre = [0] * 31 # crée une liste de 31 composantes initialisées à 0
for i in range(1, 31):
   pluie_septembre[i] = int(input("pluie enregistrée le " + str(i) + " septembre :"))
# calcule la somme dans la composante 0
pluie_septembre[0] = sum(pluie_septembre)

# 2) communication des valeurs à la demande
print("Donnez le jour dont vous désirez la valeur des pluies"
     " (entre 1 et 30 pour les pluies du jour, 0 pour avoir tout le mois"
     " et -1 pour terminer)")
jour = int(input("Jour :"))
while jour > -1 and jour < 31:
   print(pluie_septembre[jour])
   jour = int(input("Jour :"))
print("Au revoir et merci ! ")

