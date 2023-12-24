import sqlite3

from Connect_DB import Connect_DB


class Operations_Crud:
    def __init__(self):
        path = r'PycharmProjects/CadastroDeClientes/src/data_base/cadastro_clientes.db'
        self.receiver = Connect_DB(path)

    def insert_db(self, nome, contato, rua, bairro, cidade, phone, setor, relevancia, staus, data):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO cadastro_clientes.db VALUES(NULL, ?, ?, ?, ?)', (nome, contato, rua, bairro, cidade,
                                                                                 phone, setor, relevancia, staus, data))
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
                cursor.execute(f'SELECT * FROM cadastro_clientes.db WHERE {column} = ?', (search,))
                result = cursor.fetchall()
                if result:
                    print("\nContacts found:")
                    print("{:<5} {:<20} {:<30} {:<15} {:<15}{:<15} {:<15}{:<15} {:<15}{:<15}{:<15}".format("ID",
                                                                                                           "nome",
                                                                                                           "contato",
                                                                                                           "rua",
                                                                                                           "bairro",
                                                                                                           "cidade",
                                                                                                           "phone",
                                                                                                           "setor",
                                                                                                           "relevancia",
                                                                                                           "staus",
                                                                                                           "data"))
                    print("-" * 80)
                    for results in result:
                        print("{:<5} {:<20} {:<30} {:<15} {:<15}{:<15} {:<15}{:<15} {:<15}{:<15}{:<15}".format(
                            results[0], results[1], results[2], results[3],
                            results[4], results[5], results[6], results[7],
                            results[8], results[9], results[10]))
                    print("-" * 80)

                else:
                    print('Contact not found')
                    return -1
            if opc == '-1':
                cursor.execute(f'SELECT * {column} {search}')
                result = cursor.fetchall()
                if result:
                    print("\nContacts found:")
                    print("{:<5} {:<20} {:<30} {:<15} {:<15}{:<15} {:<15}{:<15} {:<15}{:<15}{:<15}".format("ID",
                                                                    "nome", "contato", "rua", "bairro", "cidade",
                                                                    "phone", "setor", "relevancia", "staus", "data"))
                    print("-" * 80)
                    for results in result:
                        print("{:<5} {:<20} {:<30} {:<15} {:<15}{:<15} {:<15}{:<15} {:<15}{:<15}{:<15}".format(
                            results[0], results[1], results[2], results[3],
                            results[4], results[5], results[6], results[7],
                            results[8], results[9], results[10]))
                    print("-" * 80)
                else:
                    print('Contact not found')
        except sqlite3.Error as e:
            print('Error in search', e)
        finally:
            self.receiver.close_connection()

    def update(self, nome, contato, rua, bairro, cidade, phone, setor, relevancia, staus, data, id, ):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            set_values = ""
            values = []

            validation = self.search_db(-1, 'id', id,)

            if validation != -1:

                if nome is not None and nome.strip() != "":
                    set_values += "nome=?, "
                    values.append(nome)
                else:
                    cursor.execute(f'SELECT nome FROM cadastro_clientes.db WHERE id = ?', (id,))
                    set_values += "nome=?, "
                    nome = cursor.fetchone()[0]
                    values.append(nome)

                if contato is not None and contato.strip() != "":
                    set_values += "contato = ?, "
                    values.append(contato)
                else:
                    cursor.execute(f'SELECT contato FROM cadastro_clientes.db WHERE N_ID = ?', (id,))
                    set_values += "contato = ?, "
                    contato = cursor.fetchone()[0]
                    values.append(contato)

                if rua is not None and rua.strip() != "":
                    set_values += "rua = ?, "
                    values.append(rua)
                else:
                    cursor.execute(f'SELECT rua FROM cadastro_clientes.db WHERE id = ?', (id,))
                    set_values += "rua = ?, "
                    rua = cursor.fetchone()[0]
                    values.append(rua)

                if set_values:
                    set_values = set_values.rstrip(', ')

                query = f'UPDATE cadastro_clientes.db SET {set_values} WHERE N_ID = ?'
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

    def delete_db(self, T_ID):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM cadastro_clientes.db WHERE N_ID = ?", (T_ID,))
            connection.commit()
            print('Delete data successfully')
        except sqlite3.Error as e:
            print(f'Error Delete ', {e})
        finally:
            self.receiver.close_connection()

