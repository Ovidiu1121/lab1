

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

    def sort_token_masina(self):
        lista_masini = self.__masina_repo.lista_masini
        for i in range(len(lista_masini) - 1):
            for j in range(i + 1, len(lista_masini)):
                if self.__comparator_token_masina(lista_masini[i].token_masina, lista_masini[j].token_masina):
                    aux = lista_masini[i]
                    lista_masini[i] = lista_masini[j]
                    lista_masini[j] = aux
        return lista_masini