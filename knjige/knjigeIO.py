import json

datoteka = './datoteke/knjige.json'

def sacuvaj_knjige(knjige):
    with open(datoteka, "w") as f:
        json.dump(knjige, f, indent=2)

def ucitaj_knjige():
    with open(datoteka, "r") as f:
        return json.load(f)