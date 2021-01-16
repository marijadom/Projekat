from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from knjige.knjigeIO import ucitaj_knjige
from pomocne.unos import validacija_unosa_broj, validacija_unosa_string
import datetime
from racun.racunIO import ucitaj_racune

def kreiraj_akciju():

    postojece_akcije = ucitaj_akcije()
    akcija = {
        "sifra": len(postojece_akcije) + 1,
        "knjige": {}
    }
    postojece_knjige = ucitaj_knjige()
    sifra_knjige = int(validacija_unosa_broj("Unesite sifru knjige (0 za prekid unosa): "))

    while sifra_knjige != 0:
        for knjiga in postojece_knjige:
            if knjiga['sifra'] == sifra_knjige:
                nova_cena = validacija_unosa_broj("Unesite novu cenu knjige: ")
                akcija['knjige'][sifra_knjige] = {
                    "nova cena": nova_cena,
                    "naslov": knjiga['naslov'],
                    "autor": knjiga['autor'],
                    "kategorija": knjiga['kategorija']

                }

        sifra_knjige = int(validacija_unosa_broj("Unesite sifru knjige (0 za prekid unosa): "))

    datum_unos = validacija_unosa_string("Unesite datum vazenja akcije (dan,mesec,godina): ")
    obradjeni_unos = datum_unos.split(",")
    datum_vazenja_akcije = datetime.datetime(int(obradjeni_unos[2]), int(obradjeni_unos[1]), int(obradjeni_unos[0]))
    akcija['datum vazenja'] = datum_vazenja_akcije.strftime("%x")

    postojece_akcije.append(akcija)
    sacuvaj_akcije(postojece_akcije)

def kreiraj_izvestaj():
    print("1.Ukupna prodaja svih knjiga.")
    print("2.Ukupna prodaja svih akcija.")
    print("3.Ukupna prodaja svih knjiga po odredjenom kriterijumu.")
    opcija = int(validacija_unosa_broj("Unesite opciju: "))

    if opcija == 1:
        izvestaj_knjige()

    if opcija == 2:
        pass

    if opcija == 3:
        izvestaj_knjige_pretraga()

def izvestaj_knjige():
    racuni = ucitaj_racune()
    izvestaj = {}

    for racun in racuni:
        for sifra_knjige in racun['knjige'].keys():
            if sifra_knjige not in izvestaj:
                izvestaj[sifra_knjige] = {
                    "naslov": racun['knjige'][sifra_knjige]['naslov'],
                    "autor": racun['knjige'][sifra_knjige]['autor'],
                    "ukupna kolicina": racun['knjige'][sifra_knjige]['kolicina'],
                    "ukupna zarada": racun['knjige'][sifra_knjige]['cena'] * racun['knjige'][sifra_knjige]['kolicina']
                }

            else:
                izvestaj[sifra_knjige]['ukupna kolicina'] += racun['knjige'][sifra_knjige]['kolicina']
                izvestaj[sifra_knjige]['ukupna zarada'] += racun['knjige'][sifra_knjige]['cena'] * racun['knjige'][sifra_knjige]['kolicina']

    zaglavlje = f"{'naslov':<30}{'autor':<30}{'ukupna kolicina':<16}{'ukupna zarada':<10}"

    print(zaglavlje)
    print('-' * len(zaglavlje))

    for knjiga in izvestaj.values():
        ispis = f"{knjiga['naslov']:<30}{knjiga['autor']:<30}{knjiga['ukupna kolicina']:<16}{knjiga['ukupna zarada']:<10}"
        print(ispis)

    print('-' * len(zaglavlje))


