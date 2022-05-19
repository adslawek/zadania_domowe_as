import math

class Robot:
    def __init__(self, x, y, zwrot):
        self.x = x
        self.y = y
        self.zwrot = zwrot

    def wypisz(self):
        print(f"Aktualne polozenie robota: {self.x}/{self.y}, zwrot: {self.zwrot}.")

    def lewo(self):
        if self.zwrot == 'N':
            self.zwrot == 'W'
        elif self.zwrot == 'W':
            self.zwrot == 'S'
        elif self.zwrot == 'S':
            self.zwrot == 'E'
        elif self.zwrot == 'E':
            self.zwrot == 'N'

    def prawo(self):
        if self.zwrot == 'N':
            self.zwrot == 'E'
        elif self.zwrot == 'E':
            self.zwrot == 'S'
        elif self.zwrot == 'S':
            self.zwrot == 'W'
        elif self.zwrot == 'W':
            self.zwrot == 'N'

    def naprzod(self):
        if self.zwrot == 'N':
            self.y += 1
        elif self.zwrot == 'S':
            self.y -= 1
        elif self.zwrot == 'W':
            self.x -= 1
        elif self.zwrot == 'E':
            self.x += 1
        else:
            print('ERROR! NIEPRAWIDLOWY KIERUNEK!')

    def wykonaj(self, ciag_instrukcji):
        for instrukcja in ciag_instrukcji:
            if instrukcja == 'N':
                self.naprzod()
            elif instrukcja == 'L':
                self.lewo()
            elif instrukcja == 'P':
                self.prawo()

robocop = Robot(15,15, "N")
robocop.wypisz()
robocop.lewo()
robocop.wypisz()
robocop.naprzod()
robocop.wypisz()
robocop.naprzod()
robocop.prawo()
robocop.naprzod()
robocop.wypisz()
robocop.wykonaj("NLPPLN")
robocop.wypisz()


