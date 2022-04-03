#Pole Trójkąta
#wzór na pole trójkąta: p  - połowa obwodu trójkąta, czyli p=(a+b+c)/2
#Aby z trzech odcinków zbudować trójkąt, najdłuższy z nich musi być krótszy niż suma długość dwóch pozostałych.

import math

bok_a = int(input("Podaj długość boku a w cm: "))
bok_b = int(input("Podaj długość boku b w cm: "))
bok_c = int(input("Podaj długość boku c w cm: ")) #bok_c będzie odpowiadał najdłuższemu z boków

trojkat = [bok_a, bok_b, bok_c]
obwod=sum(trojkat)
dluzszy=max(trojkat)
p = (bok_a + bok_b +bok_c) / 2

if obwod - dluzszy < dluzszy:
    print("Z danych boków nie można utworzyć trójkąta!")
else:
    pole = math.sqrt(p * (p- bok_a) * (p - bok_b) * (p-bok_c))
    print(f'Pole trójkąta wynosi {pole:.2f} cm2')