def izvestaj_knjige_pretraga():
    print("1.Ukupna prodaja svih knjiga odabranog autora.")
    print("2.Ukupna prodaja svih knjiga odabranog izdavaca.")
    print("3.Ukupna prodaja svih knjiga odabrane kategorije.")
    opcija = int(validacija_unosa_broj("Unesite opciju: "))
    racuni = ucitaj_racune()
    izvestaj = {}

    if opcija == 1:
        unos = validacija_unosa_string("Unesite autora: ")
        for racun in racuni:
            for sifra_knjige in racun['knjige'].keys():
                if sifra_knjige not in izvestaj:
                    if racun['knjige'][sifra_knjige]['autor'].lower() == unos.lower():
                        izvestaj[sifra_knjige] = {
                            "naslov": racun['knjige'][sifra_knjige]['naslov'],
                            "autor": racun['knjige'][sifra_knjige]['autor'],
                            "ukupna kolicina": racun['knjige'][sifra_knjige]['kolicina'],
                            "ukupna zarada": racun['knjige'][sifra_knjige]['cena'] * racun['knjige'][sifra_knjige][
                                'kolicina']
                        }

                else:
                    if racun['knjige'][sifra_knjige]['autor'].lower() == unos.lower():
                        izvestaj[sifra_knjige]['ukupna kolicina'] += racun['knjige'][sifra_knjige]['kolicina']
                        izvestaj[sifra_knjige]['ukupna zarada'] += racun['knjige'][sifra_knjige]['cena'] * \
                                                                   racun['knjige'][sifra_knjige]['kolicina']

    if opcija == 2:
        unos = validacija_unosa_string("Unesite izdavaca: ")
        for racun in racuni:
            for sifra_knjige in racun['knjige'].keys():
                if sifra_knjige not in izvestaj:
                    if racun['knjige'][sifra_knjige]['izdavac'].lower() == unos.lower():
                        izvestaj[sifra_knjige] = {
                            "naslov": racun['knjige'][sifra_knjige]['naslov'],
                            "autor": racun['knjige'][sifra_knjige]['autor'],
                            "ukupna kolicina": racun['knjige'][sifra_knjige]['kolicina'],
                            "ukupna zarada": racun['knjige'][sifra_knjige]['cena'] * racun['knjige'][sifra_knjige][
                                'kolicina']
                        }

                else:
                    if racun['knjige'][sifra_knjige]['izdavac'].lower() == unos.lower():
                        izvestaj[sifra_knjige]['ukupna kolicina'] += racun['knjige'][sifra_knjige]['kolicina']
                        izvestaj[sifra_knjige]['ukupna zarada'] += racun['knjige'][sifra_knjige]['cena'] * \
                                                                   racun['knjige'][sifra_knjige]['kolicina']

    if opcija == 3:
        unos = validacija_unosa_string("Unesite kategoriju: ")
        for racun in racuni:
            for sifra_knjige in racun['knjige'].keys():
                if sifra_knjige not in izvestaj:
                    if racun['knjige'][sifra_knjige]['kategorija'].lower() == unos.lower():
                        izvestaj[sifra_knjige] = {
                            "naslov": racun['knjige'][sifra_knjige]['naslov'],
                            "autor": racun['knjige'][sifra_knjige]['autor'],
                            "ukupna kolicina": racun['knjige'][sifra_knjige]['kolicina'],
                            "ukupna zarada": racun['knjige'][sifra_knjige]['cena'] * racun['knjige'][sifra_knjige][
                                'kolicina']
                        }

                else:
                    if racun['knjige'][sifra_knjige]['kategorija'].lower() == unos.lower():
                        izvestaj[sifra_knjige]['ukupna kolicina'] += racun['knjige'][sifra_knjige]['kolicina']
                        izvestaj[sifra_knjige]['ukupna zarada'] += racun['knjige'][sifra_knjige]['cena'] * \
                                                                   racun['knjige'][sifra_knjige]['kolicina']
    zaglavlje = f"{'naslov':<30}{'autor':<30}{'ukupna kolicina':<16}{'ukupna zarada':<10}"

    print(zaglavlje)
    print('-' * len(zaglavlje))

    for knjiga in izvestaj.values():
        ispis = f"{knjiga['naslov']:<30}{knjiga['autor']:<30}{knjiga['ukupna kolicina']:<16}{knjiga['ukupna zarada']:<10}"
        print(ispis)

    print('-' * len(zaglavlje))






