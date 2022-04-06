import random
x = random.randint(0, 999)
proba = None
ilosc_prob = 0
while True:
    proba = int(input("Zgadnij jaka liczba z zakresu 0-999 została wylosowana: "))
    ilosc_prob += 1
    if proba == x:
        print(f'Gratulacje! Odgadłeś/-aś wynik! Potrzebowałeś/-aś na to {ilosc_prob} prób.')
        break
    if proba > x:
        print("Podana liczba jest większa od wylosowanej. Próbuj dalej!")
    elif proba < x:
        print("Podana liczba jest mniejsza od wylosowanej. Próbuj dalej!")