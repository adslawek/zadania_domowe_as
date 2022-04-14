"""
km to miles
"""

def km_na_mile():
    km = float(input("Podaj odleglosc w km: "))
    mila = km * 0.6213727366498067
    wynik = mila
    print(f'{km} km to w milach {wynik:.2f}.')
    return wynik

km_na_mile()

