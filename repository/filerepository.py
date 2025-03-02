from model.masinaentity import Masina
from repository.inmemoryrepository import InMemoryRepository


class MasinaFileRepository(InMemoryRepository):
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        try:
            with open(self.__file_name) as f:
                for line in f:
                    array = line.split(" ")
                    if len(array) != 3:
                        continue
                    try:
                        masina = Masina(str(array[0]), str(array[1]), str(array[2]), int(array[3]), int(array[4]))
                    except ValueError as e:
                        print(f"Skipping invalid line: {line}. Error: {e}")
        except FileNotFoundError:
            print(f"File {self.__file_name} not found.")
        except Exception as e:
            print(f"Unexpected error while loading data: {e}")

    def save(self, masina):
        try:
            with open(self.__file_name, "a") as f:
                f.write("\n" + str(masina.model) + " " + str(masina.marca) + " " + str(masina.tokenMasina)+ " " + str(masina)+
                        " " + str(masina.marca) + " " + str(masina.pretAchizitie)+" "+str(masina.pretVanzare))
        except Exception as e:
            print(f"Error saving client {masina.tokenMasina}: {e}")