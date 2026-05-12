class Tallennus:

    def __init__(self, tiedosto):
        self.tiedosto = tiedosto

    def tallenna_tulos(self, tulos):
        with open(self.tiedosto, "a") as f:
            f.write(tulos + "\n")

    def hae_tulokset(self):
        try:
            with open(self.tiedosto, "r") as f:
                return f.read().splitlines()
        except FileNotFoundError:
            return []
