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
       lista_placas = carro.obter_lista_placas()
       p = str(input('Placa ')).upper().strip()
       if p not in lista_placas:
           placa = p
           break
       else:
            print('Numero de Placa Invalido')
    ano = str(input('Ano ')).upper().strip()
    km_inicial = int(input('Km_inicial '))
    manutencao = int(input('Manutenção '))
    autonomia = int(input('Autonomia '))
    data = datetime.now().date()
    contador = 0
    carro.insert_db(marca, modelo, placa, ano, km_inicial, manutencao, autonomia, data, contador)


def update_km(carro_id, km_rodado):
    carro.update_km(carro_id, km_rodado)
    carro.update_contador(carro_id, km_rodado)
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
    elif op == 1:
        carro.search('-1', '', '')
    else:
        print('Opção Invalida')


def listar_carros_geral(opc, column, search):
    carro.search(opc, column, search)



