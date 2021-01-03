from knjige.knjigeIO import ucitaj_knjige


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
        cena = input("Unesite cenu: ")
        knjige = pretrazi_knjige_brojevi('cena', cena)


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

def prikazi_knjige():
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