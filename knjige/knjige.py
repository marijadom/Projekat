from knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige
from pomocne import unos

def pretrazi_knjige_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige_brojevi(kljuc, donja_vrednost, gornja_vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []
    for knjiga in knjige:
        if donja_vrednost <= knjiga[kljuc] <= gornja_vrednost:
            filtrirane_knjige.append(knjiga)
    return filtrirane_knjige


def pretrazi_knjige():
    print("1.Pretrazi po naslovu")
    print("2.Pretrazi po kategoriji")
    print("3.Pretrazi po autoru")
    print("4.Pretrazi po izdavacu")
    print("5.Pretrazi po ceni")

    stavka = int(input("Izaberite stavku: "))
    knjige = []
    if stavka == 1:
        naslov = input("Unesite naslov: ")
        knjige = pretrazi_knjige_string('naslov', naslov)

    elif stavka == 2:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretrazi_knjige_string('kategorija', kategorija)

    elif stavka == 3:
        autor = input("Unesite autora: ")
        knjige = pretrazi_knjige_string('autor', autor)
    elif stavka == 4:
        izdavac = input("Unesite izdavaca: ")
        knjige = pretrazi_knjige_string('izdavac', izdavac)
    elif stavka == 5:
        donja_granica_cene = unos.validacija_unosa_broj("Unesi donju granicu cene: ")
        gornja_granica_cene = unos.validacija_unosa_broj("Unesi gornju granicu cene: ")
        knjige = pretrazi_knjige_brojevi('cena', donja_granica_cene, gornja_granica_cene)

    for knjiga in knjige:
        print(knjiga)


def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp

    return knjige


def prikaz_tabele_knjiga():
    knjige = ucitaj_knjige()
    zaglavlje = f"{'sifra':<7}{'naslov':<35}{'autor':<30}{'isbn':<35}{'izdavac':<20}{'broj strana':<13}{'godina':<8}{'cena':<9}{'kategorija':<20}"

    print(zaglavlje)
    print('-'*len(zaglavlje))

    for knjiga in knjige:
        ispis = f"{knjiga['sifra']:<7}{knjiga['naslov']:<35}{knjiga['autor']:<30}{knjiga['isbn']:<35}{knjiga['izdavac']:<20}{knjiga['broj strana']:<13}{knjiga['godina']:<8}{knjiga['cena']:<9}{knjiga['kategorija']:<20}"
        print(ispis)

    print('-'*len(zaglavlje))


def prikazi_knjige():
    prikaz_tabele_knjiga()
    print("1.Sortiraj po naslovu")
    print("2.Sortiraj po kategoriji")
    print("3.Sortiraj po autoru")
    print("4.Sortiraj po izdavacu")
    print("5.Sortiraj po ceni")

    stavka = int(input("Izaberite stavku: "))

    knjige = []
    if stavka == 1:
        knjige = sortiraj_knjige("naslov")
    elif stavka == 2:
        knjige = sortiraj_knjige("kategorija")
    elif stavka == 3:
        knjige = sortiraj_knjige("autor")
    elif stavka == 4:
        knjige = sortiraj_knjige("izdavac")
    elif stavka == 5:
        knjige = sortiraj_knjige("cena")

    for knjiga in knjige:
        print(knjiga)


def dodaj_knjigu():
    sifra = int(unos.validacija_unosa_broj("Unesite sifru: "))

    postojece_knjige = ucitaj_knjige()
    for knjiga in postojece_knjige:
        if knjiga['sifra'] == sifra:
            print("Knjiga sa unetom sifrom vec postoji!")
            return None

    naslov = unos.validacija_unosa_string("Unesite naslov: ")
    autor = unos.validacija_unosa_string("Unesite autora: ")
    isbn = int(unos.validacija_unosa_broj("Unesite isbn: "))
    izdavac = unos.validacija_unosa_string("Unesite izdavaca: ")
    broj_strana = int(unos.validacija_unosa_broj("Unesite broj strana knjige: "))
    godina = int(unos.validacija_unosa_broj("Unesite godinu izdanja: "))
    cena = unos.validacija_unosa_broj("Unesite cenu: ")
    kategorija = unos.validacija_unosa_string("Unesite kategoriju: ")

    nova_knjiga = {
        "sifra": sifra,
        "naslov": naslov,
        "autor": autor,
        "isbn": isbn,
        "izdavac": izdavac,
        "broj strana": broj_strana,
        "godina": godina,
        "cena": cena,
        "kategorija": kategorija
    }
    print(nova_knjiga)

    postojece_knjige.append(nova_knjiga)

    sacuvaj_knjige(postojece_knjige)
    print("Uspesno ste dodali knjigu!")

def izmena_knjige():
    sifra = int(unos.validacija_unosa_broj("Unesite sifru: "))
    postojece_knjige = ucitaj_knjige()
    pronadjena = False
    for knjiga in postojece_knjige:
        if knjiga['sifra'] == sifra:
            pronadjena = True

            naslov = input("Unesite naslov: ")
            if naslov != "":
                knjiga['naslov'] = naslov

            autor = input("Unesite autora: ")
            if autor != "":
                knjiga['autor'] = autor

            isbn = input("Unesite isbn: ")
            if isbn != "":
                knjiga['isbn'] = int(isbn)

            izdavac = input("Unesite izdavaca: ")
            if izdavac != "":
                knjiga['izdavac'] = izdavac

            broj_strana = input("Unesite broj strana knjige: ")
            if broj_strana != "":
                knjiga['broj strana'] = int(broj_strana)

            godina = input("Unesite godinu izdanja: ")
            if godina != "":
                knjiga['godina'] = int(godina)

            cena = input("Unesite cenu: ")
            if cena != "":
                knjiga['cena'] = float(cena)

            kategorija = input("Unesite kategoriju: ")
            if kategorija != "":
                knjiga['kategorija'] = kategorija

            break

    if pronadjena:
        sacuvaj_knjige(postojece_knjige)
        print("Uspesno ste napravili izmenu!")



