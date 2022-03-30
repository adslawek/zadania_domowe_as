#krok 1
waga_kg = float(input("Podaj wagę: "))
cena_za_kg = float(input("Podaj cenę za kg: "))
naleznosc = round(cena_za_kg * waga_kg, 2)
print("Należność: ", naleznosc, "PLN")

#krok 2
ilosc_ziemniakow = 5
cena_ziemniakow = float(input('Podaj cenę za kilogram: '))
naleznosc = ilosc_ziemniakow * cena_ziemniakow
print(naleznosc)

#krok 3
ziemniaki_cena_kg = float(input('Podaj cenę za kg ziemniaków: '))
waga_ziemniaków = float(input('Podaj wagę ziemniaków w kg: '))
naleznosc_1 = round(ziemniaki_cena_kg * waga_ziemniaków, 2)

banany_cena_kg = float(input('Podaj cenę za kg bananów: '))
waga_banany = float(input('Podaj wagę bananów w kg: '))
naleznosc_2 = round(banany_cena_kg * banany_cena_kg, 2)
naleznosc_suma = round((ziemniaki_cena_kg * waga_ziemniaków) + (banany_cena_kg * banany_cena_kg), 2)

print('Za banany i ziemnaiki należy się: ', naleznosc_suma, 'PLN')

if naleznosc_1 > naleznosc_2:
    print('Za ziemniaki płacisz więcej niż za banany.')
else:
    print('Za banany płacisz więcej niż za ziemniaki.')
