import requests
import math


def citeste_date(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip().split('\n')
        else:
            print("Eroare: Nu s-a putut prelua datele de pe site.")
            return None
    except Exception as e:
        print("Eroare:", e)
        return None


def metoda2(numar):
    url_matrice = f"https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/a_{numar}.txt"
    url_vector = f"https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/b_{numar}.txt"

    date_matrice = citeste_date(url_matrice)
    date_vector = citeste_date(url_vector)

    if date_matrice and date_vector:
        n = int(date_matrice[0])
        date = []

        for linie in date_matrice[1:]:
            valoare, i, j = map(float, linie.strip().split(','))
            i = int(i)
            j = int(j)
            date.append((valoare, i, j))
        date.sort(key=lambda x: x[1])

        valori = []
        ind_col = []
        inceput_linii = [0]
        new_row = 0

        for valoare, i, j in date:
            valori.append(valoare)
            ind_col.append(j)
            if i != new_row:
                inceput_linii.append(len(valori) - 1)
                new_row = i

        inceput_linii.append(len(valori))

        b = [float(x.split(',')[0]) for x in date_vector[1:]]

        return n, valori, ind_col, inceput_linii, b
    else:
        return None


def citeste_matrice_si_vector(numar):
    url_matrice = f"https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/a_{numar}.txt"
    url_vector = f"https://profs.info.uaic.ro/~ancai/CN/lab/4/sislinrar/b_{numar}.txt"

    date_matrice = citeste_date(url_matrice)
    date_vector = citeste_date(url_vector)

    if date_matrice and date_vector:
        n = int(date_matrice[0])
        matrice = [[] for _ in range(n)]
        for linie in date_matrice[1:]:
            valoare, i, j = map(float, linie.strip().split(','))
            i = int(i)
            j = int(j)
            matrice[i].append((valoare, j))

        b = [float(x.split(',')[0]) for x in date_vector[1:]]

        return n, matrice, b
    else:
        return None


def GaussSeidel(A, b, kmax, epsilon):
    n = len(A)
    x_gs = [0] * n
    k = 0
    delta_x = epsilon
    while delta_x >= epsilon and k <= kmax and delta_x <= 10 ** 8:
        suma_delta = 0
        for i, lista in enumerate(A):
            suma = sum(valoare * x_gs[j] for valoare, j in lista if j != i)
            aii = next(valoare for valoare, j in lista if j == i)
            suma_delta += ((b[i] - suma) / aii - x_gs[i]) ** 2
            x_gs[i] = (b[i] - suma) / aii

        delta_x = math.sqrt(suma_delta)
        k = k + 1

    if delta_x < epsilon:
        return k, x_gs
    else:
        return k, 0


def GaussSeidel_2(valori, ind_col, inceput_linii, b, kmax, epsilon):
    n = len(inceput_linii) - 1
    x_gs = [0] * n
    k = 0
    delta_x = epsilon
    while delta_x >= epsilon and k <= kmax and delta_x <= 10 ** 8:
        suma_delta = 0
        for i in range(n):
            elem_pe_linie = inceput_linii[i + 1] - inceput_linii[i]

            suma = sum(
                valori[inceput_linii[i] + j] * x_gs[ind_col[inceput_linii[i] + j]] for j in range(elem_pe_linie) if
                ind_col[inceput_linii[i] + j] != i)
            aii = next(valori[inceput_linii[i] + j] for j in range(elem_pe_linie) if ind_col[inceput_linii[i] + j] == i)
            suma_delta += ((b[i] - suma) / aii - x_gs[i]) ** 2
            x_gs[i] = (b[i] - suma) / aii

        delta_x = math.sqrt(suma_delta)
        k = k + 1

    if delta_x < epsilon:
        return k, x_gs
    else:
        return k, 0


def norma_absoluta(x):
    return sum(abs(valoare) for valoare in x)


def norma_Euclidiana(Z):
    return math.sqrt(sum(Z[i] ** 2 for i in range(len(Z))))


def norma_maxima(x):
    return max(abs(valoare) for valoare in x)


def diferentaA_B(A, B):
    if len(A) != len(B):
        return 0
    else:
        dif = [0] * len(A)
        for i in range(len(A)):
            dif[i] = A[i] - B[i]
        return dif


def inmultireA_x(A, s):
    n = len(s)
    b = [0] * n

    for i, lista in enumerate(A):
        for valoare, j in lista:
            b[i] += s[j] * valoare

    return b


def inmultireA_x_2(valori, ind_col, inceput_linii, s):
    n = len(s)
    b = [0] * n

    for i in range(len(inceput_linii) - 1):
        elem_pe_linie = inceput_linii[i + 1] - inceput_linii[i]
        for j in range(elem_pe_linie):
            b[i] += s[ind_col[inceput_linii[i] + j]] * valori[inceput_linii[i] + j]

    return b


def check_diagonala(A):
    for i, lista in enumerate(A):
        diag_null = True
        for valoare, j in lista:
            if j != i:
                diag_null = False
        if diag_null:
            return False
    return True


def check_diagonala_2(ind_col, inceput_linii):
    for i in range(len(inceput_linii) - 1):
        elem_pe_linie = inceput_linii[i + 1] - inceput_linii[i]
        diag_null = True
        for j in range(elem_pe_linie):
            if ind_col[inceput_linii[i] + j] != i:
                diag_null = False
        if diag_null:
            return False
    return True


# ---------------------------------------------------------------------
num = 2
epsilon = 10 ** (-15)

n, A, b = citeste_matrice_si_vector(num)

# if n and A and b:
#     print("Dimensiunea sistemului:", n)
#     print("Matricea rară A:", A)
#     print("Vectorul termenilor liberi b:", b)
#
if check_diagonala(A):
    iteratia, x_GS = GaussSeidel(A, b, 10000, epsilon)
    if x_GS == 0:
        print("Divergenta\n")
    else:
        print("Solutia x_GS:")
        print(x_GS)
        print(f"{iteratia} iteratii.")

        A_GS = inmultireA_x(A, x_GS)
        z1 = norma_maxima(diferentaA_B(A_GS, b))
        print("\nNorma maxima z1: ", z1)

else:
    print("Matricea A nu are toate elementele diagonalei nenule.")

n2, valori, ind_col, inceput_linii, b2 = metoda2(num)

if check_diagonala_2(ind_col, inceput_linii):
    iteratia, x_GS = GaussSeidel_2(valori, ind_col, inceput_linii, b2, 10000, epsilon)
    if x_GS == 0:
        print("Divergenta\n")
    else:
        print("Solutia x_GS:")
        print(x_GS)
        print(f"{iteratia} iteratii.")

        A_GS = inmultireA_x_2(valori, ind_col, inceput_linii, x_GS)
        z2 = norma_maxima(diferentaA_B(A_GS, b2))
        print("\nNorma maxima z2: ", z2)

else:
    print("Matricea A nu are toate elementele diagonalei nenule.")
