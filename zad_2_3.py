x = int(input("Podaj liczbę: "))
ile_liczb = 1
suma = x
min = x
max = x

while x != "y":
    x = input("Podaj liczbę lub kilka liczb. Kiedy skończysz, podaj [y]: ")
    if x != "y":
        x = int(x)
        suma = suma + x
        ile_liczb += 1
        srednia = suma / ile_liczb
        if min > x:
            min = x
        elif max < x:
            max = x

if ile_liczb == 1:
    print(f"Wypisałeś {ile_liczb} liczbę.")
elif ile_liczb >= 2 and ile_liczb <= 4:
    print(f"Wypisałeś {ile_liczb} liczby.")
else:
    print(f"Wypisałeś {ile_liczb} liczb.")
print(f"Średnia podanych liczb wynosi: {srednia}.")
print(f"Najmniejsza z podanych liczb to: {min}.")
print(f"Największa z podanych liczb to: {max}.")
