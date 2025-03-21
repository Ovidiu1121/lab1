import time

class MasinaService:
    def __init__(self, masina_repo):
        self.__masina_repo = masina_repo

    def find_by_token(self, token, eficient_ineficient):
        try:
            masina = None
            start_time = time.time()
            if eficient_ineficient == 1:
                masina = self.__masina_repo.find_by_token_binary(token)
            else:
                masina = self.__masina_repo.find_by_token_secvential(token)
            end_time = time.time()
            return masina, end_time - start_time
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

    def __bubble_sort(self, criteriu):
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

    def __sort_quicksort(self, criteriu):
        start_time = time.time()
        lista_masini = self.__masina_repo.lista_masini[:]

        def quicksort(lista, low, high):
            if low < high:
                pivot = lista[high]
                i = low - 1

                for j in range(low, high):
                    if not self.__comparator_masini(lista[j], pivot, criteriu):
                        i += 1
                        lista[i], lista[j] = lista[j], lista[i]

                lista[i + 1], lista[high] = lista[high], lista[i + 1]
                pi = i + 1

                quicksort(lista, low, pi - 1)
                quicksort(lista, pi + 1, high)

        quicksort(lista_masini, 0, len(lista_masini) - 1)

        end_time = time.time()
        return lista_masini, end_time - start_time

    def sort_masini(self,criteriu,eficient_ineficient):
        if eficient_ineficient == 1:
            return self.__bubble_sort(criteriu)
        else:
            return self.__sort_quicksort(criteriu)
