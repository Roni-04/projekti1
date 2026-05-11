import random

class Sanakirjasto:

    def __init__(self, tiedosto):
        self.tiedosto = tiedosto

    def hae_satunnainen_sana(self):
        with open(self.tiedosto, "r") as f:
            sanat = f.read().splitlines()

        return random.choice(sanat)