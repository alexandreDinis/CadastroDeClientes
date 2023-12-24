from datetime import datetime

class viagem:

    def __init__(self,km_inicial, km_final, preço_combustivel):
        self._km_inicial = km_inicial
        self._km_final = km_final
        self._preço_combustivel = preço_combustivel
        self._data = datetime.now().date()

    def get_km_inicial(self):
        return self._km_inicial

    def set_km_inicial(self, novo_km_inicial):
        self._km_inicial = novo_km_inicial

    def get_km_final(self):
        return self._km_final

    def set_km_final(self, novo_km_final):
        self._km_final = novo_km_final

    def get_preço_combustivel(self):
        return self._preço_combustivel

    def set_preço_combustivel(self, novo_preço_combustivel):
        self._preço_combustivel = novo_preço_combustivel
