import random
x = random.randint(0, 99)
y = random.randint(0, 99)
suma = x + y
print(f'Wylosowano liczby: {x} i {y}. Podaj ich sumę!')

while True:
    proba = int(input("Suma wylosowanych liczb: "))
    if proba == suma:
        print(f'Podałeś prawidłowy wynik. Suma wolosowanych liczb to {suma}')
        break
    else:
        print('Wynik nieprawidłowy. Próbuj dalej!')
        continue