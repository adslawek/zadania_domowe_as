"""
mile na km
"""

def mile_na_km():
    mila = float(input("Podaj odleglosc w km: "))
    km = mila * 1.609344
    wynik = km
    print(f'{mila} m to {wynik:.2f} km.')
    return wynik

mile_na_km()