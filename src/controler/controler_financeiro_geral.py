import calendar as cal
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from colorama import Fore, Style
from prettytable import PrettyTable

from src.data_base.Operation_Crud_Financeiro_C import Operations_Crud_Financeiro_C
from src.data_base.Operation_Crud__Financeiro_P import Operations_Crud_Financeiro_P
from src.data_base.Operations_Crud_Clientes import Operations_Crud_Clientes
from src.controler import controler_financeiro_C, controler_financeiro_P

cl = Operations_Crud_Clientes()
emp = Operations_Crud_Financeiro_C()
pes = Operations_Crud_Financeiro_P()
con_emp = controler_financeiro_C
con_pes = controler_financeiro_P


def menu_op_financeiro():
    menu = int(input("""
Financeiro
[1] Empresa
[2] Pessoal
[3] Relatorios
[0] Voltar
"""))
    return menu


def menu_relatorio():
    menu = int(input("""
Relatorio
[1] Anual entrada/saida
[2] Comparador de Anos
[0] Voltar
"""))
    return menu


def start_relatorio():
    while True:
        op = menu_relatorio()
        if op == 1:
            entrada_saida_geral()
        elif op == 2:
            comparar_entradas_saidas_anos()
        elif op == 0:
            break
        else:
            print('Opçao Invalida')


def start():
    while True:
        op = menu_op_financeiro()
        if op == 1:
            con_emp.start()
        elif op == 2:
            con_pes.start()
        elif op == 3:
            start_relatorio()
        elif op == 0:
            break
        else:
            print('Opção Invalida')


def saida_insert():
    valor = float(input('Valor da entrada = R$ '))
    data = str(datetime.now().date())
    emp.insert_db_saida(valor, data)


# repensar essa funçao
def comparador():
    opc = '1'
    column = 'status'
    status = 'ATIVO'
    cl.search_db(opc, column, status)
    cliente = str(input('Digite o Cliente que deseja comparar '))
    ano_a = str(input('Digite o Ano _A '))
    mes_a = str(input('Digite o Mes _A '))
    valor_a = emp.relatorio_financeiro(ano_a, mes_a, cliente)
    ano_b = str(input('Digite o Ano _B '))
    mes_b = str(input('Digite o Mes _B '))
    valor_b = emp.relatorio_financeiro(ano_b, mes_b, cliente)
    diferenca = float(valor_a - valor_b)
    perc = int(valor_a - valor_b) / valor_a * 100
    print(f' Data {mes_a}/{ano_a} Valor R$ {valor_a:.2f}')
    print(f' Data {mes_b}/{ano_b} Valor R$ {valor_b:.2f}')
    print(f'diferenca R$ {diferenca:.2f} % {perc}')


def entrada_saida_geral():
    ano_entrada = str(input('Digite o Ano '))
    valores_entrada = []
    valores_saida = []

    for i in range(1, 13):
        mes_formatado = f'{i:02}'
        valores_entrada.append(emp.get_valor_por_ano_mes_entrada(ano_entrada, mes_formatado))
        valores_saida.append(emp.get_valor_por_ano_mes_saida(ano_entrada, mes_formatado))

    total_entrada = sum(valores_entrada)
    total_saida = sum(valores_saida)

    # Mapeamento de números de meses para nomes por extenso abreviados
    meses_abreviados = [cal.month_abbr[i] for i in range(1, 13)]

    # Exibir a tabela usando PrettyTable
    table = PrettyTable()
    table.field_names = ["Mês", "Entrada", "Saída", "Diferença", "Porcentagem"]

    for i in range(len(valores_entrada)):
        mes = meses_abreviados[i]
        diferenca = valores_entrada[i] - valores_saida[i]

        if total_entrada != 0:
            porcentagem = ((valores_entrada[i] - valores_saida[i]) / total_entrada) * 100
        else:
            porcentagem = 0

        # Definindo cores com base na diferença
        cor_diferenca = Fore.BLUE if diferenca > 0 else Fore.RED

        table.add_row([mes, f'{valores_entrada[i]:.2f}', f'{valores_saida[i]:.2f}', f'{cor_diferenca}{diferenca:.2f}{Style.RESET_ALL}', f'{porcentagem:.2f}%'])

    print(table)

    # Exibir os gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Gráfico de barras para Entradas e Saídas
    labels = meses_abreviados
    x = np.arange(len(labels))
    width = 0.35

    rects1 = ax1.bar(x - width/2, valores_entrada, width, label='Entrada')
    rects2 = ax1.bar(x + width/2, valores_saida, width, label='Saída')

    ax1.set_ylabel('Valores')
    ax1.set_title('Entradas e Saídas por Mês')
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.legend()

    # Gráfico de barras para Diferença Total
    ax2.bar(0, total_entrada - total_saida, color='blue' if total_entrada - total_saida > 0 else 'red')
    ax2.set_ylabel('Diferença Total')
    ax2.set_title('Diferença Total')
    ax2.set_xticks([])

    # Exibir os gráficos
    plt.show()


