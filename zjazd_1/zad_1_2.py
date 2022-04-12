#zasadniczy problem jest taki, że nie wiem jak zapętlić dni tygodnia w taki sposób, żeby po 7 przeskakiwać spowrotem do 1-ki
#mam też problem z ułożeniem sensowengo wzoru na końcowe obliczenie.
#w wersji 1 wynik końcowy to de facto długość naprawy, w wersji dwa suma liczb z obu inputów.
#w obu wersjach coś nie gra, ale jw - podstawowy problem jest z pętlami, bo źle je ustawiam

#wersja_1

numer_dnia = 1
dzien = int(input("Podaj numer dnia, w którym pozostawiono buty: "))
dlugosc_naprawy = int(input("Podaj czas na naprawę: "))
termin = dzien + dlugosc_naprawy - ((dzien + dlugosc_naprawy) // 7) * 7

print(f'Możesz odebrać buty w dniu {termin}.')