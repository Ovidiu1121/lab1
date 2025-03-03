from dataclasses import dataclass


class Masina:
    def __init__(self, model:str, marca: str, tokenMasina: str, pretAchizitie: int, pretVanzare: int):
        self.__model = model
        self.__marca = marca
        self.__tokenMasina = tokenMasina
        self.__pretAchizitie = pretAchizitie
        self.__pretVanzare = pretVanzare

    @property
    def marca(self):
        return self.__marca

    @property
    def model(self):
        return self.__model

    @property
    def tokenMasina(self):
        return self.__tokenMasina

    @property
    def pretAchizitie(self):
        return self.__pretAchizitie

    @property
    def pretVanzare(self):
        return self.__pretVanzare

    def __str__(self):
        return self.marca + " " + self.model + " " + self.tokenMasina + f" {self.pretAchizitie} {self.pretVanzare}\n"