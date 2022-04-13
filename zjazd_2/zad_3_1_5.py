#BMI

def oblicz_BMI():
    wzrost = float(input("Podaj swój wzrost w cm: "))
    masa = float(input("Podaj masę ciała w kg: "))
    BMI = 10000 * (masa / (wzrost ** 2))
    print(f'Twój współczynnik BMI wynosi {BMI:.2f}')

    if BMI < 16:
        print("Twoje BMI wskazuje na wygłodzenie. Pilnie skontaktuj się z lekarzarzem!")
    elif BMI >= 16 and BMI <= 16.99:
        print("Twoje BMI wskazuje na wychudzenie. Zalecamy pilny kontakt z lekarzem!")
    elif BMI >= 17 and BMI <= 18.49:
        print("Cierpisz na niedowagę. Zalecamy konsultacje z lekarzem lub dietetykiem.")
    elif BMI >= 25 and BMI <= 29.99:
        print("Cierpisz na nadwagę. Zalecamy konsultacje z lekarzem lub dietetykiem.")
    elif BMI >= 30 and BMI <= 34.99:
        print("Twoje BMI wskazuje na I stopień otyłości. Zalecamy kontakt z lekarzem!")
    elif BMI >= 35 and BMI <= 39.99:
        print("Twoje BMI wskazuje na I stopień otyłości. Zalecamy pilny kontakt z lekarzem!")
    elif BMI > 40:
        print("Cierpisz na skrajną otyłość. Pilnie skontaktuj się z lekarzem!")
    else:
        print("Wartość BMI jest w normie. Twoja waga jest prawidłowa!")
    print(
        "Utrzymanie prawidłowej masy ciała jest ważne ze względu na lepsze samopoczucie oraz zdrowie i dłuższe życie.")
    return BMI

oblicz_BMI()
