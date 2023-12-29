from src.model import Clientes
from src.data_base.Operations_Crud_Clientes import Operations_Crud_Clientes
from src.data_base import Connect_DB

path = 'cadastro_clientes.db'


from datetime import datetime

clientes = Clientes.Clientes

data = ''
def cadastrar():
    data_base = Operations_Crud_Clientes
    global data
    while True:
        nome = str(input('Nome Fantasia: '))
        contato = str(input('Contato: '))
        rua = str(input('Rua: '))
        bairro = str(input('Bairro: '))
        cidade = str(input('Cidade: '))
        phone = str(input('Phone: '))
        setor = str(input('Setor: '))
        r = str(input('Relevancia [ S = Strong) | M = Medium | W = Weak ]: ')).upper().strip()
        relevancia = ''
        while r not in 'S''M''W':
            if r == 'S':
                relevancia = 'Strong'
            elif r == 'M':
                relevancia = 'Medium'
            elif r == 'W':
                relevancia = 'Weak'
            else:
                print('Opção Invalida')
            r = str(input('Relevancia [ S = Strong) | M = Medium | W = Weak ]: ')).upper().strip()

        s = str(input('Status [ I = Inativo) | A = Ativo ]: ')).upper().strip()
        status = ''
        while s not in 'I' 'A':
            if s == 'I':
                status = 'Inativo'
            elif s == 'A':
                status = 'Ativo'
            else:
                print('Opção Invalida')
            s = str(input('Status [ I = Inativo) | A = Ativo ]: ')).upper().strip()

        clientes(nome, contato, rua, bairro, cidade, phone, setor, relevancia, status, data)
        data = str(input('data'))

        data_base.insert( nome, contato, rua, bairro, cidade, phone, setor, relevancia, status, data)
        op = int(input('Novo Cadastro [1 = Sim | 0 = Nao ]'))
        if op == 0:
            break


if __name__ == "__main__":
    cadastrar()
