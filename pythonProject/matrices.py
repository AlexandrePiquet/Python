#def init_mat(n, m):

#    matrice = [[0 for i in range(m)] for j in range(n)]

#    return matrice

def print_mat(ma_matrice):
    if ma_matrice == []:
        print("\n")
    else:
        for ligne in ma_matrice:
            for colonne in ligne:
                print(colonne, end=" ")
            print(end="\n")
    return

ma_matrice = eval(input())
print_mat(ma_matrice)
