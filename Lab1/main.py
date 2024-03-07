import math
import random

# Exercitiul 1
# Cautam precizia masinii

u = 10
while 1 + float(u / 10) != 1.0:
    u = float(u / 10)

print(f"Exercitiul 1 :", u)
print(1 + 0.000000000000001)  # u = 10^(-15)
print(1 + 0.0000000000000001)

# Exercitiul 2

x = 1.0
y = float(u / 10)
z = float(u / 10)

suma1 = (x + y) + z
suma2 = x + (y + z)
print("\nExercitiul 2\n")
print(f"Suma 1 = ", suma1)
print(f"Suma 2 = ", suma2)
if (suma1 != suma2):
    print("Operatia de adunare nu este asociativa.")
else:
    print("Operatia de adunare este asociativa.")

a = 0.2
b = 0.4
c = float(1 / 3)

mult1 = (a * b) * c
mult2 = a * (b * c)
print(f"Produsul 1 = ", mult1)
print(f"Produsul 2 = ", mult2)
if (mult1 != mult2):
    print("Operatia de inmultire nu este asociativa.")
else:
    print("Operatia de inmultire este asociativa.")

# Exercitiul 3
print("\nExercitiul 3\n")

count = 0
count_ti = {'t4': 0, 't5': 0, 't6': 0, 't7': 0, 't8': 0, 't9': 0}

while count < 10000:
    a = random.uniform(-math.pi / 2, math.pi / 2)
    standard = float(math.tan(a))

    # i = 4
    t4 = float((105 * a - 10 * (a ** 3)) / (105 - 45 * (a ** 2) + a ** 4))

    # i = 5
    t5 = float((945 * a - 105 * (a ** 3) + a ** 5) / (945 - 420 * (a ** 2) + 15 * (a ** 4)))

    # i = 6
    t6 = float((10395 * a - 1260 * (a ** 3) + 21 * (a ** 5)) / (10395 - 4725 * (a ** 2) + 210 * (a ** 4) - a ** 6))

    # i = 7
    t7 = float((135135 * a - 17325 * (a ** 3) + 378 * (a ** 5) - a ** 7) / (
            135135 - 62370 * (a ** 2) + 3150 * (a ** 4) - 28 * (a ** 6)))

    # i = 8
    t8 = float((2027025 * a - 17325 * (a ** 3) + 378 * (a ** 5) - a ** 7) / (
            2027025 - 945945 * (a ** 2) + 51975 * (a ** 4) - 630 * (a ** 6) + a ** 8))

    # i = 9
    t9 = float((34459425 * a - 4729725 * (a ** 3) + 135135 * (a ** 5) - 990 * (a ** 7) + a ** 9) / (
            34459425 - 16216200 * (a ** 2) + 945945 * (a ** 4) - 13860 * (a ** 6) + 45 * (a ** 8)))

    error4 = abs(t4 - standard)
    error5 = abs(t5 - standard)
    error6 = abs(t6 - standard)
    error7 = abs(t7 - standard)
    error8 = abs(t8 - standard)
    error9 = abs(t9 - standard)

    list_error = {'t4': error4, 't5': error5, 't6': error6, 't7': error7, 't8': error8, 't9': error9}
    sorted_list_error = dict(sorted(list_error.items(), key=lambda x: x[1])[:3])

    # print(f"Primele 3 functii cu cele mai mici erori pentru valoarea {a} : {sorted_list_error}")

    k = 3
    for ti in sorted_list_error.keys():
        count_ti[ti] += k
        k = k - 1

    count += 1

ierarhie = dict(sorted(count_ti.items(), key=lambda x: x[1], reverse=True))
print(ierarhie.keys())
