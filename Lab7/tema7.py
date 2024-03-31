def schema_lui_Horner(grad, x_dat, a):
    P = a[0]
    for i in range(1, grad):
        P = P * x_dat + a[i]

    return P


def Muller(a0, x0, x1, x2, kmax, epsilon, grad):
    k = 0
    delta_x = epsilon

    while abs(delta_x) >= epsilon and k <= kmax and abs(delta_x) <= 10 ** 8:

        h0 = x1 - x0
        h1 = x2 - x1

        if h0 + h1 == 0:
            break

        delta0 = (schema_lui_Horner(grad, x1, a0) - schema_lui_Horner(grad, x0, a0)) / h0
        delta1 = (schema_lui_Horner(grad, x2, a0) - schema_lui_Horner(grad, x1, a0)) / h1
        a = (delta1 - delta0) / (h1 + h0)
        b = a * h1 + delta1
        c = schema_lui_Horner(grad, x2, a0)

        delta = b ** 2 - 4 * a * c
        rad_delta = (b ** 2 - 4 * a * c) ** 0.5

        if delta < 0:
            break

        # if abs(max(b + rad_delta, b - rad_delta)) < epsilon:
        #     break

        if abs(b - rad_delta) < abs(b + rad_delta):
            d = b + rad_delta
        else:
            d = b - rad_delta

        if d == 0:
            break

        delta_x = 2 * c / d
        x3 = x2 - delta_x
        k = k + 1
        x0 = x1
        x1 = x2
        x2 = x3

    if abs(delta_x) < epsilon:
        return k, x2
    else:
        return k, None


def find_R(a0):
    max_a = max(abs(ai) for ai in a0)

    R = (abs(a0[0]) + max_a) / abs(a0[0])

    return -R, R

def solutie(a):
    grad = len(a)
    epsilon = 10 ** (-15)

    R_neg, R = find_R(a)
    print("a = " , a)
    print("Intervalul care contine toate radacinile reale: [", R_neg, ",", R, "]")

    radacini = []

    for x0 in range(int(R_neg), int(R) + 1):
        for x1 in range(x0 + 1, int(R) + 1):
            for x2 in range(x1 + 1, int(R) + 1):
                _, radacina = Muller(a, x0, x1, x2, 10000, epsilon, grad)
                if radacina != None:
                    distincta = True
                    for r in radacini:
                        if abs(r -radacina) <= epsilon:
                            distincta = False
                    if distincta == True:
                        radacini.append(radacina)

    print("Radacinile gasite:")
    for radacina in radacini:
        print(radacina)

    f.write(f"a = {a} \n")
    f.write(f"Intervalul care contine toate radacinile reale: [ {R_neg} , {R} ] \n")
    f.write(f"Radacinile gasite:\n")
    for radacina in radacini:
        f.write(f"{radacina} \n")
    f.write("\n")


# ------------------------------------------
a0 = [1.0, -6.0, 11.0, -6.0]
a1 = [42.0, -55.0, -42.0, 49.0,-6.0]
a2 = [8.0, -38.0, 49.0, -22.0, 3.0]
a3 = [1.0, -6.0, 13.0, -12.0,4.0]

with open('radacini.txt', 'w') as f:

    solutie(a0)
    print("\n")
    solutie(a1)
    print("\n")
    solutie(a2)
    print("\n")
    solutie(a3)

    f.close()