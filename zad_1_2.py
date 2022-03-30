#zasadniczy problem jest taki, że nie wiem jak zapętlić dni tygodnia w taki sposób, żeby po 7 przeskakiwać spowrotem do 1-ki
#mam też problem z ułożeniem sensowengo wzoru na końcowe obliczenie.
#w wersji 1 wynik końcowy to de facto długość naprawy, w wersji dwa suma liczb z obu inputów.
#w obu wersjach coś nie gra, ale jw - podstawowy problem jest z pętlami, bo źle je ustawiam

#wersja_1

numer_dnia = 1
pozostawienie_butow = int(input("Podaj numer dnia: "))
dlugosc_naprawy = int(input("Podaj czas na naprawę: "))

for liczba in range(0,6):
    numer_dnia += 1
    if numer_dnia > 7:
        print("Podaj liczbę 1-7.")
    elif dlugosc_naprawy > 7:
        print("Nasze naprawy nie trwają dłużej niż 7 dni: ")

print(f'Możesz odebrać buty w dniu {dlugosc_naprawy}.')

#wersja_2

numer_dnia = 1
pozostawienie_butow = int(input("Podaj numer dnia: "))
dlugosc_naprawy = int(input("Podaj czas na naprawę: "))
odbior_butow = pozostawienie_butow + 5

while numer_dnia <= 1:
    numer_dnia += 1
    if numer_dnia > 7:
        print("Podaj liczbę 1-7.")
    elif odbior_butow > 7:
        print("Nasze naprawy nie trwają dłużej niż 7 dni: ")

print(f'Możesz odebrać buty w dniu {odbior_butow}.')