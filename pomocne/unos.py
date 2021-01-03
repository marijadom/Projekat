

def validacija_unosa_string(poruka):
    unos = input(poruka)

    while unos == "":
        print("Ne moze se uneti prazan string!")
        unos = input(poruka)

    return unos


def validacija_unosa_broj(poruka):
    unos = input(poruka)

    while unos == "":

        print("Ne moze se uneti prazan string!")
        unos = input(poruka)

    return float(unos)
