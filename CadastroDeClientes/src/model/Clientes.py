

class Clientes:

    def __init__(self, nome, contato, rua, bairro,  cidade, phone, setor, relevancia, status, data):
        self.__nome = nome
        self._contato = contato
        self._rua = rua
        self._bairro = bairro
        self._cidade = cidade
        self._phone = phone
        self._setor = setor
        self._relevancia = relevancia
        self._status = status
        self._data = data

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_contato(self):
        return self._contato

    def set_contato(self, contato):
        self._contato = contato

    def get_rua(self):
        return self._rua

    def set_rua(self, rua):
        self._rua = rua

    def get_bairro(self):
        return self._bairro

    def set_bairro(self, bairro):
        self._bairro = bairro

    def get_cidade(self):
        return self._cidade

    def set_cidade(self, cidade):
        self._cidade = cidade

    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        self._phone = phone

    def get_setor(self):
        return self._setor

    def set_setor(self, setor):
        self._setor = setor

    def get_relevancia(self):
        return self._relevancia

    def set_relevancia(self, relevancia):
        self._relevancia = relevancia

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_data(self):
        return self._data


