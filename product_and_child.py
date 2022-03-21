
class Product:
    BTW = 0.21

    def __init__(self, naam, prijs, categorie):
        self._naam = naam
        self._prijs = prijs
        self._categorie = categorie

    @property
    def categorie(self):
        return self._categorie

    @property
    def naam(self):
        return self._naam

    @property
    def prijs(self):
        return self._prijs

    @prijs.setter
    def prijs(self, value):
        self._prijs = value

    def __str__(self):
        return f"{self.naam}[{self.categorie}]: {self.prijs}"

    def __repr__(self):
        return f"{self.naam}-{self.categorie}"

    def bereken_prijs_met_belastingen(self):
        return round(self.prijs + self.prijs * Product.BTW, 2)

    def kan_verkopen(self):
        return False


class VoedingsArtikkel(Product):

    def __init__(self, naam, prijs, nutri_score, verpakking):
        Product.__init__(self, naam, prijs, "voeding")
        self._nutri_score = nutri_score
        self._verpakking = verpakking

    @property
    def nutri_score(self):
        return self._nutri_score

    @property
    def verpakking(self):
        return self._verpakking

    def __str__(self):
        return f"Voeding - {self.naam} in {self.verpakking}, prijs {self.prijs}"

    def adverteer(self):
        print(f"Lekker product {self.naam}, nu maar {self.prijs}")


class MeubelArtikkel(Product):

    STOEL = 0
    TAFEL = 1
    ZETEL = 2

    def __init__(self, naam, prijs, soort, tweedehands=False):
        Product.__init__(self, naam, prijs, "meubelen")
        self._soort = soort
        self._tweedehands = tweedehands

    @property
    def soort(self):
        return self._soort

    @property
    def tweedehands(self):
        return self._tweedehands

    def __str__(self):
        soort = ["stoel", "tafel", "zetel"][self.soort]
        return f"Meubelen - {soort}({self.naam}), prijs {self.prijs} " + \
               {False: "", True: "(tweede hands)"}[self.tweedehands]

    def verkoop(self):
        self.tweedehands = True

    def verkoopprijs(self):
        return self.prijs / 2

    def kan_verkopen(self):
        return True


class BoekArtikkel(Product):

    def __init__(self, naam, prijs, aantal_paginas, tweedehands=False):
        Product.__init__(self, naam, prijs, "boek")
        self._aantal_paginas = aantal_paginas
        self._tweedehands = tweedehands

    def __str__(self):
        return f"Boek - {self.naam}, prijs {self.prijs} " + \
               {False: "", True: "(tweede hands)"}[self.tweedehands]

    @property
    def aantal_paginas(self):
        return self._aantal_paginas

    @property
    def tweedehands(self):
        return self._tweedehands


    def verkoopprijs(self):
        return self.prijs / 3

    def kan_verkopen(self):
        return True

    @classmethod
    def kopieer_machine(cls, boek):
        return cls(boek.naam, boek.prijs, boek.aantal_paginas, boek.tweedehands)


def vraag_wat_te_doen():
    print("Wat wil je doen?")
    print()
    print("1. Een artikkel kopen")
    print("2. Een artikkel verkopen")
    print("3. Een tweedehands artikkel verkopen")
    print()

    try:
        return int(input("Maak een keuze?").strip())
    except BaseException:
        return None


def vraag_product_category():
    print("Wat soort product wil je kopen?")
    print()
    print("1. voeding")
    print("2. meubelen")
    print("3. boek")
    print()

    try:
        return int(input("Maak een keuze?").strip())
    except BaseException:
        return None


def vraag_welk_product(artikkelen, categorie):

    number = 0
    van_die_soort = []

    print()

    for artikkel in artikkelen:
        if artikkel.categorie == "voeding":
            artikkel.adverteer()

    print()

    for artikkel in artikkelen:
        if artikkel.categorie == categorie:
            number += 1
            print(f"{number}. {artikkel}")
            van_die_soort.append(artikkel)

    print()

    try:
        return van_die_soort[int(input("Maak een keuze?").strip())-1]
    except BaseException:
        return None


def vraag_artikkel_om_te_verkopen(mandje):

    te_verkopen = []

    number = 0

    for artikkel in mandje:
        if artikkel.kan_verkopen():
            number += 1
            print(f"{number}. {artikkel.naam} voor {artikkel.verkoopprijs()}")
            te_verkopen.append(artikkel)

    print()

    if len(te_verkopen) == 0:
        print("Je hebt geen artikkelen om te verkopen")
        print()
        return

    try:
        return te_verkopen[int(input("Maak een keuze?").strip())-1]
    except BaseException:
        return None


def vraag_artikkel_om_tweede_hands_te_kopen(artikkelen):

    if len(artikkelen) == 0:
        print("Je hebt geen artikkelen om terug te kopen")
        return

    number = 0

    for artikkel in artikkelen:
        number += 1
        print(f"{number}. {artikkel.naam} voor {artikkel.prijs}")

    print()

    try:
        return artikkelen[int(input("Maak een keuze?").strip())-1]
    except BaseException:
        return None


if __name__ == "__main__":

    artikkelen = [

        VoedingsArtikkel("chipolata", 5.48, "D", "papier"),
        VoedingsArtikkel("speculoos", 1.18, "E", "doos"),
        VoedingsArtikkel("lasagna", 8.98, "B", "brik"),

        MeubelArtikkel("KLIPPAN", 199, MeubelArtikkel.ZETEL),
        MeubelArtikkel("ADDE", 12.50, MeubelArtikkel.STOEL),
        MeubelArtikkel("VANGSTA", 119, MeubelArtikkel.TAFEL),

        BoekArtikkel("Het gymnasium", 14, 256),
        BoekArtikkel("the midnight lock", 9.31, 125),
        BoekArtikkel("huisarrest", 22.99, 384)
    ]

    mijn_mandje = []

    tweede_hands_artikkelen = []

    while True:

        wat_te_doen = vraag_wat_te_doen()

        if wat_te_doen == 1: # kopen
            categorie = vraag_product_category()

            if categorie is None:
                continue

            artikkel = vraag_welk_product(artikkelen, ["voeding", "meubelen", "boek"][categorie-1])

            if artikkel is not None:

                print(f"Artikkel {artikkel.naam} gekocht met prijs {artikkel.bereken_prijs_met_belastingen()}")
                print()

                if artikkel.categorie == "boek":
                    artikkel = BoekArtikkel.kopieer_machine(artikkel)

                mijn_mandje.append(artikkel)

        if wat_te_doen == 2: # verkopen
            artikkel = vraag_artikkel_om_te_verkopen(mijn_mandje)

            if artikkel is not None:
                print(f"Artikkel {artikkel.naam} verkocht voor prijs {artikkel.verkoopprijs()}")
                artikkel.prijs = artikkel.verkoopprijs()

                mijn_mandje.remove(artikkel)
                tweede_hands_artikkelen.append(artikkel)

                print(mijn_mandje)
                print(tweede_hands_artikkelen)

        if wat_te_doen == 3: # tweede hands kopen
            artikkel = vraag_artikkel_om_tweede_hands_te_kopen(tweede_hands_artikkelen)

            if artikkel is not None:
                print(f"Artikkel {artikkel.naam} terug gekocht voor prijs {artikkel.prijs}")

                tweede_hands_artikkelen.remove(artikkel)
                mijn_mandje.append(artikkel)

                print(mijn_mandje)
                print(tweede_hands_artikkelen)
