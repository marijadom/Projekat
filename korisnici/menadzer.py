from akcije.akcijeIO import ucitaj_akcije, sacuvaj_akcije
from knjige.knjigeIO import ucitaj_knjige
from pomocne.unos import validacija_unosa_broj, validacija_unosa_string
import datetime

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



