from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike
from pomocne import unos
import datetime



def prijava():
    korisnici = ucitaj_korisnike()
    broj_pokusaja_prijave = 0
    pronadjen = False
    pronadjen_korisnik = None

    while broj_pokusaja_prijave < 3:
        korisnicko_ime = unos.validacija_unosa_string("Unesi korisnicko ime: ")
        lozinka = unos.validacija_unosa_string("Unesi lozinku: ")

        for korisnik in korisnici:
            if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka'] == lozinka:
                pronadjen = True
                pronadjen_korisnik = korisnik
        if pronadjen:
            return pronadjen_korisnik
        else:
            broj_pokusaja_prijave += 1

    return None


def registracija():
    novi_korisnik = {}

    print("1.Dodajte menadzera.")
    print("2.Dodajte prodavca.")


    while True :
        opcija = unos.validacija_unosa_broj("Unesite opciju: ")
        if opcija == 1:
            novi_korisnik['tip_korisnika'] = "Menadzer"
            break

        if opcija == 2:
            novi_korisnik['tip_korisnika'] = "Prodavac"
            break

    korisnici = ucitaj_korisnike()
    postoji = True
    korisnicko_ime = unos.validacija_unosa_string("Unesite korisnicko ime: ")
    while postoji:
        pronadjen = False
        for korisnik in korisnici:
            if korisnik['korisnicko_ime'] == korisnicko_ime:
                pronadjen = True
                break
        if pronadjen:
            print("Greska, uneto korisnicko ime vec postoji!")
            korisnicko_ime = unos.validacija_unosa_string("Unesite korisnicko ime: ")
        postoji = pronadjen

    novi_korisnik['korisnicko_ime'] = korisnicko_ime
    ime = unos.validacija_unosa_string("Unesite ime: ")
    prezime = unos.validacija_unosa_string("Unesite prezime: ")
    lozinka = unos.validacija_unosa_string("Unesite lozinku: ")
    novi_korisnik['ime'] = ime
    novi_korisnik['prezime'] = prezime
    novi_korisnik['lozinka'] = lozinka

    korisnici.append(novi_korisnik)
    sacuvaj_korisnike(korisnici)
    print("Uspesno dodat korisnik!")



def pregled_korisnika(korisnici):
        zaglavlje = f"{'korisnicko ime':<20}{'ime':<15}{'prezime':<15}{'tip korisnika':<15}"

        print(zaglavlje)
        print('-' * len(zaglavlje))

        for korisnik in korisnici:
            ispis = f"{korisnik['korisnicko_ime']:<20}{korisnik['ime']:<15}{korisnik['prezime']:<15}{korisnik['tip_korisnika']:<15}"
            print(ispis)

        print('-' * len(zaglavlje))


def sortiraj_korisnike(kljuc):
        korisnici = ucitaj_korisnike()

        for i in range(len(korisnici)):
            for j in range(len(korisnici)):
                if korisnici[i][kljuc] < korisnici[j][kljuc]:
                    temp = korisnici[i]
                    korisnici[i] = korisnici[j]
                    korisnici[j] = temp

        return korisnici

def prikazi_korisnike():
    pregled_korisnika(ucitaj_korisnike())
    print("1.Sortiraj po imenu.")
    print("2.Sortiraj po prezimenu.")
    print("3.Sortiraj po tipu korisnika.")


    stavka = int(input("Izaberite stavku: "))


    if stavka == 1:
        sortirani_korisnici = sortiraj_korisnike("ime")
        pregled_korisnika(sortirani_korisnici)
    elif stavka == 2:
        sortirani_korisnici = sortiraj_korisnike("prezime")
        pregled_korisnika(sortirani_korisnici)
    elif stavka == 3:
        sortirani_korisnici = sortiraj_korisnike("tip_korisnika")
        pregled_korisnika(sortirani_korisnici)




