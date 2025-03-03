import os

class AppConsole:
    def __init__(self, masina_service):
        self.__masina_service = masina_service
        self.__options = [{"name": "AFISARE masini",
                           "func": self.__afiseaza_masini},
                          {"name" : "SEARCH tokenMasina",
                           "func" : self.__search_token_masina},
                          {"name" : "SORT marca model",
                           "func" : self.__sort_marca_model},
                          {"name" : "SORT marca model tokenMasina",
                           "func" : self.__sort_marca_model_token_masina},
                          {"name" : "SORT profit",
                           "func" : self.__sort_profit}]

    def __afiseaza_masini(self, eficient_ineficient):
        self.__masina_service.print_masini()

    def __search_token_masina(self, eficient_ineficient):
        token = input("Token: ")
        masina = self.__masina_service.find_by_token(token, eficient_ineficient)
        print(masina)

    def __sort_marca_model(self, eficient_ineficient):
        pass

    def __sort_marca_model_token_masina(self, eficient_ineficient):
        pass

    def __sort_profit(self, eficient_ineficient):
        pass

    def __afisare_meniu(self):
        for index, elem in enumerate(self.__options):
            print(f"{index + 1}. {elem['name']}")

    def __waitForX(self):
        while True:
            print("x. Exit")
            option = input('option: ')
            if option.lower() == 'x':
                os.system("clear")
                break

    def __choose_eficient_ineficient(self):
        option = input("1. Eficient\n2. Ineficient\n")
        if option != '1' and option != '2':
            raise ValueError("Invalid option")
        return int(option)


    def run_console(self):
        while True:
            try:
                self.__afisare_meniu()
                print("x. Exit")
                option = input("option: ")

                if option.lower() == 'x':
                    break

                option = int(option)
                if option > len(self.__options):
                    raise ValueError("Invalid option")

                print()
                eficient_ineficient = self.__choose_eficient_ineficient()
                self.__options[option - 1]["func"](eficient_ineficient)
                self.__waitForX()

            except ValueError as e:
                print(e)

            except Exception as e:
                print(e)