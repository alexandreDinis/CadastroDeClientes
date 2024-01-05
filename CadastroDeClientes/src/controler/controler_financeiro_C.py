from src.data_base.Operation_Crud_Financeiro_C import Operations_Crud_Financeiro_C
from src.data_base.Operations_Crud_Clientes import Operations_Crud_Clientes
from datetime import datetime
from colorama import Fore, Style
import calendar




def menu_op_financeiro():
    menu = int(input("""
Financeiro
[1] Empresa
[2] Pessoal
[0] Voltar
"""))
    return menu


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


def menu_relatorios_financiro():
    print('=-' * 30)

    menu = int(input(
        '''Digite a Opção Desejada :

[1] Relatorios de entradas  
[2] Relatorios Comparativo 
[3] Geral mes
[0] voltar
'''))
    while True:
        fn = Operations_Crud_Financeiro_C()

        if menu == 1:
            ano = str(input('Digite o Ano '))
            mes = str(input('Digite o Mes '))
            cliente = str(input('Digite o Cliente'))
            fn.relatorio_financeiro(ano, mes, cliente)
            break
        elif menu == 2:
            comparador()
            break
        elif menu == 3:
            entrada_saida_geral()
            break
        elif menu == 0:
            break
        else:
            print('Opção Invalida')

    print('=-' * 30)
    return menu


def enter_insert():
    cl = Operations_Crud_Clientes()
    fn = Operations_Crud_Financeiro_C()
    opc = '1'
    column = 'status'
    status = 'ATIVO'
    cl.search_db(opc, column, status)
    id_cliente = int(input('Digite o ID do Cliente '))
    valor = float(input('Valor da entrada = R$ '))
    data = str(datetime.now().date())
    fn.insert_db_entrada(id_cliente, valor, data)


def saida_insert():
    fn = Operations_Crud_Financeiro_C()
    valor = float(input('Valor da entrada = R$ '))
    data = str(datetime.now().date())
    fn.insert_db_saida(valor, data)


def comparador():
    cl = Operations_Crud_Clientes()
    fn = Operations_Crud_Financeiro_C()
    opc = '1'
    column = 'status'
    status = 'ATIVO'
    cl.search_db(opc, column, status)
    cliente = str(input('Digite o Cliente que deseja comparar '))
    ano_a = str(input('Digite o Ano _A '))
    mes_a = str(input('Digite o Mes _A '))
    valor_a = fn.relatorio_financeiro(ano_a, mes_a, cliente)
    ano_b = str(input('Digite o Ano _B '))
    mes_b = str(input('Digite o Mes _B '))
    valor_b = fn.relatorio_financeiro(ano_b, mes_b, cliente)
    diferença = float(valor_a - valor_b)
    perc = int(valor_a - valor_b) / valor_a * 100
    print(f' Data {mes_a}/{ano_a} Valor R$ {valor_a:.2f}')
    print(f' Data {mes_b}/{ano_b} Valor R$ {valor_b:.2f}')
    print(f'diferença R$ {diferença:.2f} % {perc}')


def entrada_saida_geral():
    fn = Operations_Crud_Financeiro_C()
    ano = str(input('Digite o Ano '))
    valores_entrada = []
    valores_saida = []

    for i in range(1, 13):
        mes_formatado = f'{i:02}'
        valores_entrada.append(fn.get_valor_por_ano_mes_entrada(ano, mes_formatado))
        valores_saida.append(fn.get_valor_por_ano_mes_saida(ano, mes_formatado))

    total_entrada = sum(valores_entrada)
    total_saida = sum(valores_saida)

    # Mapeamento de números de meses para nomes por extenso abreviados
    meses_abreviados = [calendar.month_abbr[i] for i in range(1, 13)]

    print(f'\n{"-" * 75}')
    print(f'{"Ano":^10} | {"Mês":^10} | {"Entrada":^10} | {"Saída":^10} | {"Diferença":^10} | {"Porcentagem":^10} |')
    print(f'{"-" * 75}')

    for i in range(len(valores_entrada)):
        mes = meses_abreviados[i]
        diferenca = valores_entrada[i] - valores_saida[i]
        porcentagem = ((valores_entrada[i] - valores_saida[i]) / valores_entrada[i]) * 100 if valores_entrada[
                                                                                                  i] != 0 else 0

        # Definindo cores com base na diferença
        cor_diferenca = Fore.BLUE if diferenca > 0 else Fore.RED

        print(
            f'{ano:^10} | {mes:^10} | {valores_entrada[i]:^10.2f} | {valores_saida[i]:^10.2f} | '
            f'{cor_diferenca}{diferenca:^10.2f}{Style.RESET_ALL} | {porcentagem:^10.2f}% |'
        )

    print(f'{"-" * 75}')
    print(
        f'{ano:^10} |  Total     | {total_entrada:^10.2f} | {total_saida:^10.2f} | '
        f'{Fore.BLUE if total_entrada - total_saida > 0 else Fore.RED}{total_entrada - total_saida:^10.2f}{Style.RESET_ALL} | '
        f'{((total_entrada - total_saida) / total_entrada) * 100:^10.2f}% |'
    )
    print(f'{"-" * 75}')


