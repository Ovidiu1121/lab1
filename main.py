import traceback

from repository.filerepository import MasinaFileRepository
from service.masinaservice import MasinaService
from ui.console import AppConsole


def main():
    print("hello")

    masina_repository = MasinaFileRepository("data/masini")
    masina_service = MasinaService(masina_repository)

    app_console = AppConsole(masina_service)
    app_console.run_console()

    print("bye")


main()