from korisnici.korisniciIO import ucitaj_korisnike
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
    return None
