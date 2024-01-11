import sqlite3
from calendar import calendar
from datetime import datetime

from prettytable import PrettyTable
from termcolor import colored
from src.data_base.Connect_DB import Connect_DB


class Operations_Crud_Financeiro_P:

    def __init__(self):
        path = "data_base/cadastro_clientes.db"
        self.receiver = Connect_DB(path)

    def insert_despesa_fixa(self, data, valor, categoria_id, descricao):
        conn = self.receiver.connect()
        cursor = conn.cursor()

        insert_sql = '''
        INSERT INTO DespesasFixas (data, valor, categoria_id, descricao)
        VALUES (?, ?, ?, ?);
        '''

        cursor.execute(insert_sql, (data, valor, categoria_id, descricao))
        conn.commit()

        print(colored("Registro de despesa fixa inserido com sucesso!", "green"))

        self.receiver.close_connection()

    def insert_despesa_variavel(self, data, valor, categoria_id, descricao):
        conn = self.receiver.connect()
        cursor = conn.cursor()

        insert_sql = '''
        INSERT INTO DespesasVariaveis (data, valor, categoria_id, descricao)
        VALUES (?, ?, ?, ?);
        '''

        cursor.execute(insert_sql, (data, valor, categoria_id, descricao))
        conn.commit()

        print(colored("Registro de despesa variável inserido com sucesso!", "green"))

        self.receiver.close_connection()

    def insert_despesa_inesperada(self, data, valor, categoria_id, descricao):
        conn = self.receiver.connect()
        cursor = conn.cursor()

        insert_sql = '''
        INSERT INTO DespesasInesperadas (data, valor, categoria_id, descricao)
        VALUES (?, ?, ?, ?);
        '''

        cursor.execute(insert_sql, (data, valor, categoria_id, descricao))
        conn.commit()

        print(colored("Registro de despesa inesperada inserido com sucesso!", "green"))

        self.receiver.close_connection()

    def gerar_relatorio_mensal(self, mes, ano):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            # Função auxiliar para obter o total de uma categoria no mês
            def obter_total_categoria(tabela, categoria_id):
                cursor.execute(f'''
                       SELECT SUM(valor) 
                       FROM {tabela} 
                       WHERE strftime('%Y-%m', data) = ? 
                           AND categoria_id = ?;
                   ''', (f'{ano}-{mes:02d}', categoria_id))

                total = cursor.fetchone()[0]
                return total if total is not None else 0

            # Obter todas as categorias
            cursor.execute('SELECT * FROM Categoria')
            categorias = cursor.fetchall()

            # Inicializar tabela
            table = PrettyTable()
            table.field_names = ["Categoria", "Gastos Fixos", "Gastos Variáveis", "Gastos Inesperados", "Total no Mês"]

            for categoria in categorias:
                categoria_id, nome_categoria = categoria

                # Obter total de cada categoria nas despesas fixas, variáveis e inesperadas
                total_fixas = obter_total_categoria('DespesasFixas', categoria_id)
                total_variaveis = obter_total_categoria('DespesasVariaveis', categoria_id)
                total_inesperadas = obter_total_categoria('DespesasInesperadas', categoria_id)

                # Calcular o total de todas as categorias no mês
                total_mes = total_fixas + total_variaveis + total_inesperadas

                # Adicionar linha à tabela
                table.add_row([nome_categoria, total_fixas, total_variaveis, total_inesperadas, total_mes])

            print("\nRelatório Mensal:")
            print(table)
            print("-" * 120)

        except sqlite3.Error as e:
            print('Error in generating monthly report', e)
        finally:
            self.receiver.close_connection()

    def is_last_day_of_month(self, date):
        # Verifica se a data fornecida é válida
        try:
            datetime_obj = datetime.strptime(self, date, '%Y-%m-%d')
        except ValueError:
            print('Data inválida')
            return False

        # Obtém o último dia do mês para a data fornecida
        last_day = calendar.monthrange(datetime_obj.year, datetime_obj.month)[1]

        # Compara o dia da data fornecida com o último dia do mês
        return datetime_obj.day == last_day
