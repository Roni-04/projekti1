class Hirsipuu:

    def __init__(self, sana):
        self.sana = sana
        self.arvattu = ["_"] * len(sana)
        self.yritykset = 15
        self.arvatut = []

    def arvaa(self, kirjain):

        if kirjain in self.arvatut:
            return "Kirjain arvattu jo"

        self.arvatut.append(kirjain)

        if kirjain in self.sana:

            for i in range(len(self.sana)):
                if self.sana[i] == kirjain:
                    self.arvattu[i] = kirjain

            return "Oikein"

        else:
            self.yritykset -= 1
            return "Väärin"

    def voitto(self):
        return "_" not in self.arvattu

    def havio(self):
        return self.yritykset <= 0
