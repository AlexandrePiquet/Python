""" programme qui somme les pluies pour septembre
   les valeurs quotidiennes sont entrées (input)
   et la somme est affichée en sortie"""
somme_pluie = 0
for i in range(1, 31): # du jour 1 au jour 30 (31 n'est pas inclus!)
   val = int(input("pluie enregistrée le " + str(i) + " septembre :"))
   somme_pluie += val
print("pluie cumulée pour le mois de septembre :", somme_pluie)
print("Au revoir et merci ! ")