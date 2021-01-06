import random
NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)
print(secret)
essai = 1
choix = int(input())


while essai <= NB_ESSAIS_MAX:

    if essai < NB_ESSAIS_MAX:
        if choix < secret:
            print("Trop petit")
        elif choix > secret:
            print("Trop grand")
        else:
            print("Gagné en ", essai, " essais !")
            essai = NB_ESSAIS_MAX
        essai += 1
        choix = int(input())
    elif choix == secret:
        print("Gagné en ", essai, " essais !")
        essai += 1
    else:
        print("Perdu ! Le secret était ", secret)
        essai += 1