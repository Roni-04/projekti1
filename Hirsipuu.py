import random

# Sanat joista arvotaan
sanat = [

]

sana = random.choice(sanat)
arvattu = ["_"] * len(sana)

yritykset = 15
arvatut_kirjaimet = []

print("=== HIRSIPUU ===")

while yritykset > 0 and "_" in arvattu:
    print("\nSana:", " ".join(arvattu))
    print("Arvatut kirjaimet:", " ".join(arvatut_kirjaimet))
    print("Yrityksiä jäljellä:", yritykset)

    kirjain = input("Arvaa kirjain: ").lower()

    # Tarkistetaan syöte
    if len(kirjain) != 1 or not kirjain.isalpha():
        print("Anna yksi kirjain!")
        continue

    if kirjain in arvatut_kirjaimet:
        print("Olet arvannut tämän jo.")
        continue

    arvatut_kirjaimet.append(kirjain)

    if kirjain in sana:
        print("Oikein!")
        for i in range(len(sana)):
            if sana[i] == kirjain:
                arvattu[i] = kirjain
    else:
        print("Väärä arvaus.")
        yritykset -= 1

# Pelin loppu
if "_" not in arvattu:
    print("\nVoitit! Sana oli:", sana)
else:
    print("\nHävisit! Sana oli:", sana)