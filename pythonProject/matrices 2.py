def antisymetrique(M):

    est_antisymetrique = False
    compteur_erreur = 0

    if M == [0]:
        est_antisymetrique = True
    else:
        for i, line in enumerate(M):
            for j, col in enumerate(line):
                print()
                if M[i][j] != - M[j][i]:
                    compteur_erreur += 1

    if compteur_erreur == 0:
        est_antisymetrique = True

    return est_antisymetrique

print([[0, -5, -10, -4, -2, -2], [5, 0, -9, -7, -1, -7], [10, 9, 0, -3, -9, -9], [4, 7, 3, 0, -7, -8], [2, 1, 9, 7, 0, -10], [2, 7, 9, 8, 10, 0]])
print(antisymetrique([[0, -5, -10, -4, -2, -2], [5, 0, -9, -7, -1, -7], [10, 9, 0, -3, -9, -9], [4, 7, 3, 0, -7, -8], [2, 1, 9, 7, 0, -10], [2, 7, 9, 8, 10, 0]]))