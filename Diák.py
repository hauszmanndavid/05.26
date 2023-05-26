'''Hozz létre egy Diak nevű osztályt. Attribútumai: név, osztály, születési év. Az egyik metódusa
állapítsa meg az aktuális év és a születési év alapján a diák életkorát, a másik metódusa pedig adjon
vissza egy sztringet, amelyben mondatszerűen szerepelnek a diák adatai: Szia, Kiss Péter vagyok, a
10.A osztályba járok, 16 éves vagyok.'''

class Diak:
    def __init__(self, név, osztály, év):
        self.név = név
        self.osztály = osztály
        self.év = év

    def eletkor(self):
        aktualisév = int(input("Adja meg az aktuális évet: "))
        return aktualisév - self.év

    def adatok(self):
        return "Szia, {0} vagyok, a {1} osztályba járok, {2} éves vagyok.".format(self.név, self.osztály, self.eletkor())


Lista = []
név = input("Adja meg nevét: ")
osztály = input("Adja meg hogy melyik osztályba jár: ")
év = int(input("Adja meg hogy melyik évben született: "))
diák = Diak(név,osztály,év)
Lista.append(diák)

for i in Lista:
    print(i.adatok())