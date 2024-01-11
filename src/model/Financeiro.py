class Financeiro:
    def __init__(self, entrada, saida, descricao, ):
        self._entrada = entrada
        self._saida = saida
        self._descricao = descricao

        def get_entrada(self):
            return self._entrada

        def set_entrada(self, nova_entrada):
            self._entrada = nova_entrada

        def get_saida(self):
            return self._saida

        def set_saida(self, nova_saida):
            self._saida = nova_saida

        def get_descricao(self):
            return self._descricao

        def set_descricao(self, nova_descricao):
            self._descricao = nova_descricao