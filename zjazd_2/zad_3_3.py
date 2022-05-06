lista_adama = [2, 22, 23, 25, 28, 99, 104, 105, 333, 698, 900]
wynik = sum(lista_adama)
print (wynik)

#srednia
srednia = sum(lista_adama) / len(lista_adama)
print(srednia)

#max
maxi = max(lista_adama)
print(maxi)

#roznica min - max
def max_minus_min(lista: list) -> int:

    mini = min(lista_adama)
    maxi = max(lista_adama)
    roznica_min_max = maxi - mini
    print(roznica_min_max)

    return roznica_min_max

max_minus_min(lista_adama)


#wypisz wieksze od x
def wypisz_wieksze(lista: list, liczba: float):
    lista_adama = [2, 22, 23, 25, 28, 99, 104, 105, 333, 698, 900]
    x = int(input("Podaj liczbe: "))
    for liczba in lista_adama:
        if liczba > x:
            print(liczba)

wypisz_wieksze(list, liczba=55)

#pierwsza wieksza
def pierwsza_wieksza(lista: list, liczba: float):
    lista_adama = [2, 22, 23, 25, 28, 99, 104, 105, 333, 698, 900]
    x = float(input("Podaj liczbe: "))
    wynik = 0
    for liczba in lista_adama:
        if x > liczba:
            return lista_adama
        else:
            return None
    return wynik

print(pierwsza_wieksza(list ,liczba=25))

#pierwsza_wieksza(liczby, x) – zwraca ( return ) pierwszą znalezioną w liczby liczbę większą od x
#zwraca None , jeśli takiej liczby tam nie ma


#wypisz_podzielne(liczby, x) – wypisuje ( print ) wszystkie te liczby z listy liczby , które są podzielne przez x

def wypisz_podzielne(lista: list, liczba: float):
    lista_adama = [2, 22, 23, 25, 28, 99, 104, 105, 333, 698, 900]
    x = float(input("Podaj liczbe: "))
    ile_liczb = 0
    for liczba in lista_adama:
        if liczba % x == 0:
            print(liczba)

    return ile_liczb

print(wypisz_podzielne(list, liczba=float))

