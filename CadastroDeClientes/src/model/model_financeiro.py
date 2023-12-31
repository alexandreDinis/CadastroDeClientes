from src.data_base.Operation_Crud_Financeiro import Operations_Crud_Financeiro
from src.data_base.Operations_Crud_Clientes import Operations_Crud_Clientes
from datetime import datetime
def menu_financeiro_geral():

    print('=-' * 30)

    menu = int(input(
    '''Digite a Opção Desejada :

[1] Entrada   
[2] Saidas 
[3] Relatorios
[0] Voltar   
'''))
    print('=-' * 30)
    return menu

def menu_cadastro_financeiro():
    print('=-' * 30)
    while True:
        menu = menu_financeiro_geral()
        if menu == 1:
            pass
        elif menu == 2:
            # def saida
            pass
        elif menu == 3:
            # relatorios
            pass
        elif menu == 0:
            break
        else:
            print('Opção Invalida')


        print('=-' * 30)

def enter_insert():
    cl = Operations_Crud_Clientes()
    fn = Operations_Crud_Financeiro()
    opc = '1'
    column = 'status'
    status = str('ATIVO')
    cl.search_db(opc, column, status)
    id_cliente = int(input('Digite o ID do Cliente '))
    valor = float(input('Valor da entrada = R$ '))
    data = str(datetime.now().date())
    fn.inserir_entrada(id_cliente, valor, data)
