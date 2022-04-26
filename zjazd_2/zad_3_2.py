"""
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
Logikę obliczania liczby dni wydziel do osobnej funkcji.
"""
"""
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
Logikę obliczania liczby dni wydziel do osobnej funkcji.
"""

def miesiac_liczba_dni():
    while True:

        nazwa = ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien',
                'pazdziernik', 'listopad', 'grudzien']
        miesiac = input("Podaj miesiac: ")
        if miesiac == 'styczen' or miesiac == 'marzec' or miesiac == 'maj' or miesiac == 'lipiec' or miesiac == 'sierpien' or miesiac == 'pazdziernik' or miesiac == 'grudzien':
            print(f'Miesiac {miesiac} ma 31 dni.')
        elif miesiac == 'kwiecien' or miesiac == 'czerwiec' or miesiac == 'wrzesien' or miesiac == 'listopad':
            print(f'Miesiac {miesiac} ma 30 dni.')
        elif miesiac == 'luty':
            print(f'Luty ma 28 dni.')
            continue

        if miesiac == 'stop':
            print('Koniec psot.')
            break


miesiac_liczba_dni()