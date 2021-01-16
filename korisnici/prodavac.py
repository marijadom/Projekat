from knjige.knjigeIO import ucitaj_knjige
import uuid
from pomocne.unos import validacija_unosa_broj
from racun.racunIO import ucitaj_racune, sacuvaj_racune
import datetime
from akcije.akcijeIO import ucitaj_akcije

def unos_kolicine_knjiga():
    kolicina = int(validacija_unosa_broj("Unesite kolicinu: "))
    while kolicina <1:
        kolicina = int(validacija_unosa_broj("Unesite kolicinu: "))
    return kolicina


def kupovina_preko_sifre_knjige():
    sifra_knjige = int(validacija_unosa_broj("Unesite sifru knjige: "))
    knjige = ucitaj_knjige()
    for knjiga in knjige:
        if knjiga['sifra'] == sifra_knjige:
            kolicina = unos_kolicine_knjiga()

            return knjiga, kolicina


def dodaj_knjigu_na_racun(racun, knjiga, cena, kolicina):
    if str(knjiga['sifra']) in racun['knjige']:
        racun['knjige'][str(knjiga['sifra'])]["kolicina"] += kolicina
    else:
        racun['knjige'][str(knjiga['sifra'])] = {
            "kolicina": kolicina,
            "autor": knjiga['autor'],
            "kategorija": knjiga['kategorija'],
            "izdavac": knjiga['izdavac'],
            "naslov": knjiga['naslov'],
            "cena": cena
        }

    racun['ukupna cena'] = racun['ukupna cena'] + cena * kolicina
    return racun

def pronadji_knjigu_po_sifri(sifra):
    knjige = ucitaj_knjige()
    for knjiga in knjige:
        if knjiga['sifra'] == sifra:
            return knjiga



def prodaja_knjiga(prodavac):
    print("1. Kupovina preko sifre knjige.")
    print("2. Kupovina preko sifre akcije.")
    print("3. Pregled korpe.")
    print("4. Zavrsi kupovinu.")

    print("0. Otkazi kupovinu.")

    opcija = int(input("Izaberite opciju: "))
    racun = {
        "sifra": uuid.uuid1().int,
        "knjige": {},
        "prodavac": prodavac['ime'] + " " + prodavac['prezime'],
        "ukupna cena": 0

    }

    while opcija != 0:
        if opcija == 1:
            kupljena_knjiga, kolicina = kupovina_preko_sifre_knjige()
            racun = dodaj_knjigu_na_racun(racun, kupljena_knjiga, kupljena_knjiga['cena'], kolicina)

        if opcija == 2:
            sifra_akcije = int(validacija_unosa_broj("Unesite sifru akcije: "))
            postojece_akcije = ucitaj_akcije()
            for akcija in postojece_akcije:
                if akcija['sifra'] == sifra_akcije and datetime.datetime.now() < datetime.datetime.strptime(akcija['datum vazenja'], "%x"):
                    for sifra in akcija['knjige'].keys():
                        knjiga = pronadji_knjigu_po_sifri(int(sifra))
                        racun = dodaj_knjigu_na_racun(racun, knjiga, akcija['knjige'][sifra]['nova cena'], 1)


        if opcija == 3:
            sifre_knjiga = racun['knjige'].keys()
            for sifra in sifre_knjiga:
                print("Kupljeno je {0} knjiga sa sifrom {1}".format(racun['knjige'][sifra], sifra))
            print("Trenutno stanje racuna je : " + str(racun['ukupna cena']))

        if opcija == 4:

            trenutni_datum = datetime.datetime.now()
            racun['datum i vreme'] = trenutni_datum.strftime("%d/%m/%Y %H:%M")

            postojeci_racuni = ucitaj_racune()
            postojeci_racuni.append(racun)
            sacuvaj_racune(postojeci_racuni)
            break



        if opcija == 0:
            break

        print("1. Kupovina preko sifre knjige.")
        print("2. Kupovina preko sifre akcije.")
        print("3. Pregled korpe.")
        print("4. Zavrsi kupovinu.")

        print("0. Otkazi kupovinu.")

        opcija = int(input("Izaberite opciju: "))

