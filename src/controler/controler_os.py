from datetime import datetime

from prettytable import PrettyTable
from src.data_base.Operation_Crud_Financeiro_C import Operations_Crud_Financeiro_C
from src.data_base.Operation_Crud_OS import Operations_Crud_OS
from src.data_base.Operations_Crud_Clientes import Operations_Crud_Clientes
from src.controler import controler_estatisticas

est = controler_estatisticas
fc = Operations_Crud_Financeiro_C()
cl = Operations_Crud_Clientes()
db = Operations_Crud_OS()


def start():
    while True:
        op = menu_geral_os()
        if op == 1:
            abrir_os()
        elif op == 2:
            fechar_os()
        elif op == 3:
            filtrar_os_por_filtros_interativos()
        elif op == 0:
            break
        else:
            print('Opção Invalida')


def menu_geral_os():
    menu = int(input(""""
*** O.S ***
[1]Abrir 
[2]Fechar
[3]Relatorios
[0]Voltar
    """))
    return menu


def abrir_os():
    while True:
        db.imprimir_tabela_tipo_ordem()
        tipo_id = str(input('Tipo de O.S ')).strip().upper()
        descricao_tipo = db.get_descricao_by_id(tipo_id)

        if descricao_tipo is not None:
            tipo = descricao_tipo
            break
        else:
            print('Opção Inválida')

    if tipo == 'ATENDIMENTO':
        cl.search_db('1', 'status', 'ATIVO')
        cliente = str(input("ID Cliente ")).strip().upper()
    else:
        cliente = None
    km_inicial = None
    km_final = None
    financeiro = None
    status = cl.buscar_valor_status('4')
    data_inicial = datetime.now()
    data_final = None
    db.insert(tipo, cliente, km_inicial, km_final, financeiro, status, data_inicial, data_final)


def fechar_os():
    while True:
        verifica = db.search_db('1', 'status_id', 'ABERTO')
        if verifica == -1:
            print('Nao há O.S Abertas')
            break
        id = str(input('Digite o ID da O.S '))
        km_inicial = int(input("Km Inicial  "))
        km_final = int(input('Km Final '))
        financeiro = int(input('Valor R$ '))
        print('Digite a Hora, Minuto, Dia separado por espaço')
        dia = int(input('Dia '))
        hora = int(input('Hora '))
        minutos = int(input('Minutos '))
        data_final = data_hora_fechamento(hora, minutos, dia)
        fc.abrir_a_receber(id, financeiro,'ABERTO', data_final)
        db.update('\n', '\n', km_inicial, km_final, financeiro, 'FECHADO', '\n',
                  data_final, id)
        db.search_db('1', 'id', id)
        id_cliente = cl.search_db('-1', 'cliente_id', id)
        data_inicial = db.search_db('-1', 'data_inicial', id)
        hora_inicial = data_inicial.strftime("%H:%M:%S")
        hora_final = data_final.strftime("%H:%M:%S")
        est.estatisticas(id, id_cliente, financeiro, km_inicial, km_final, hora_inicial, hora_final, datetime.now())
        op = str(input('Novo Cadastro [S/N]')).upper().strip()
        if op == 'N':
            break
# id_os, id_cliente, valor, km_ini, km_fin, hora_ini, hora_fin, data

def data_hora_fechamento(hora, minuto, dia):
    # Obtém a data atual
    hoje = datetime.today()

    # Cria um objeto datetime com a data e hora do fechamento
    data_hora = datetime(hoje.year, hoje.month, dia, hora, minuto)

    return data_hora




def obter_filtros_interativos():
    filtros = {
        "ano": None,
        "mes": None,
        "status_id": None,
        "cliente": None
    }

    while True:
        print("\nFiltros atuais:")
        for chave, valor in filtros.items():
            print(f"{chave.capitalize()}: {valor or 'Nenhum'}")

        print("\nEscolha um número para adicionar/remover filtro:")
        print("1. Ano")
        print("2. Mês")
        print("3. Status")
        print("4. Cliente")
        print("5. Limpar filtros")
        print("0. Sair")

        opcao = input("\nOpção: ")

        if opcao == "1":
            chave = "ano"
        elif opcao == "2":
            chave = "mes"
        elif opcao == "3":
            print("\nEscolha o status:")
            print("1. ABERTO")
            print("2. FECHADO")
            opcao_status = input("\nOpção de Status: ")

            if opcao_status == "1":
                valor = "ABERTO"
            elif opcao_status == "2":
                valor = "FECHADO"
            else:
                print("Opção inválida. Tente novamente.")
                continue
            chave = "status_id"
        elif opcao == "4":
            chave = "cliente"
        elif opcao == "5":
            filtros = {chave: None for chave in filtros}
            print("Filtros limpos.")

            # Exibir tabela geral após limpar os filtros
            resultado = db.filtrar_os_por_parametros()
            if resultado:
                table = PrettyTable()
                table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro", "Status ID",
                                     "Data Inicial", "Data Final"]

                for row in resultado:
                    table.add_row(row)

                print("\nTabela Geral:")
                print(table)
                print("-" * 160)
            else:
                print('Nenhuma OS encontrada.')

            continue
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

        filtros[chave] = valor

        # Exibir tabela filtrada após cada filtro adicionado
        resultado = db.filtrar_os_por_parametros(**filtros)
        if resultado:
            table = PrettyTable()
            table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro", "Status ID",
                                 "Data Inicial", "Data Final"]

            for row in resultado:
                table.add_row(row)

            print("\nOS filtradas:")
            print(table)
            print("-" * 160)
        else:
            print('Nenhuma OS encontrada com os filtros especificados.')

    return filtros


def filtrar_os_por_filtros_interativos():
    # Mostrar a tabela geral antes de solicitar os filtros
    db.mostrar_tabela_geral_os()

    resultado = db.filtrar_os_por_parametros(**obter_filtros_interativos())

    if resultado:
        table = PrettyTable()
        table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro", "Status ID",
                             "Data Inicial", "Data Final"]

        for row in resultado:
            table.add_row(row)

        print("\nOS encontradas:")
        print(table)
        print("-" * 160)
    else:
        print('Nenhuma OS encontrada com os filtros especificados.')

