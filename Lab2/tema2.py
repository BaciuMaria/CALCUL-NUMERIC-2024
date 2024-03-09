import math
import numpy as np

# -------- FUNCTII ---------
def descompunereLU(A_init):
    n = len(A_init)
    A = []
    for i in range(n):
        A.append([0] * n)

    for p in range(n):
        if p == 0:
            for i in range(n):
                A[i][0] = A_init[i][0]
                if i > 0:
                    A[0][i] = A_init[0][i] / A[0][0]
        else:
            for i in range(p, n):
                A[i][p] = (A_init[i][p] - sum(A[i][k] * A[k][p] for k in range(p)))
                if A[p][p] == 0:
                    raise ValueError("Descompunerea LU nu poate fi calculata.")
            for i in range(p + 1, n):
                A[p][i] = (A_init[p][i] - sum(A[p][k] * A[k][i] for k in range(p))) / A[p][p]
    return A


def determinant_matrice_triunghiulara(A):
    det_A = 1

    n = len(A)

    for i in range(n):
        det_A *= A[i][i]

    return det_A


def substitutie_directa(A, b):
    n = len(A)
    x = [0] * n

    for i in range(n):
        if abs(A[i][i]) < epsilon:
            print("Impartire la zero detectata in substitutie_directa. Nu se poate face impartirea.")
            return None
        if i == 0:
            x[i] = b[i] / A[i][i]
        else:
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i))) / A[i][i]
    return x


def substitutie_inversa(A, b):
    n = len(A)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        if abs(A[i][i]) < epsilon:
            print("Impartire la zero detectata in substitutie_inversa. Nu se poate face impartirea.")
            return None
        if i == n - 1:
            x[i] = b[i]
        else:
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n)))
    return x

def inmultireA_x(A, x):
    n = len(A)
    y = [0] * n
    for i in range(n):
        for j in range(n):
            y[i] += A[i][j] * x[j]
    return y

def diferentaA_B(A, B):
    if len(A) != len(B):
        return 0
    else:
        dif = [0] * len(A)
        for i in range(len(A)):
            dif[i] = A[i] - B[i]
        return dif

def norma_Euclidiana(Z):
    return math.sqrt(sum(Z[i] ** 2 for i in range(len(Z))))

def inversa_matrice(A):
    try:
        inversa_A = np.linalg.inv(A)
        return inversa_A
    except np.linalg.LinAlgError:
        print("Matricea nu este inversabilă.")
        return None

def lib_solve_sistem(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except Exception as e:
        print(f"A intervenit o eroare: {e}")
        return None

# -------------------------------------------

n = 3
t = 5
epsilon = 10 ** (-t)
A_init = [[2.5, 2, 2],
          [5, 6, 5],
          [5, 6, 6.5]]
B = [[1, 2, 3, 4, 5],
     [5, 6, 7, 8, 9],
     [9, 1, 2, 3, 4],
     [4, 5, 6, 1, 8],
     [9, 1, 2, 3, 5]]

b = [2, 2, 2]

try:
    A = descompunereLU(A_init)

    print("Matricea A initiala:")
    for row in A_init:
        print(row)
    print("Matricea A:")
    for row in A:
        print(row)

    # det_A = determinant_matrice_triunghiulara(L) * determinant_matrice_triunghiulara(U)
    # determinant_matrice_triunghiulara(U) -> 1
    print("\nDeterminantul lui A:", determinant_matrice_triunghiulara(A) )

    y = substitutie_directa(A, b)
    if y is not None:
        x_LU = substitutie_inversa(A, y)
        if x_LU is not None:
            print("\nSolutia x_(LU) pentru Ax = b:", x_LU)

    A_x = inmultireA_x(A_init, x_LU)
    Z = norma_Euclidiana(diferentaA_B(A_x, b))
    print(f"\nNorma Euclidiana Z : {Z}")

    x_lib = lib_solve_sistem(A_init, b)
    Z1 = norma_Euclidiana(diferentaA_B(x_LU, x_lib))
    print(f"Norma Euclidiana Z1 : {Z1}")

    inversa_A = inversa_matrice(A_init)
    A_b = inmultireA_x(inversa_A,b)
    Z2 = norma_Euclidiana(diferentaA_B(x_LU, A_b))
    print(f"Norma Euclidiana Z2 : {Z2}")

except ValueError as e:
    print(e)
