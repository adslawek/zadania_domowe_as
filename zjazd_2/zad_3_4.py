def policz_znaki(napis: str, start: str = '<', stop: str = '>') -> int:

    napis = input("Podaj napis: ")

    if napis.count('<') != 1 or napis.count('>') != 1:
        print('Nieprawidlowa liczba nawiasow <>')
        exit()


    if not (napis.find('<') < napis.find('>')):
        print('Zla kolejnosc nawiasow, najpierw < a pozniej >')
        exit()

    czy_zliczac = False
    liczba_znakow = 0

    for litera in napis:
        if litera == '<':
            czy_zliczac = True
        elif litera == '>':
            czy_zliczac = False
        elif czy_zliczac == True:
            liczba_znakow += 1

    print(f'W napisie "{napis}" znaleziono {liczba_znakow} znakow')

policz_znaki(napis="Ala ma kota")