"""
1.stopy na metry: przelicza odległość wyrażoną w stopach na metry
"""
#1 stopa = 0,3048 metra

def stopy_na_metry():
    metr = 1
    stopa = float(input("Podaj ilość stóp którą chcesz przeliczyć na metry: "))
    wynik = stopa / 3.2808
    print(f'Podana w stopach wartość jest równa {wynik:.3f} m.')
    return wynik

stopy_na_metry()

def test_stopy_na_metry():
    liczba = 1
    wynik = liczba / 3.2808
    assert wynik == 0.30479999767864

