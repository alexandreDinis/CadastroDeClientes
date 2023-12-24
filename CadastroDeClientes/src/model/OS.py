from datetime import datetime
from Clientes import Clientes

class OS:
    def __init__(self, clientes, tipo, km_inicial, km_final, financeiro):
        self._tipo = tipo
        self._km_inicial = km_inicial
        self._km_final = km_final
        self._Financeiro = financeiro
        self._data = datetime.now().date()
        self._Clientes = clientes

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, novo_tipo):
        self._tipo = novo_tipo

    def get_km_inicial(self):
        return self._km_inicial

    def set_km_inicial(self, novo_km_inicial):
        self._km_inicial = novo_km_inicial

    def get_km_final(self):
        return self._km_final

    def set_km_final(self, novo_km_final):
        self._km_final = novo_km_final

    def get_financeiro(self):
        return self._Financeiro

    def set_financeiro(self, novo_financeiro):
        self._Financeiro = novo_financeiro

    def get_clientes(self):
        return self._Clientes

    def set_clientes(self, novos_clientes):
        self._Clientes = novos_clientes

