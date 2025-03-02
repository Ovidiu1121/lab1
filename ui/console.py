

class AppConsole:
    def __init__(self, masina_service):
        self.__masina_service = masina_service

    def __afiseaza_masini(self):
        print("cevaa")
        print(*self.__masina_service.get_all(), sep="\n")

    def run_console(self):
        self.__afiseaza_masini()

