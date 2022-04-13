"""
pole_kola - oblicza pole koła o podanym promieniu (jeden parametr) podpowiedź:
wartość PI jest dostępna jako Math.PI
Pole koła = pi * r2
"""
import math

def pole_kola():
    r = float(input("Podaj dłgość promienia koła w cm: "))
    pi = math.pi
    pole = pi * (r ** 2)
    print(f'Pole koła wynosi {pole} cm2.')
    return pole

pole_kola()


