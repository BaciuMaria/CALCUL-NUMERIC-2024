import numpy as np


def schema_lui_Aitken(x, y):
    n = len(x)
    y_nou = []
    for i in range(n):
        row = [0] * n
        y_nou.append(row)

    for i in range(n):
        y_nou[i][0] = y[i]

    for k in range(1, n + 1):
        for i in range(k, n):
            y_nou[i][k] = y_nou[i][k - 1] - y_nou[i - 1][k - 1]
            if k == i:
                y[i] = y_nou[i][k]

    return y


def formula_lui_Newton(x, y, x_dat):
    n = len(x)
    h = (x[n - 1] - x[0]) / (n - 1)
    t = (x_dat - x[0]) / h

    s = [0] * (n - 1)
    s[0] = t

    for k in range(1, n - 1):
        s[k] = s[k - 1] * ((t - k) / (k + 1))

    L_n = y[0]
    for i in range(1, n):
        L_n += y[i] * s[i - 1]

    return L_n


def schema_lui_Horner(grad, x0, xn, x_dat, x, y):
    x_nou = []
    y_nou = []
    for i in range(len(x)):
        if i >= x0 and i <= xn:
            x_nou.append(x[i])
            y_nou.append(y[i])

    B = matricea_B(x_nou, grad)
    a = lib_solve_sistem(B, y_nou)

    P = a[grad]
    for i in range(grad - 1, -1, -1):
        P = P * x_dat + a[i]

    return P


def lib_solve_sistem(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except Exception as e:
        print(f"A intervenit o eroare: {e}")
        return None


def matricea_B(x, grad):
    n = len(x)
    B = []

    for i in range(n):
        row = [x[i] ** j for j in range(grad + 1)]
        B.append(row)

    return B


# -------------------------------------------------------------------

x = [0, 1, 2, 3, 4, 5]
y1 = [50, 47, -2, -121, -310, -545]
y2 = [50, 47, -2, -121, -310, -545]
x_dat = 1.5
f = 30.3125

print(f"Vectorul x: {x}")
print(f"Vectorul y: {y1}")

y1 = schema_lui_Aitken(x, y1)
print(f"Noul y: {y1}")

L_n = formula_lui_Newton(x, y1, x_dat)
print(f"\nL_n pentru x = {x_dat} : {L_n}")

z1 = abs(L_n - f)
print("\n| L_n - f(x) | = ", z1)

P = schema_lui_Horner(4, 1, 5, x_dat, x, y2)
print(f"\nP pentru x = {x_dat} : {P}")

z2 = abs(P - f)
print("\n| P - f(x) | = ", z2)

suma = 0
for i in range(len(x)):
    suma += abs(schema_lui_Horner(4, 1, 5, x[i], x, y2) - y2[i])

print("\nSuma = ", suma)
