from src.data_base.Operation_Crud_Viagem import Operations_Crud_Viagem
from src.controler import controler_carros
from datetime import datetime

vg = Operations_Crud_Viagem()
car = controler_carros


def menu_geral():
    menu = int(input("""
Logistica
[1] Abastecimento
[2] Viagem
[3] Carros
[0] Voltar
"""))
    return menu


def menu_abastecimento():
    menu = int(input("""
Abastecimento
[1] Cadastrar
[2] Relatorio
[0] Voltar    
"""))
    return menu


def menu_viagem():
    menu = int(input("""
Viagem
[1] Cadastrar
[2] Relatorio
[0] Voltar    
"""))
    return menu


def insert_abastecimento():
    car.listar_carros_geral('-1', '', '')
    carro_id = int(input('Carro ID '))
    data = datetime.now().date()
    km = int(input('Digite o KM '))
    valor = float(input('Valor abatecido '))
    valor_comb = float(input('Valor do combustivel '))
    car.update_km(carro_id, km)
    vg.insert_db_abastecimento(data, km, valor, valor_comb)


def insert_viagem():
    data = datetime.now().date()
    km = int(input('Digite o KM '))
    vg.insert_db_viagem(data, km)


def search_viagem():
    print('Relatorio de Km')
    ano = str(input('Ano '))
    mes = str(input('Mes '))
    resul = vg.get_total_value_viagem(ano, mes)
    if ano is not None and mes is None:
        print(f'Voce rodou {resul} km no ano {ano}')
    elif ano is not None and mes is not None:
        print(f'Voce rodou {resul} km no mes {mes} do ano {ano}')
    else:
        data = datetime.now().date()
        search_data = vg.get_days_since_first_record(data)
        print(f'Voce rodou {resul} desde o primerio registro em {search_data} dias')


def search_abastecimento():
    ano = str(input('Ano '))
    mes = str(input('Mes '))
    dia = str(input('Dia '))
    vg.search_abastecimento(ano, mes, dia)


def start_viagem():
    while True:
        op = menu_geral()
        if op == 1:
            while True:
                op = menu_abastecimento()
                if op == 1:
                    insert_abastecimento()
                elif op == 2:
                    search_abastecimento()
                elif op == 0:
                    break
                else:
                    print('Opição Invalida')
        elif op == 2:
            while True:
                op = menu_viagem()
                if op == 1:
                    insert_viagem()
                elif op == 2:
                    search_viagem()
                elif op == 0:
                    break
                else:
                    print('Opição Invalida')
        elif op == 3:
            car.start_carro()
        elif op == 0:
            break
        else:
            print('Opição Invalida')



