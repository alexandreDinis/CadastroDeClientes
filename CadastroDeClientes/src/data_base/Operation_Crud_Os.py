import sqlite3
from prettytable import PrettyTable
from src.data_base.Connect_DB import Connect_DB

class Operations_Crud_OS:

    def __init__(self):
        path = "data_base/cadastro_clientes.db"
        self.receiver = Connect_DB(path)

    def insert_db(self, tipo, cliente_id, km_inicial, km_final, financeiro, hora_inicial, hora_final, status_id, data):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('''
                INSERT INTO "os" VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (tipo, cliente_id, km_inicial, km_final, financeiro, hora_inicial, hora_final, status_id, data))
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
                cursor.execute(f'SELECT * FROM os WHERE {column} = ?', (search,))
                result = cursor.fetchall()
                if result:
                    table = PrettyTable()
                    table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro",
                                         "Hora Inicial", "Hora Final", "Status ID", "Data"]

                    for row in result:
                        table.add_row(row)

                    print("\nOS found:")
                    print(table)
                    print("-" * 160)
                else:
                    print('OS not found')
                    return -1

            if opc == '-1':
                cursor.execute('SELECT * FROM os')
                result = cursor.fetchall()
                if result:
                    table = PrettyTable()
                    table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro",
                                         "Hora Inicial", "Hora Final", "Status ID", "Data"]

                    for row in result:
                        table.add_row(row)

                    print("\nOS found:")
                    print(table)
                    print("-" * 160)
                    return result
                else:
                    print('OS not found')

        except sqlite3.Error as e:
            print('Error in search', e)
        finally:
            self.receiver.close_connection()

    def update(self, tipo, cliente_id, km_inicial, km_final, financeiro, hora_inicial, hora_final, status_id, id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            set_values = ""
            values = []

            validation = self.search_db(-1, 'id', id, )

            if validation != -1:

                if tipo is not None and tipo.strip() != "":
                    set_values += "tipo=?, "
                    values.append(tipo)
                else:
                    cursor.execute(f'SELECT tipo FROM os WHERE id = ?', (id,))
                    set_values += "tipo=?, "
                    tipo = cursor.fetchone()[0]
                    values.append(tipo)

                # Adicione o mesmo bloco de código para as outras colunas

                if set_values:
                    set_values = set_values.rstrip(', ')

                query = f'UPDATE os SET {set_values} WHERE id = ?'
                values.append(id)
                cursor.execute(query, tuple(values))

                connection.commit()

                print('Database update successfully\n')
                print()
                self.search_db(-1, 'id', id)

        except sqlite3.Error as e:
            print('Error when update', e)
        finally:
            self.receiver.close_connection()

    def delete_db(self, id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM os WHERE id = ?", (id,))
            connection.commit()
            print('Delete data successfully')
        except sqlite3.Error as e:
            print(f'Error Delete ', {e})
        finally:
            self.receiver.close_connection()

# Exemplo de uso:
# ops_os = Operations_Crud_OS()
# ops_os.insert_db('Manutenção', 1, 100, 200, 150.0, '08:00', '10:00', 1, '2024-01-01')
# ops_os.search_db(-1, '', '')
# ops_os.update('Reparo', 2, 300, 400, 200.0, '14:00', '16:00', 2, 1)
# ops_os.delete_db(1)