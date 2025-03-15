import time

class MasinaService:
    def __init__(self, masina_repo):
        self.__masina_repo = masina_repo

    def find_by_token(self, token, eficient_ineficient):
        try:
            masina = None
            if eficient_ineficient == 1:
                masina = self.__masina_repo.find_by_token_binary(token)
            else:
                masina = self.__masina_repo.find_by_token_secvential(token)
            return masina
        except ValueError as e:
            raise ValueError(f"Cannot find client: {e}")

    def get_all(self):
        return self.__masina_repo.lista_masini

    def print_masini(self):
        for masina in self.__masina_repo.lista_masini:
            print(masina)

    def __comparator_token_masina(self, a, b):
        return a > b

    def __comparator_masini(self, a, b, criteriu):
        if criteriu == "tokenMasina":
            return a.tokenMasina > b.tokenMasina
        if criteriu == "marca model":
            return a.marca > b.marca or (a.marca == b.marca and a.model == b.model)
        if criteriu == "marca model tokenMasina":
            return a.marca > b.marca or (a.marca == b.marca and a.model > b.model or (a.model == b.model and a.tokenMasina == b.tokenMasina))
        return a.getProfit() > b.getProfit()

    def sort_masini(self, criteriu):
        start_time = time.time()
        lista_masini = self.__masina_repo.lista_masini
        for i in range(len(lista_masini) - 1):
            for j in range(i + 1, len(lista_masini)):
                if self.__comparator_masini(lista_masini[i], lista_masini[j], criteriu):
                    aux = lista_masini[i]
                    lista_masini[i] = lista_masini[j]
                    lista_masini[j] = aux
        end_time = time.time()
        return lista_masini, end_time - start_time