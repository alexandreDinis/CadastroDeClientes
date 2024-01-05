from datetime import datetime

from src.data_base.Operation_Crud_Carro import Operation_Crud_Carro

carro = Operation_Crud_Carro()


def menu_geral():
    menu = int(input("""
carros

[1] Cadastrar
[2] Pesquisar
[3] Deletar
[0] Voltar    
"""))
    return menu


def start_carro():
    while True:
        op = menu_geral()

        if op == 1:
            cadastrar()
        elif op == 2:
            pass # relatorios de carros
        elif op == 3:
            delite()


def cadastrar():
    marca = str(input('Marca ')).upper().strip()
    modelo = str(input('Modelo ')).upper().strip()
    while True:
        p = str(input('Placa ')).upper().strip()
        verifica = carro.id_placa_exists(p)
        if len(p) == 7 and verifica is None:
            placa = p
            break
        elif verifica is not None:
            print('Placa ja cadastrada')
        else:
            print('Numero de Placa Invalido')
    ano = str(input('Ano ')).upper().strip()
    km_inicial = str(input('Km_inicial ')).upper().strip()
    km_atual = str(input('Km_atual ')).upper().strip()
    autonomia = str(input('Autonomia ')).upper().strip()
    data = datetime.now().date()
    carro.insert_db(marca, modelo, placa, ano, km_inicial, km_atual, autonomia, data)


def update_km(id, km_rodado):
    carro.update_km(id, km_rodado)
    carro.update_manutencao(id, km_rodado)
    contador = carro.buscar_contador(id)
    manutencao = carro.buscar_manutencao(id)
    tempo_manutencao = manutencao - contador
    if contador >= manutencao - 500:
        print(f'Alerta de manutenção')
        print(f'Você tem  {tempo_manutencao} Km')
        if tempo_manutencao < 0:
            op = str(input('Voce ja passou do prazo para a manutenção, se voce ja a fez [S/N]')).upper().strip()
            if op == 'S':
                carro.zerar_contador_km(id)


def delite():
    while True:
        carro.search('-1', '', '')
        id = str(input('Digite o ID do carro '))
        verifica = carro.id_carros_exists(id)
        if verifica is not None:
            carro.search('1', 'id', id)
            op = str(input('Tem certeza que deseja deletar [S/N] ')).upper().strip()
            if op == 'S':
                carro.delete(id)
                break
            else:
                break

