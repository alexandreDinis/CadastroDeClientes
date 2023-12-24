from data_base import Operations_Crud_Clientes
from model import Clientes
from src.data_base import Connect_DB



class Main:
    def __init__(self):

        clientes = Clientes.Clientes
        data_base = Operations_Crud_Clientes.Operations_Crud_Clientes()

        def cadastrar():

            while True:
                nome = str(input('Nome Fantasia: '))
                contato = str(input('Contato: '))
                rua = str(input('Rua: '))
                bairro = str(input('Bairro: '))
                cidade = str(input('Cidade: '))
                phone = str(input('Phone: '))
                setor = str(input('Setor: '))
                relevancia = str(input('Relevancia [ S = Strong) | M = Medium | W = Weak ]: ')).upper().strip()
                while relevancia != 'S' or relevancia != 'M' or relevancia != 'W':
                    if relevancia == 'S':
                        relevancia = 'Strong'
                    elif relevancia == 'M':
                        relevancia = 'Medium'
                    elif relevancia == 'W':
                        relevancia = 'Weak'
                    else:
                        print('Opção Invalida')
                status = str(input('Status [ I = Inativo) | A = Ativo ]: ')).upper().strip()
                while status != 'I' or status != 'A':
                    if status == 'I':
                        status = 'Inativo'
                    elif status == 'A':
                        status = 'Ativo'
                    else:
                        print('Opção Invalida')
                data = clientes.get_data
                clientes(nome, contato, rua, bairro, cidade, phone, setor, relevancia, status,)
                data_base.insert_db(clientes.get_nome, clientes.get_contato, clientes.get_rua, clientes.get_bairro,
                      clientes.get_cidade, clientes.get_phone, clientes.get_setor, clientes.get_relevancia, data, )

                op = int(input('Novo Cadastro [1 = Sim | 0 = Nao ]'))
                if op == 0:
                    break

        if __name__ == "__main__":
            cadastrar()