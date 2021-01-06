position_courante = 0

saut = int(input())
position_cible = int(input())
cible_atteinte = 0

position_courante += saut
position_courante = position_courante % 100

while position_courante != 0 and cible_atteinte == 0:

    if position_courante == position_cible:
        cible_atteinte = 1
    else:
        print(position_courante)
        position_courante += saut
        position_courante = position_courante % 100

if cible_atteinte == 1:
    print("Cible atteinte")
else:
    print(position_courante)
    print("Pas trouvé")
