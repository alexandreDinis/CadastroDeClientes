from prettytable import PrettyTable
import sqlite3
from src.data_base.Connect_DB import Connect_DB


class Operation_Crud_Carro:

    def __init__(self):
        path = "data_base/cadastro_clientes.db"
        self.receiver = Connect_DB(path)

    def id_carros_exists(self, id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('SELECT 1 FROM "carros" WHERE id = ?', (id,))
            return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print('Error checking if id_cliente exists:', e)
            return False
        finally:
            self.receiver.close_connection()

    def obter_lista_placas(self):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('SELECT placa FROM "carros"')
            result = cursor.fetchall()
            return [placa[0] for placa in result]  # Extrai as placas da lista de tuplas
        except sqlite3.Error as e:
            print('Error retrieving list of plates:', e)
            return []
        finally:
            self.receiver.close_connection()

    def insert_db(self, marca, modelo, placa, ano, km, manutencao, autonomia, data, contador):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO "carros"  VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (marca, modelo, placa,
                                                                                           ano, km,
                                                                                           manutencao, autonomia,
                                                                                           data, contador))
            connection.commit()
            print('\nInsert successfully\n')
        except sqlite3.Error as e:
            print('Insert not successfully', e)
        finally:
            self.receiver.close_connection()

    def search(self, opc, column, search):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            if opc != '-1':
                cursor.execute(f'SELECT * FROM carros WHERE {column} = ?', (search,))
                result = cursor.fetchall()
                if result:
                    table = PrettyTable()
                    table.field_names = ["ID", "Marca", "Modelo", "Palca", "Ano", "Km", "manutencao", "Autonomia",
                                         "Data"]

                    for row in result:
                        table.add_row(row)

                    print("\nContacts found:")
                    print(table)
                    print("-" * 160)
                else:
                    print('Contact not found')
                    return -1

            if opc == '-1':
                cursor.execute('SELECT * FROM carros')
                result = cursor.fetchall()
                if result:
                    table = PrettyTable()
                    table.field_names = ["ID", "Marca", "Modelo", "Palca", "Ano", "Km_", "manutencao", "Autonomia",
                                         "Data"]

                    for row in result:
                        table.add_row(row)

                    print("\nContacts found:")
                    print(table)
                    print("-" * 160)
                    return result
                else:
                    print('Contact not found')

        except sqlite3.Error as e:
            print('Error in search', e)
        finally:
            self.receiver.close_connection()

    def delete(self, id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM carros WHERE id = ?", (id,))
            connection.commit()
            print('Delete data successfully')
        except sqlite3.Error as e:
            print(f'Error Delete ', {e})
        finally:
            self.receiver.close_connection()

    def buscar_km(self, id):
        connection = self.receiver.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT carros FROM km WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        connection.close()

        # Verifique se o resultado foi encontrado
        if resultado:
            return resultado[0]
        else:
            return None

    def buscar_manutencao(self, id):
        connection = self.receiver.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT carros FROM manutencao WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        connection.close()

        # Verifique se o resultado foi encontrado
        if resultado:
            return resultado[0]
        else:
            return None

    def buscar_contador(self, id):
        connection = self.receiver.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT carros FROM contador WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        connection.close()

        # Verifique se o resultado foi encontrado
        if resultado:
            return resultado[0]
        else:
            return None

    def update_km(self, id_carro, km):

        global connection
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            # Atualizar a coluna manutencao somando o valor de km
            cursor.execute('UPDATE carros SET km = km + ? WHERE id = ?', (km, id_carro))

            # Confirmar a transação
            connection.commit()

        except sqlite3.Error as e:
            print('Erro ao fazer manutencao:', e)

        finally:
            connection.close()

    def update_manutencao(self, id_carro, km):

        global connection
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            # Atualizar a coluna manutencao somando o valor de km
            cursor.execute('UPDATE carros SET manutencao = manutencao + ? WHERE id = ?', (km, id_carro))

            # Confirmar a transação
            connection.commit()

        except sqlite3.Error as e:
            print('Erro ao fazer manutencao:', e)

        finally:
            connection.close()


    def update_contador(self, id_carro, km):

        global connection
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            # Atualizar a coluna manutencao somando o valor de km
            cursor.execute('UPDATE carros SET contador_km = contador_km + ? WHERE id = ?', (km, id_carro))

            # Confirmar a transação
            connection.commit()

        except sqlite3.Error as e:
            print('Erro ao fazer manutencao:', e)

        finally:
            connection.close()

    def zerar_contador_km(self, id_carro):
        global connection
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            # Zerar o contador_km para um registro específico na tabela carros
            cursor.execute('UPDATE carros SET contador_km = 0 WHERE id = ?', (id_carro,))

            # Confirmar a transação
            connection.commit()

        except sqlite3.Error as e:
            print(f'Erro ao zerar o contador_km para o ID {id_carro}:', e)

        finally:
            connection.close()

    def get_car_id_by_plate(self, plate):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('SELECT id FROM "carros" WHERE placa = ?', (plate,))
            result = cursor.fetchone()
            if result:
                return result[0]  # Return the first column (ID)
            else:
                return None  # Return None if the plate is not found
        except sqlite3.Error as e:
            print('Error getting car ID by plate:', e)
            return None
        finally:
            self.receiver.close_connection()
