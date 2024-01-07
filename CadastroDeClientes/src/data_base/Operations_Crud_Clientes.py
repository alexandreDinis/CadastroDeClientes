import sqlite3
from src.data_base.Connect_DB import Connect_DB
from prettytable import PrettyTable

class Operations_Crud_Clientes:

    def __init__(self):

        path = "data_base/cadastro_clientes.db"
        self.receiver = Connect_DB(path)

    def insert_db(self, nome, contato, rua, bairro, cidade, phone, setor, relevancia, status, data):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO "Clientes"  VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (nome, contato, rua,
                                                                                                   bairro, cidade,
                                                                                                   phone, setor,
                                                                                                   relevancia, status,
                                                                                                   data))
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
                cursor.execute(f'SELECT * FROM Clientes WHERE {column} = ?', (search,))
                result = cursor.fetchall()
                if result:
                    table = PrettyTable()
                    table.field_names = ["ID", "Nome", "Contato", "Rua", "Bairro", "Cidade", "Phone", "Setor",
                                         "Relevância", "Status", "Data"]

                    for row in result:
                        table.add_row(row)

                    print("\nContacts found:")
                    print(table)
                    print("-" * 160)
                else:
                    print('Contact not found')
                    return -1

            if opc == '-1':
                cursor.execute('SELECT * FROM Clientes')
                result = cursor.fetchall()
                if result:
                    table = PrettyTable()
                    table.field_names = ["ID", "Nome", "Contato", "Rua", "Bairro", "Cidade", "Phone", "Setor",
                                         "Relevância", "Status", "Data"]

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

    def update(self, nome, contato, rua, bairro, cidade, phone, setor, relevancia, status, id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            set_values = ""
            values = []

            validation = self.search_db(-1, 'id', id, )

            if validation != -1:

                if nome is not None and nome.strip() != "":
                    set_values += "nome=?, "
                    values.append(nome)
                else:
                    cursor.execute(f'SELECT nome FROM Clientes WHERE id = ?', (id,))
                    set_values += "nome=?, "
                    nome = cursor.fetchone()[0]
                    values.append(nome)

                if contato is not None and contato.strip() != "":
                    set_values += "contato = ?, "
                    values.append(contato)
                else:
                    cursor.execute(f'SELECT contato FROM Clientes WHERE id = ?', (id,))
                    set_values += "contato = ?, "
                    contato = cursor.fetchone()[0]
                    values.append(contato)

                if rua is not None and rua.strip() != "":
                    set_values += "rua = ?, "
                    values.append(rua)
                else:
                    cursor.execute(f'SELECT rua FROM Clientes WHERE id = ?', (id,))
                    set_values += "rua = ?, "
                    rua = cursor.fetchone()[0]
                    values.append(rua)

                if rua is not None and cidade.strip() != "":
                    set_values += "cidade = ?, "
                    values.append(rua)
                else:
                    cursor.execute(f'SELECT cidade FROM Clientes WHERE id = ?', (id,))
                    set_values += "cidade = ?, "
                    cidade = cursor.fetchone()[0]
                    values.append(cidade)

                if bairro is not None and bairro.strip() != "":
                    set_values += "bairro = ?, "
                    values.append(bairro)
                else:
                    cursor.execute(f'SELECT bairro FROM Clientes WHERE id = ?', (id,))
                    set_values += "bairro = ?, "
                    bairro = cursor.fetchone()[0]
                    values.append(bairro)

                if phone is not None and phone.strip() != "":
                    set_values += "phone = ?, "
                    values.append(phone)
                else:
                    cursor.execute(f'SELECT phone FROM Clientes WHERE id = ?', (id,))
                    set_values += "phone = ?, "
                    phone = cursor.fetchone()[0]
                    values.append(phone)

                if setor is not None and setor.strip() != "":
                    set_values += "setor = ?, "
                    values.append(setor)
                else:
                    cursor.execute(f'SELECT setor FROM Clientes WHERE id = ?', (id,))
                    set_values += "setor = ?, "
                    setor = cursor.fetchone()[0]
                    values.append(setor)

                if relevancia is not None and relevancia.strip() != "":
                    set_values += "relevancia = ?, "
                    values.append(relevancia)
                else:
                    cursor.execute(f'SELECT relevancia FROM Clientes WHERE id = ?', (id,))
                    set_values += "relevancia = ?, "
                    relevancia = cursor.fetchone()[0]
                    values.append(relevancia)

                if rua is not None and rua.strip() != "":
                    set_values += "rua = ?, "
                    values.append(rua)
                else:
                    cursor.execute(f'SELECT rua FROM Clientes WHERE id = ?', (id,))
                    set_values += "rua = ?, "
                    rua = cursor.fetchone()[0]
                    values.append(rua)

                if status is not None and status.strip() != "":
                    set_values += "status = ?, "
                    values.append(status)
                else:
                    cursor.execute(f'SELECT status FROM Clientes WHERE id = ?', (id,))
                    set_values += "status = ?, "
                    status = cursor.fetchone()[0]
                    values.append(status)

                if set_values:
                    set_values = set_values.rstrip(', ')

                query = f'UPDATE Clientes SET {set_values} WHERE id = ?'
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
            cursor.execute("DELETE FROM Clientes WHERE id = ?", (id,))
            connection.commit()
            print('Delete data successfully')
        except sqlite3.Error as e:
            print(f'Error Delete ', {e})
        finally:
            self.receiver.close_connection()

    def buscar_valor_relevancia(self, id):
        connection = self.receiver.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT descricao FROM relevancia WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        connection.close()

        # Verifique se o resultado foi encontrado
        if resultado:
            return resultado[0]
        else:
            return None

    def buscar_valor_status(self, id):
        connection = self.receiver.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT descricao FROM status WHERE id = ?", (id,))
        resultado = cursor.fetchone()
        connection.close()

        # Verifique se o resultado foi encontrado
        if resultado:
            return resultado[0]
        else:
            return None

