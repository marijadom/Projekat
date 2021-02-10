from akcije.akcijeIO import ucitaj_akcije
import datetime
from pomocne.unos import validacija_unosa_broj, validacija_unosa_string

def prikaz_tabele_akcija(akcije):


    zaglavlje = f"{'sifra':<7}{'datum vazenja':<10}{'naslov':<35}{'autor':<35}{'kategorija':<15}{'nova cena':<7}"

    print(zaglavlje)
    print('-'*len(zaglavlje))

    for akcija in akcije:
        ispis = f"{akcija['sifra']:<7}{akcija['datum vazenja']:<10}"
        print(ispis)
        for knjiga in akcija['knjige'].keys():
            ispis = '\t\t\t\t\t' + f" {akcija['knjige'][knjiga]['naslov']:<35}{akcija['knjige'][knjiga]['autor']:<35}{akcija['knjige'][knjiga]['kategorija']:<15}{akcija['knjige'][knjiga]['nova cena']:<7}"
            print(ispis)

    print('\n1.Sortirati akcije po sifri.')
    print('2.Sortirati akcije po datumu.')
    stavka = validacija_unosa_broj("Izaberite tip sortiranja: ")

    if stavka == 1:
        sortiran_prikaz_tabele_akcija(sortiraj_akcije('sifra'))

    elif stavka == 2:
        sortiran_prikaz_tabele_akcija(sortiraj_akcije_po_datumu())

    print('-'*len(zaglavlje))

def sortiran_prikaz_tabele_akcija(akcije):

    zaglavlje = f"{'sifra':<5}  {'datum vazenja':<10}  {'naslov':<30}{'autor':<30}{'kategorija':<15}{'nova cena':<7}"

    print(zaglavlje)
    print('-'*len(zaglavlje))

    for akcija in akcije:
        ispis = f"{akcija['sifra']:<5}   {akcija['datum vazenja']:<10}"
        print(ispis)
        for knjiga in akcija['knjige'].keys():
            ispis = '\t\t\t\t\t' + f" {akcija['knjige'][knjiga]['naslov']:<30}{akcija['knjige'][knjiga]['autor']:<30}{akcija['knjige'][knjiga]['kategorija']:<15}{akcija['knjige'][knjiga]['nova cena']:<7}"
            print(ispis)

    print('-'*len(zaglavlje))

def sortiraj_akcije(kljuc):          #za sortiranje po sifri
    akcije = ucitaj_akcije()

    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i][kljuc] < akcije[j][kljuc]:
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

    return akcije

def sortiraj_akcije_po_datumu():
    akcije = ucitaj_akcije()

    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if datetime.datetime.strptime(akcije[i]['datum vazenja'], "%x") < datetime.datetime.strptime(akcije[j]['datum vazenja'], "%x"):
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

    return akcije



def pretrazi_knjige_string(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtrirane_akcije = []

    for akcija in akcije:
        pronadjena = False
        for knjiga in akcija['knjige'].keys():
            if vrednost.lower() in akcija['knjige'][knjiga][kljuc].lower():
                pronadjena = True
                break
        if pronadjena:
            filtrirane_akcije.append(akcija)

    return filtrirane_akcije


def pretrazi_knjige_brojevi(kljuc, vrednost):
    akcije = ucitaj_akcije()
    filtrirane_akcije = []

    for akcija in akcije:
        if vrednost == akcija[kljuc]:
            filtrirane_akcije.append(akcija)

    return filtrirane_akcije


def pretrazi_akcije():

    print("1. Pretrazi akcije po sifri.")
    print("2. Pretrazi akcije po naslovu knjige.")
    print("3. Pretrazi akcije po autoru knjige.")
    print("4. Pretrazi akcije po kategoriji knjige.")

    opcija = validacija_unosa_broj("Izaberite opciju: ")

    if opcija == 1:
        sifra = validacija_unosa_broj("Unesite sifru: ")
        sortiran_prikaz_tabele_akcija(pretrazi_knjige_brojevi('sifra', sifra))
    if opcija == 2:
        naslov = validacija_unosa_string("Unesite naslov: ")
        sortiran_prikaz_tabele_akcija(pretrazi_knjige_string('naslov', naslov))
    if opcija == 3:
        autor = validacija_unosa_string("Unesite autora: ")
        sortiran_prikaz_tabele_akcija(pretrazi_knjige_string('autor', autor))
    if opcija == 4:
        kategorija = validacija_unosa_string("Unesite kategoriju: ")
        sortiran_prikaz_tabele_akcija(pretrazi_knjige_string('kategorija', kategorija))

