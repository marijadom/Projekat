from korisnici.korisnici import prijava, registracija, prikazi_korisnike
from knjige.knjige import prikazi_knjige, pretrazi_knjige, dodaj_knjigu, izmena_knjige
from pomocne import unos
from korisnici.prodavac import prodaja_knjiga
from korisnici.menadzer import kreiraj_akciju
from akcije.akcije import prikaz_tabele_akcija, pretrazi_akcije
from akcije.akcijeIO import ucitaj_akcije

def meni_administrator():

    while True:
        print('\n1.Prikaz knjiga')
        print('2.Pretraga knjiga')
        print('3.Prikaz akcija')
        print('4.Pretraga akcija')
        print('5.Dodavanje nove knjige')
        print('6.Izmena knjige')
        print('7.Registracija korisnika')
        print('8.Prikaz korisnike')
        print('9.Kraj.')

        stavka = unos.validacija_unosa_broj("Izaberite stavku: ")

        if stavka == 1:
            prikazi_knjige()

        elif stavka == 2:
            pretrazi_knjige()

        elif stavka == 3:
            prikaz_tabele_akcija(ucitaj_akcije())

        elif stavka == 4:
            pretrazi_akcije()


        elif stavka == 5:
            dodaj_knjigu()

        elif stavka == 6:
            izmena_knjige()

        elif stavka == 7:
            registracija()

        elif stavka == 8:
            prikazi_korisnike()

        elif stavka == 9:
            return
        else:
            print("Pokusajte ponovo!")




def meni_prodavac(prodavac):

    while True:
        print('\n1.Prodaja knjiga')
        print('2.Prikaz knjiga')
        print('3.Pretraga knjiga')
        print('4.Prikaz akcija')
        print('5.Pretraga akcija')
        print('6.Dodavanje nove knjige')
        print('7.Izmena knjige')
        print('8.Logicko brisanje knjige')
        print('9. Kraj')

        stavka = unos.validacija_unosa_broj("Izaberite stavku: ")

        if stavka == 1:
            prodaja_knjiga(prodavac)

        elif stavka == 2:
            prikazi_knjige()

        elif stavka == 3:
            pretrazi_knjige()

        elif stavka == 4:
            prikaz_tabele_akcija(ucitaj_akcije())

        elif stavka == 5:
            pretrazi_akcije()

        elif stavka == 6:
            dodaj_knjigu()

        elif stavka == 7:
            izmena_knjige()

        elif stavka == 8:
            pass

        elif stavka == 9:
            return
        else:
            print("Pokusajte ponovo!")



def meni_menadzer():

    while True:
        print('\n1.Prikaz knjiga')
        print('2.Pretraga knjiga')
        print('3.Prikaz akcija')
        print('4.Pretraga akcija')
        print('5.Registracija korisnika')
        print('6.Prikaz korisnika')
        print('7.Dodavanje nove akcije')
        print('8. Kreiranje izvestaja')
        print('9. Kraj')

        stavka = unos.validacija_unosa_broj("Izaberite stavku: ")

        if stavka == 1:
            prikazi_knjige()

        elif stavka == 2:
            pretrazi_knjige()

        elif stavka == 3:
            prikaz_tabele_akcija(ucitaj_akcije())

        elif stavka == 4:
            pretrazi_akcije()

        elif stavka == 5:
            registracija()

        elif stavka == 6:
            prikazi_korisnike()

        elif stavka == 7:
            kreiraj_akciju()

        elif stavka == 8:
            pass
        
        elif stavka == 9:
            return
        else:
            print("Pokusajte ponovo!")




def main():

    ulogovani_korisnik = prijava()

    if ulogovani_korisnik is not None:
        if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
            meni_administrator()
        elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
            meni_prodavac(ulogovani_korisnik)

        elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
            meni_menadzer()
        else:
            print("Korisnik ima nepoznatu ulogu!")
    else:
        print("Tri puta pogresan unos!")


main()