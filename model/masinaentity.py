from dataclasses import dataclass


@dataclass
class Masina:
    marca:str
    model:str
    tokenMasina:str
    pretAchizitie:int
    pretVanzare:int

    @property
    def marca(self):
        return self.marca

    @property
    def model(self):
        return self.model

    @property
    def tokenMasina(self):
        return self.tokenMasina

    @property
    def pretAchizitie(self):
        return self.pretAchizitie

    @property
    def pretVanzare(self):
        return self.pretVanzare

    def __str__(self):
        return self.marca + " " + self.model + " " + self.tokenMasina + f" {self.pretAchizitie} {self.pretVanzare}\n"