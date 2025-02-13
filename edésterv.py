
def edzesterv_hozzaadas():
    tipus = int(input("Mi a mai edzés típusa? (pl. futás, súlyemelés): "))
    ido = int(input("Mennyi ideig tart az edzés (percekben)? "))
    return f"Edzés: {tipus}, Időtartam: {ido} perc"

def edzesterv_kiiras(edzesterv):
    if edzesterv:
        print("\nA mai edzésterv:")
        for edzes in edzesterv:
            print(edzes)
    else:
        print("Nincs mentett edzés.")

# Fő program
edzesterv = []
while True:
    print("\n1. Edzés hozzáadása")
    print("2. Edzésterv megjelenítése")
    print("3. Kilépés")
    valasz = input("Válassz egy lehetőséget: ")

    if valasz == "1":
        edzesterv.append(edzesterv_hozzaadas())
    elif valasz == "2":
        edzesterv_kiiras(edzesterv)
    elif valasz == "3":
        print("Kilépés...")
        break
    else:
        print("Érvénytelen választás, próbáld újra.")
