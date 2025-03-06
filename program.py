import random


gyakorlatok = {
    "kar": ["bicepsz hajlítás", "tricepsz nyújtás", "karhúzás", "fekvőtámasz"],
    "láb": ["guggolás", "felhúzás", "kitörés", "lábnyújtás"],
    "has": ["plank", "felülés", "lábemelés", "biciklizés"],
    "mell": ["fekvőtámasz", "pados fekvenyomás", "karnyújtás", "csigás tárogatás"]
}

def valasz_kap():
    edzes_tipus = input("Milyen típusú edzést szeretnél? (kar, láb, has, mell): ").lower()
    intenzitas = input("Milyen intenzitású edzést szeretnél? (alacsony, közepes, magas): ").lower()
    return edzes_tipus, intenzitas

def edzes_program(edzes_tipus, intenzitas):
    if edzes_tipus not in gyakorlatok:
        print("Érvénytelen testrész.")
        return

    gyakorlat_lista = gyakorlatok[edzes_tipus]
    szam = 10 if intenzitas == "magas" else 7 if intenzitas == "kozepes" else 5
    edzes = random.sample(gyakorlat_lista, szam)

    print("Az Ön edzésprogramja ({edzes_tipus}) - {intenzitas} intenzitás:")
    for gyakorlat in edzes:
        print(f"- {gyakorlat}")
    print("Ne felejts el bemelegíteni és nyújtani a végén!")

def main():
    edzes_tipus, intenzitas = valasz_kap()
    edzes_program(edzes_tipus, intenzitas)

if __name__ == "__main__":
    main()
