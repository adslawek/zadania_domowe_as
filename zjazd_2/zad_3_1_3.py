"""
Napisz funkcję, która liczy średnią z dwóch liczb.
"""

def srednia():
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    srednia_wartosc = (x + y) / 2
    print(f'Średnia wartość z dwóch podanych liczb to: {srednia_wartosc}.')
    return srednia_wartosc

srednia()
