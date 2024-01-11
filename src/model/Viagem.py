from datetime import datetime


class Viagem:
    def __init__(self, km_inicial, km_final, preco_combustivel):
        self._km_inicial = km_inicial
        self._km_final = km_final
        self._preco_combustivel = preco_combustivel
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
        return self._preco_combustivel

    def set_preco_combustivel(self, novo_preco_combustivel):
        self._preco_combustivel = novo_preco_combustivel

    def caululo_viagem(self, inicial, final, autonomia, valor_comb):
        result = float((final - inicial) / autonomia * valor_comb)
        return round(result, 2)
