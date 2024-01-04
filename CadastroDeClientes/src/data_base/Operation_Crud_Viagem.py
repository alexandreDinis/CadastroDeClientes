import sqlite3
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
            cursor.execute(f'INSERT INTO "viagens"  VALUES(NULL, ?, ?, ?, ?)', (data, km, valor, valor_comb,))
            connection.commit()
            print('\nInsert successfully\n')
        except sqlite3.Error as e:
            print('Insert not successfully', e)
        finally:
            self.receiver.close_connection()

    def search_db(self, opc, column, search):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            if opc != '-1':
                cursor.execute(f'SELECT * FROM viagens WHERE {column} = ?', (search,))
                result = cursor.fetchall()
                if result:
                    table = PrettyTable()
                    table.field_names = ["ID", "data", "Km", "Valor", "Valor_comb",]

                    for row in result:
                        table.add_row(row)

                    print("\nContacts found:")
                    print(table)
                    print("-" * 50)
                else:
                    print('Contact not found')
                    return -1

            if opc == '-1':
                cursor.execute('SELECT * FROM viagens')
                result = cursor.fetchall()
                if result:
                    table = PrettyTable()
                    table.field_names = ["ID", "data", "Km", "Valor", "Valor_comb",]

                    for row in result:
                        table.add_row(row)

                    print("\nContacts found:")
                    print(table)
                    print("-" * 50)
                    return result
                else:
                    print('Contact not found')

        except sqlite3.Error as e:
            print('Error in search', e)
        finally:
            self.receiver.close_connection()
