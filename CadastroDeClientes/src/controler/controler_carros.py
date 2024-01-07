from datetime import datetime
from src.data_base.Operation_Crud_Carro import Operation_Crud_Carro

carro = Operation_Crud_Carro()


def menu_geral():
    menu = int(input("""
Carros
[1] Cadastrar
[2] Relatorios
[3] Deletar
[0] Voltar    
"""))
    return menu


def menu_relatorio():
    menu = int(input("""
Relatorios
[1] Placa
[2] Lista de carros
"""))
    return menu


def start_carro():
    while True:
        op = menu_geral()

        if op == 1:
            insert()
        elif op == 2:
            search()
        elif op == 3:
            delite()
        elif op == 0:
            break
        else:
            print('Opção Invalida')


def insert():
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


def update_km(carro_id, km_rodado):
    carro.update_km(carro_id, km_rodado)
    carro.update_manutencao(carro_id, km_rodado)
    contador = carro.buscar_contador(carro_id)
    manutencao = carro.buscar_manutencao(carro_id)
    tempo_manutencao = manutencao - contador
    if contador >= manutencao - 500:
        print(f'Alerta de manutenção')
        print(f'Você tem  {tempo_manutencao} Km')
        if tempo_manutencao < 0:
            op = str(input('Voce ja passou do prazo para a manutenção! Voce ja fez ? [S/N]')).upper().strip()
            if op == 'S':
                carro.zerar_contador_km(carro_id)


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

def search():
    op = menu_relatorio()
    if op == 2:
        placa = str(input('Digite a Placa ')).upper().strip()
        carro.search('1', 'placa', placa)
        op = str(input('Mais detalhes [S/N] ')).upper().strip()
        if op == 'S':
            carro_id = carro.get_car_id_by_plate(placa)
            contador = carro.buscar_contador(carro_id)
            manutencao = carro.buscar_manutencao(carro_id)
            tempo_manutencao = manutencao - contador
            if contador >= manutencao - 500:
                print(f'Alerta de manutenção')
                print(f'Você tem  {tempo_manutencao} Km')
                if tempo_manutencao < 0:
                    op = str(input('Voce ja passou do prazo para a manutenção! Voce ja fez ? [S/N]')).upper().strip()
                    if op == 'S':
                        carro.zerar_contador_km(carro_id)
    else:
        carro.search('-1', '', '')

