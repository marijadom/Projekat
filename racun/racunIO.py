import json

datoteka = './datoteke/racuni.json'

def sacuvaj_racune(racuni):
    with open(datoteka, "w") as f:
        json.dump(racuni, f, indent=2)

def ucitaj_racune():
    with open(datoteka, "r") as f:
        return json.load(f)