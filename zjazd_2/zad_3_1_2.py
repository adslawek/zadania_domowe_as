"""
Funckja, która: max - zwraca większą z dwóch liczb - postaraj się nie używać funkcji max
wbudowanej w pythona
"""

def max_liczba():
    x = float(input("Podaj pierwszą liczbę: "))
    y = float(input("Podaj drugą liczbę: "))
    if x > y:
        print(f'{x} jest większe od {y}.')
    elif y > x:
        print(f'{y} jest większe od {x}.')
    else:
        print('Podałeś/Podałaś dwie takie same liczby!')
    wynik = print(f'Maksymalna wartość z dwóch podanych liczb to {max(x, y)}.')
    return wynik

print(max_liczba())