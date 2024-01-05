import sqlite3
from datetime import datetime

from prettytable import PrettyTable
from src.data_base.Connect_DB import Connect_DB


class Operations_Crud_Viagem:

    def __init__(self):
        path = "data_base/cadastro_clientes.db"
        self.receiver = Connect_DB(path)

    def insert_db_abastecimento(self, data, km, valor, valor_comb):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO "abastecimento"  VALUES(NULL, ?, ?, ?, ?)', (data, km, valor, valor_comb))
            connection.commit()
            print('\nInsert successfully\n')
        except sqlite3.Error as e:
            print('Insert not successfully', e)
        finally:
            self.receiver.close_connection()

    def search_abastecimento(self, year=None, month=None, day=None):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            # Construir a parte da cláusula WHERE baseada nos parâmetros fornecidos
            where_clause = " WHERE 1=1"
            if year:
                where_clause += f" AND strftime('%Y', data) = '{year}'"
            if month:
                where_clause += f" AND strftime('%m', data) = '{month}'"
            if day:
                where_clause += f" AND strftime('%d', data) = '{day}'"

            # Montar a consulta SQL final
            sql_query = f'SELECT id, data, km, valor_comb, valor_abastecido, total_km, total_valor, media, total_comb FROM abastecimento{where_clause}'

            cursor.execute(sql_query)
            result = cursor.fetchall()

            if result:
                table = PrettyTable()
                table.field_names = ["ID", "Data", "Km", "Valor Combustível", "Valor Abastecido", "Total Km",
                                     "Total Valor", "Média", "Total Combustível"]

                for row in result:
                    table.add_row(row)

                print("\nResults found:")
                print(table)
                print("-" * 80)
                return result
            else:
                print('Result not found')
                return -1

        except sqlite3.Error as e:
            print('Error in search', e)
        finally:
            self.receiver.close_connection()

    def insert_db_viagem(self, data, km):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO "viagem"  VALUES(NULL, ?, ?)', (data, km))
            connection.commit()
            print('\nInsert successfully\n')
        except sqlite3.Error as e:
            print('Insert not successfully', e)
        finally:
            self.receiver.close_connection()

    def get_total_value_viagem(self, year=None, month=None):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            # Construir a consulta SQL para obter o valor total
            sql_query = '''
                   SELECT COALESCE(SUM(valor_abastecido), 0) AS total_value
                   FROM abastecimento
               '''

            # Adicionar condições ao filtro por ano e/ou mês, se fornecidos
            if year:
                sql_query += f" WHERE strftime('%Y', data) = '{year}'"
                if month:
                    sql_query += f" AND strftime('%m', data) = '{month}'"

            cursor.execute(sql_query)
            result = cursor.fetchone()

            if result:
                total_value = result[0]
                if year and month:
                    print(f'Total value for {month}/{year}: {total_value}')
                elif year:
                    print(f'Total value for {year}: {total_value}')
                else:
                    print(f'Total value overall: {total_value}')
                return total_value
            else:
                print('No records found')
                return 0

        except sqlite3.Error as e:
            print('Error in get_total_value_by_year_month', e)
        finally:
            self.receiver.close_connection()

    def get_days_since_first_record(self, search_date):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            # Obter a data do primeiro registro na tabela
            cursor.execute('SELECT MIN(data) FROM abastecimento')
            first_record_date = cursor.fetchone()[0]

            if not first_record_date:
                print('No records found')
                return None

            # Converter as datas para objetos datetime
            first_record_date = datetime.strptime(first_record_date, '%Y-%m-%d')
            search_date = datetime.strptime(search_date, '%Y-%m-%d')

            # Calcular a diferença em dias
            days_difference = (search_date - first_record_date).days

            print(f'Days since the first record: {days_difference} days')
            return days_difference

        except sqlite3.Error as e:
            print('Error in get_days_since_first_record', e)
        finally:
            self.receiver.close_connection()