def comparar_entradas_saidas_anos():
    ano1 = str(input("Digite o Primeiro Ano "))
    ano2 = str(input("Digite o Segundo Ano "))
    valores_entrada_ano1 = []
    valores_saida_ano1 = []
    valores_entrada_ano2 = []
    valores_saida_ano2 = []

    for i in range(1, 13):
        mes_formatado = f'{i:02}'
        valores_entrada_ano1.append(emp.get_valor_por_ano_mes_entrada(ano1, mes_formatado))
        valores_saida_ano1.append(emp.get_valor_por_ano_mes_saida(ano1, mes_formatado))
        valores_entrada_ano2.append(emp.get_valor_por_ano_mes_entrada(ano2, mes_formatado))
        valores_saida_ano2.append(emp.get_valor_por_ano_mes_saida(ano2, mes_formatado))

    total_entrada_ano1 = sum(valores_entrada_ano1)
    total_saida_ano1 = sum(valores_saida_ano1)
    total_entrada_ano2 = sum(valores_entrada_ano2)
    total_saida_ano2 = sum(valores_saida_ano2)

    # Mapeamento de números de meses para nomes por extenso abreviados
    meses_abreviados = [cal.month_abbr[i] for i in range(1, 13)]
    linha = 121
    print(f'\n{"-" * linha}')
    print(
        f'{"Mês":^10} | {"Entrada 1":^15} | {"Saída 1":^15} | {"Entrada 2":^15} | {"Saída 2":^15} | {"Diferença":^15} | {"Porcentagem":^15} |')
    print(f'{"-" * linha}')

    for i in range(len(valores_entrada_ano1)):
        mes = meses_abreviados[i]
        diferenca_entrada = valores_entrada_ano1[i] - valores_entrada_ano2[i]
        diferenca_saida = valores_saida_ano1[i] - valores_saida_ano2[i]
        diferenca_total = diferenca_entrada - diferenca_saida

        if total_entrada_ano1 - total_saida_ano1 != 0:
            porcentagem = (diferenca_total / (total_entrada_ano1 - total_saida_ano1)) * 100
        else:
            porcentagem = 0

        # Definindo cores com base na diferença total
        cor_diferenca_total = Fore.BLUE if diferenca_total > 0 else Fore.RED

        print(
            f'{mes:^10} | {valores_entrada_ano1[i]:^15.2f} | {valores_saida_ano1[i]:^15.2f} | '
            f'{valores_entrada_ano2[i]:^15.2f} | {valores_saida_ano2[i]:^15.2f} | '
            f'{cor_diferenca_total}{diferenca_total:^15.2f}{Style.RESET_ALL} | {porcentagem:^15.2f}% |'
        )

    print(f'{"-" * linha}')
    print(
        f'{"Total":^10} | {total_entrada_ano1:^15.2f} | {total_saida_ano1:^15.2f} | '
        f'{total_entrada_ano2:^15.2f} | {total_saida_ano2:^15.2f} | '
        f'{Fore.BLUE if diferenca_total > 0 else Fore.RED}{diferenca_total:^15.2f}{Style.RESET_ALL} | '
        f'{porcentagem:^15.2f}% |'
    )
    print(f'{"-" * linha}')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Gráfico de barras para Entradas e Saídas
    labels = meses_abreviados
    x = np.arange(len(labels))
    width = 0.35

    rects1 = ax1.bar(x - width / 2, valores_entrada_ano1, width, label='Entrada 1')
    rects2 = ax1.bar(x + width / 2, valores_saida_ano1, width, label='Saída 1')
    rects3 = ax1.bar(x - width / 2, valores_entrada_ano2, width, label='Entrada 2')
    rects4 = ax1.bar(x + width / 2, valores_saida_ano2, width, label='Saída 2')

    ax1.set_ylabel('Valores')
    ax1.set_title('Entradas e Saídas por Mês')
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.legend()

    # Gráfico de barras para Diferença Total
    ax2.bar(0, diferenca_total, color='blue' if diferenca_total > 0 else 'red')
    ax2.set_ylabel('Diferença Total')
    ax2.set_title('Diferença Total')
    ax2.set_xticks([])

    # Exibir a tabela
    print(f'\n{"-" * 80}')
    # ... (código para exibir a tabela)
    print(f'{"-" * 80}')

    # Exibir os gráficos
    plt.show()
