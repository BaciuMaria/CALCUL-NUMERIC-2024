import random

import numpy as np
import math
def inmultireA_x(A, s):
    n = len(s)
    b = [0] * n

    for i in range(n):
        for j in range(n):
            b[i] += s[j] * A[i][j]

    return b

def transpusa(A):
    r = len(A)
    c = len(A[0])

    A_T = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            A_T[j][i] = A[i][j]

    return A_T

def descompunere_QR_Householder(A, epsilon=1e-10):
    n = len(A)
    Q = [[0] * n for _ in range(n)]
    for i in range(n):
        Q[i][i] = 1

    R = [row[:] for row in A]

    for r in range(n - 1):
        sigma = sum(R[i][r] ** 2 for i in range(r, n))
        if sigma <= epsilon:
            break

        k = (sigma ** 0.5)
        if R[r][r] > 0:
            k = -k

        beta = sigma - k * R[r][r]

        u = [0] * n
        u[r] = R[r][r] - k
        for i in range(r + 1, n):
            u[i] = R[i][r]

        for j in range(r, n):
            gamma = sum(u[i] * R[i][j] for i in range(r, n)) / beta
            for i in range(r, n):
                R[i][j] -= gamma * u[i]

        for i in range(n):
            gamma = sum(Q[j][i] * u[j] for j in range(r, n)) / beta
            for j in range(r, n):
                Q[j][i] -= gamma * u[j]

    return Q, R

# 3

def diferentaA_B(A, B):
    if len(A) != len(B):
        return 0
    else:
        dif = [0] * len(A)
        for i in range(len(A)):
            dif[i] = A[i] - B[i]
        return dif

def diferenta_matrici(A, B):
    if len(A) != len(B):
        return 0
    else:
        dif = [[0] * len(A) for _ in range(len(A))]
        for i in range(len(A)):
            for j in  range(len(A)):
                dif[i][j] = A[i][j] - B[i][j]
        return dif
def qr_numpy_solve(A, b):
    Q, R = np.linalg.qr(A)
    x_qr = np.linalg.solve(R, np.dot(Q.T, b))
    return x_qr

def substitutie_inversa(A, b):
    n = len(A)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        if abs(A[i][i]) < epsilon:
            print("Impartire la zero detectata in substitutie_inversa. Nu se poate face impartirea.")
            return None
        if i == n - 1:
            x[i] = b[i]/A[i][i]
        else:
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n)))/A[i][i]
    return x

def norma_Euclidiana(Z):
    return math.sqrt(sum(Z[i] ** 2 for i in range(len(Z))))

def norma_Euclidiana2(Z):
    return math.sqrt(sum(Z[i][j] ** 2 for i in range(len(Z)) for j in range(len(Z[0]))))



def inversa_matricei_A(Q_T,R):
    n = len(R)
    A_invers_householder = [[0] * n for _ in range(n)]

    for j in range(n):
        b = [0] * n
        for i in range(n):
            b[i] = Q_T[i][j]

        x_stea = substitutie_inversa(R, b)

        for i in range(n):
            A_invers_householder[i][j] = x_stea[i]

    return A_invers_householder

def random_matrix(length):
    A = [[0] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            A[i][j] = round(random.uniform(-100,100),2)

    return A

def random_s(length):
    s = [0] * length

    for i in range(length):
        s[i] = round(random.uniform(-100, 100),2)
    return s

A = [[0, 0, 4],
     [1, 2, 3],
     [0, 1, 2]]
s = [3, 2, 1]
epsilon = 10 **(-5)

b = inmultireA_x(A, s)
print("Vectorul b este:", b)

Q_T, R = descompunere_QR_Householder(A)
Q = transpusa(Q_T)

print("Matricea Q:")
for row in Q:
    print(row)
print("\nMatricea R:")
for row in R:
    print(row)

C=inmultireA_x(Q_T,b)
print("\nC: ", C)


x_qr = qr_numpy_solve(A, b)
print(x_qr)

x_householder = substitutie_inversa(R, C)
print("\nx_Householder:", x_householder)

z1 = norma_Euclidiana(diferentaA_B(x_qr, x_householder))
print("\nNorma euclidiana z1: ", z1)

inmultire1 = inmultireA_x(A,x_householder)
z2 = norma_Euclidiana(diferentaA_B(inmultire1,b))
print("\nNorma euclidiana z2: ", z2)

inmultire2 = inmultireA_x(A,x_qr)
z3 = norma_Euclidiana(diferentaA_B(inmultire2,b))
print("\nNorma euclidiana z3: ", z3)

diferenta1 = diferentaA_B(x_householder,s)
z4 = norma_Euclidiana(diferenta1)
z5 = norma_Euclidiana(s)
z6 = z4 / z5
print("\nNorma euclidiana z6: ", z6)

diferenta2 = diferentaA_B(x_qr,s)
z7 = norma_Euclidiana(diferenta2)
z8  = z7/ z5
print("\nNorma euclidiana z8: ", z8)

A_householder = inversa_matricei_A(Q_T,R)
print("\nInversa matricei A:")
for row in A_householder:
    print(row)
A_inv_bibl = np.linalg.inv(A)
z9 = norma_Euclidiana2(diferenta_matrici(A_householder,A_inv_bibl))
print("\nNorma euclidiana z9: ", z9)

n_gen = random.randint(2,10)
A_gen = random_matrix(n_gen)
print("Matricea A_gen:")
for row in A_gen:
    print(row)
s_gen = random_s(n_gen)
print("Vectorul s_gen este:", s_gen)