def comparar_entradas_saidas_anos(ano1, ano2):
    fn = Operations_Crud_Financeiro_C()
    valores_entrada_ano1 = []
    valores_saida_ano1 = []
    valores_entrada_ano2 = []
    valores_saida_ano2 = []

    for i in range(1, 13):
        mes_formatado = f'{i:02}'
        valores_entrada_ano1.append(fn.get_valor_por_ano_mes_entrada(ano1, mes_formatado))
        valores_saida_ano1.append(fn.get_valor_por_ano_mes_saida(ano1, mes_formatado))
        valores_entrada_ano2.append(fn.get_valor_por_ano_mes_entrada(ano2, mes_formatado))
        valores_saida_ano2.append(fn.get_valor_por_ano_mes_saida(ano2, mes_formatado))

    total_entrada_ano1 = sum(valores_entrada_ano1)
    total_saida_ano1 = sum(valores_saida_ano1)
    total_entrada_ano2 = sum(valores_entrada_ano2)
    total_saida_ano2 = sum(valores_saida_ano2)

    # Mapeamento de números de meses para nomes por extenso abreviados
    meses_abreviados = [calendar.month_abbr[i] for i in range(1, 13)]

    print(f'\n{"-"*105}')
    print(f'{"Ano":^10} | {"Mês":^10} | {"Entrada 1":^15} | {"Saída 1":^15} | {"Entrada 2":^15} | {"Saída 2":^15} | {"Diferença":^15} | {"Porcentagem":^15} |')
    print(f'{"-"*105}')

    for i in range(len(valores_entrada_ano1)):
        mes = meses_abreviados[i]
        diferenca_entrada = valores_entrada_ano1[i] - valores_entrada_ano2[i]
        diferenca_saida = valores_saida_ano1[i] - valores_saida_ano2[i]
        diferenca_total = diferenca_entrada - diferenca_saida
        porcentagem = (diferenca_total / diferenca_entrada) * 100 if diferenca_entrada != 0 else 0

        # Definindo cores com base na diferença total
        cor_diferenca_total = Fore.BLUE if diferenca_total > 0 else Fore.RED

        print(
            f'{ano1:^10} | {mes:^10} | {valores_entrada_ano1[i]:^15.2f} | {valores_saida_ano1[i]:^15.2f} | '
            f'{valores_entrada_ano2[i]:^15.2f} | {valores_saida_ano2[i]:^15.2f} | '
            f'{cor_diferenca_total}{diferenca_total:^15.2f}{Style.RESET_ALL} | {porcentagem:^15.2f}% |'
        )

    print(f'{"-"*105}')
    print(
        f'{ano1:^10} |  Total     | {total_entrada_ano1:^15.2f} | {total_saida_ano1:^15.2f} | '
        f'{total_entrada_ano2:^15.2f} | {total_saida_ano2:^15.2f} | '
        f'{Fore.BLUE if diferenca_total > 0 else Fore.RED}{diferenca_total:^15.2f}{Style.RESET_ALL} | '
        f'{((total_entrada_ano1 - total_saida_ano1) - (total_entrada_ano2 - total_saida_ano2)) / (total_entrada_ano1 - total_saida_ano1) * 100:^15.2f}% |'
    )
    print(f'{"-"*105}')


def start_financerio_C():
    while True:
        op = menu_financeiro_geral()
        if op == 1:
            enter_insert()
        elif op == 2:
            saida_insert()
        elif op == 3:
            menu_relatorios_financiro()
        elif op == 0:
            break
        else:
            print('Opção Invalida')
