

class InMemoryRepository:
    def __init__(self):
        self.listaMasini = {}

    def find_by_token(self, token):
        if id in self.listaMasini.keys():
            return self.listaMasini[token]
        return None

    def save(self, masina):
        self.listaMasini[masina.tokenMasina] = masina

    def find_all(self):
        return list(self.listaMasini.values())



