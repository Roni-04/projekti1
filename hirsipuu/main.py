from hirsipuu.sanat import Sanakirjasto
from hirsipuu.peli import HirsipuuPeli
from hirsipuu.tallennus import Tallennus

sanat = Sanakirjasto("sanat.txt")
sana = sanat.hae_satunnainen_sana()

peli = HirsipuuPeli(sana)

tilastot = Tallennus("tilastot.txt")

print("=== HIRSIPUU ===")

while not peli.voitto() and not peli.havio():

    print("\nSana:", " ".join(peli.arvattu))
    print("Yrityksiä:", peli.yritykset)

    kirjain = input("Arvaa kirjain: ").lower()

    tulos = peli.arvaa(kirjain)

    print(tulos)

if peli.voitto():
    print("\nVoitit! Sana oli:", sana)
    tilastot.tallenna_tulos("Voitto")
else:
    print("\nHävisit! Sana oli:", sana)
    tilastot.tallenna_tulos("Häviö")

print("\nAiemmat tulokset:")

for rivi in tilastot.hae_tulokset():
    print("-", rivi)
