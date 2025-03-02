

class MasinaService:
    def __init__(self, masina_repo):
        self.masina_repo = masina_repo

    def find_by_token(self, token):
        try:
            return self.masina_repo.find_by_token(token)
        except ValueError as e:
            raise ValueError(f"Cannot find client: {e}")

    def get_all(self):
        return self.masina_repo.find_all()