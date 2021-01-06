def symetrie_horizontale(A):

    taille = len(A)
    B = [[0for i in range(taille)] for j in range(taille)]

    for i, ligne in enumerate(A):
        for j, colonne in enumerate(A):
            B[taille-i-1][j] = A[i][j]

    return B

print(symetrie_horizontale([]))

