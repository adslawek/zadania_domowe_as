#wersja1

wysokosc = int(input("podaj wysokość choinki: "))
a = 1
while a < wysokosc + 1:
    print(" " * (2*wysokosc - 2*a), " *"*a, "* "*(a-1))
    a += 1

#Matematykę skończyłem na poziomie szkoły średniej, to zadanie jest jednak matematycznie skomplikowane.
#Przydałyby się wytłuamczenia jak to obliczyć, bo bez pomocy Mikołaja na pewno bym tego nie ogarnął.

#wersja2
from turtle import color, begin_fill, end_fill

wysokosc = int(input('podaj wysokość choinki: '))

color("green")
begin_fill()
for i in range(wysokosc):
    print((' ' * (wysokosc - i)) + ('*' * ((2 * i) + 1)))

end_fill()

#próbowałem pokolorować, ale nie wyszło