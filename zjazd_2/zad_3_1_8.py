"""
mile na km
"""

def km_na_mile():
    mila = float(input("Podaj odleglosc w km: "))
    km = mila * 1.609344
    wynik = km
    print(f'{mila} m to {wynik:.2f} km.')
    return wynik

km_na_mile()