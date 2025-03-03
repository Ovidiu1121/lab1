from repository.filerepository import MasinaFileRepository
from service.masinaservice import MasinaService
from ui.console import AppConsole


def main():
    masina_repository = MasinaFileRepository("data/masini.txt")
    masina_service = MasinaService(masina_repository)

    app_console = AppConsole(masina_service)
    app_console.run_console()

main()