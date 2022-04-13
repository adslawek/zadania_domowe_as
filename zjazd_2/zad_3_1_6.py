"""Pole trójkąta"""

import math

def pole_trojkata_heron():

    bok_a = int(input("Podaj długość boku a w cm: "))
    bok_b = int(input("Podaj długość boku b w cm: "))
    bok_c = int(input("Podaj długość boku c w cm: ")) #bok_c będzie odpowiadał najdłuższemu z boków

    trojkat = [bok_a, bok_b, bok_c]
    obwod=sum(trojkat)
    dluzszy=max(trojkat)

    if obwod - dluzszy < dluzszy:
        print("Z danych boków nie można utworzyć trójkąta!")
    else:
        p = (bok_a + bok_b +bok_c) / 2
        print(f'Pole trójkąta wynosi {p:.2f} cm2')

pole_trojkata_heron()