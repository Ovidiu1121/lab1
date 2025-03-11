from model.masinaentity import Masina

class MasinaFileRepository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__lista_masini = []
        self.__load_data()

    @property
    def lista_masini(self):
        return self.__lista_masini

    def __load_data(self):
        try:
            with open(self.__file_name) as f:
                for line in f:
                    array = line.split(" ")
                    try:
                        masina = Masina(str(array[0]), str(array[1]), str(array[2]), int(array[3]), int(array[4]))
                        self.lista_masini.append(masina)
                    except ValueError as e:
                        print(f"Skipping invalid line: {line}. Error: {e}")
        except FileNotFoundError:
            print(f"File {self.__file_name} not found.")

    def save(self, masina):
        try:
            with open(self.__file_name, "a") as f:
                f.write("\n" + str(masina.model) + " " + str(masina.marca) + " " + str(masina.tokenMasina)+ " " + str(masina)+
                        " " + str(masina.marca) + " " + str(masina.pretAchizitie)+" "+str(masina.pretVanzare))
        except Exception as e:
            print(f"Error saving client {masina.tokenMasina}: {e}")

    def find_by_token_secvential(self, token):
        sol = None
        for masina in self.lista_masini:
            if masina.tokenMasina == token:
                sol = masina
        if sol is None:
            raise ValueError("Token not found")
        return sol

    def find_by_token_binary(self, token):
        low = 0
        high = len(self.lista_masini) - 1

        while low <= high:
            mid = (low + high) // 2
            current_token = self.lista_masini[mid].tokenMasina

            if current_token == token:
                return self.lista_masini[mid]
            elif current_token < token:
                low = mid + 1
            else:
                high = mid - 1

        raise ValueError("Token not found")