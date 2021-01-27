
def move (f,t) :
    #Affichage de l'instruction "déplacez le disque de f à t"
    print("Move disc from {} to {}".format(f,t))

def MoveVia (f,v,t) :
    # Récursion, Affichage de :
    # "déplacez le disque de f à v"
    # "déplacez le disque de v à t"
    move(f,v)
    move(v,t)

def hanoi(n,f,h,t) :
    #on vérifie s'il reste un disque à déplacer
    if n==0 :
        pass
    else :
        '''S'il reste un disque,
        on considère le déplacement d'une tour
        de n-1 disque'''
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)

n = int(input("Combien de disques ?"))

hanoi(n,"A","B","C")