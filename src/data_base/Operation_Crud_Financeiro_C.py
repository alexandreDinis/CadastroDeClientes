import sqlite3

from prettytable import PrettyTable
from termcolor import colored
from src.data_base.Connect_DB import Connect_DB


class Operations_Crud_Financeiro_C:

    def __init__(self):
        path = "data_base/cadastro_clientes.db"
        self.receiver = Connect_DB(path)

    def id_cliente_exists(self, id_cliente):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('SELECT 1 FROM "Clientes" WHERE id = ?', (id_cliente,))
            return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print('Error checking if id_cliente exists:', e)
            return False
        finally:
            self.receiver.close_connection()

    def insert_db_entrada(self, id_cliente, valor, data):
        try:
            if not self.id_cliente_exists(id_cliente):
                print(f'Error: id_cliente {id_cliente} does not exist in "Clientes" table.')
                return

            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO "Entradas" VALUES(NULL, ?, ?, ?)', (id_cliente, valor, data))

            connection.commit()
            print('\nInsert successfully\n')
        except sqlite3.Error as e:
            print('Insert not successful:', e)
        finally:
            self.receiver.close_connection()



    def insert_db_saida(self, valor, data):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO "Saida" VALUES(NULL, ?, ?)', (valor, data))

            connection.commit()
            print('\nInsert successfully\n')
        except sqlite3.Error as e:
            print('Insert not successful:', e)
        finally:
            self.receiver.close_connection()

    def relatorio_financeiro(self, ano=None, mes=None, id_cliente=None):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            if id_cliente:
                if ano and mes:
                    cursor.execute('''
                        SELECT e.id_cliente, c.nome, c.cidade, SUM(e.valor) as total_entradas
                        FROM "Entradas" e
                        JOIN "Clientes" c ON e.id_cliente = c.id
                        WHERE (strftime("%Y-%m", e.data) = ? OR ? IS NULL) AND e.id_cliente = ?
                        GROUP BY e.id_cliente, c.nome, c.cidade
                    ''', (f'{ano}-{mes:02}', f'{ano}-{mes:02}', id_cliente))
                elif ano:
                    cursor.execute('''
                        SELECT e.id_cliente, c.nome, c.cidade, SUM(e.valor) as total_entradas
                        FROM "Entradas" e
                        JOIN "Clientes" c ON e.id_cliente = c.id
                        WHERE (strftime("%Y", e.data) = ? OR ? IS NULL) AND e.id_cliente = ?
                        GROUP BY e.id_cliente, c.nome, c.cidade
                    ''', (ano, ano, id_cliente))
                else:
                    cursor.execute('''
                        SELECT e.id_cliente, c.nome, c.cidade, SUM(e.valor) as total_entradas
                        FROM "Entradas" e
                        JOIN "Clientes" c ON e.id_cliente = c.id
                        WHERE e.id_cliente = ?
                        GROUP BY e.id_cliente, c.nome, c.cidade
                    ''', (id_cliente,))
            else:
                if ano and mes:
                    cursor.execute('''
                        SELECT e.id_cliente, c.nome, c.cidade, SUM(e.valor) as total_entradas
                        FROM "Entradas" e
                        JOIN "Clientes" c ON e.id_cliente = c.id
                        WHERE (strftime("%Y-%m", e.data) = ? OR ? IS NULL)
                        GROUP BY e.id_cliente, c.nome, c.cidade
                    ''', (f'{ano}-{mes:02}', f'{ano}-{mes:02}'))
                elif ano:
                    cursor.execute('''
                        SELECT e.id_cliente, c.nome, c.cidade, SUM(e.valor) as total_entradas
                        FROM "Entradas" e
                        JOIN "Clientes" c ON e.id_cliente = c.id
                        WHERE (strftime("%Y", e.data) = ? OR ? IS NULL)
                        GROUP BY e.id_cliente, c.nome, c.cidade
                    ''', (ano, ano))
                else:
                    cursor.execute('''
                        SELECT e.id_cliente, c.nome, c.cidade, SUM(e.valor) as total_entradas
                        FROM "Entradas" e
                        JOIN "Clientes" c ON e.id_cliente = c.id
                        GROUP BY e.id_cliente, c.nome, c.cidade
                    ''')

            results = cursor.fetchall()

            if results:
                print('{:<10} {:<20} {:<20} {:<10}'.format('ID Cliente', 'Nome', 'Cidade', 'Total Entradas'))
                print('-' * 60)

                for row in results:
                    print('{:<10} {:<20} {:<20} R$ {:<10.2f}'.format(row[0], row[1], row[2], row[3]))

                print('-' * 60)

                # Calcula e imprime o total geral
                total_geral = sum(row[3] for row in results)
                print('Total Geral: R$ {:.2f}'.format(total_geral))
                return total_geral
            else:
                print('Nenhuma entrada encontrada.')
        except sqlite3.Error as e:
            print('Error generating general report:', e)
        finally:
            self.receiver.close_connection()

    def get_valor_por_ano_mes_entrada(self, ano, mes):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('''
                SELECT COALESCE(SUM(valor), 0) 
                FROM "Entradas" 
                WHERE strftime("%Y", data) = ? AND strftime("%m", data) = ?
            ''', (ano, mes))
            return cursor.fetchone()[0]
        except sqlite3.Error as e:
            print('Error getting value for year and month:', e)
            return 0
        finally:
            self.receiver.close_connection()

    def get_valor_por_ano_mes_saida(self, ano, mes):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('''
                SELECT COALESCE(SUM(valor), 0) 
                FROM "Saida" 
                WHERE strftime("%Y", data) = ? AND strftime("%m", data) = ?
            ''', (ano, mes))
            return cursor.fetchone()[0]
        except sqlite3.Error as e:
            print('Error getting value for year and month:', e)
            return 0
        finally:
            self.receiver.close_connection()

    def adicionar_categoria(self, nome_categoria):
        # Conectar ao banco de dados (se não existir, será criado)
        conn = sqlite3.connect('cadastro_clientes.db')

        # Criar um cursor para executar comandos SQL
        cursor = conn.cursor()

        # Inserir uma nova categoria
        insert_categoria_sql = f'''
        INSERT INTO Categoria (nome_categoria)
        VALUES ('{nome_categoria}');
        '''

        # Executar o comando SQL para inserir a nova categoria
        cursor.execute(insert_categoria_sql)

        # Commit para salvar as alterações
        conn.commit()

        # Fechar a conexão
        conn.close()

    def os_id_exists(self, os_id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('SELECT 1 FROM "os" WHERE id = ?', (os_id,))
            return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print('Error checking if os_id exists:', e)
            return False
        finally:
            self.receiver.close_connection()

    def abrir_a_receber(self, os_id, valor, status, data):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            # Verifica se o os_id existe antes de inserir na tabela A_Receber
            if not self.os_id_exists(os_id):
                print("os_id não encontrado.")
                return False

            # Insere os dados na tabela A_Receber
            cursor.execute('INSERT INTO "A_Receber" (os_id, valor, status, data) VALUES (?, ?, ?, ?)',
                           (os_id, valor, status, data))
            connection.commit()

            print("Dados inseridos com sucesso na tabela A_Receber.")
            return True

        except sqlite3.Error as e:
            print('Error inserting data into A_Receber:', e)
            return False

        finally:
            self.receiver.close_connection()

    def a_receber_id_exists(self, os_id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('SELECT 1 FROM "A_Receber" WHERE id = ?', (os_id,))
            return cursor.fetchone() is not None
        except sqlite3.Error as e:
            print('Error checking if os_id exists:', e)
            return False
        finally:
            self.receiver.close_connection()

    def search_a_receber(self, opc, column, search):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            if opc != '-1':
                cursor.execute(f'SELECT * FROM "A_Receber" WHERE {column} = ?', (search,))
            else:
                cursor.execute('SELECT * FROM "A_Receber"')

            result = cursor.fetchall()

            if result:
                table = PrettyTable()
                table.field_names = ["ID", "os_id", "Valor", "Status", "Data"]

                total_valor = 0  # Inicializa o total da coluna "Valor"

                for row in result:
                    table.add_row(row)
                    total_valor += float(row[2])  # Adiciona o valor da coluna "Valor" ao total

                print("\nA_Receber found:")
                print(table)
                print("-" * 160)

                # Adiciona uma linha "total" ao PrettyTable
                table.add_row(["Total", "", f"{total_valor:.2f}", "", ""])
                print(f"Total Valor: {total_valor:.2f}")

                return result, total_valor
            else:
                print('A_Receber not found')
                return -1

        except sqlite3.Error as e:
            print('Error in search', e)

        finally:
            self.receiver.close_connection()

    def update_a_receber(self, os_id, valor, status, data, id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            set_values = ""
            values = []

            validation = self.search_a_receber('-1', 'id', id)

            if validation != -1:

                if os_id is not None and os_id.strip() != "":
                    set_values += "os_id=?, "
                    values.append(os_id)
                else:
                    cursor.execute(f'SELECT os_id FROM "A_Receber" WHERE id = ?', (id,))
                    set_values += "os_id=?, "
                    os_id = cursor.fetchone()[0]
                    values.append(os_id)

                if valor is not None:
                    set_values += "valor=?, "
                    values.append(valor)
                else:
                    cursor.execute(f'SELECT valor FROM "A_Receber" WHERE id = ?', (id,))
                    set_values += "valor=?, "
                    valor = cursor.fetchone()[0]
                    values.append(valor)

                if status is not None and status.strip() != "":
                    set_values += "status=?, "
                    values.append(status)
                else:
                    cursor.execute(f'SELECT status FROM "A_Receber" WHERE id = ?', (id,))
                    set_values += "status=?, "
                    status = cursor.fetchone()[0]
                    values.append(status)

                if data is not None and data.strip() != "":
                    set_values += "data=?, "
                    values.append(data)
                else:
                    cursor.execute(f'SELECT data FROM "A_Receber" WHERE id = ?', (id,))
                    set_values += "data=?, "
                    data = cursor.fetchone()[0]
                    values.append(data)

                if set_values:
                    set_values = set_values.rstrip(', ')

                query = f'UPDATE "A_Receber" SET {set_values} WHERE id = ?'
                values.append(id)
                cursor.execute(query, tuple(values))

                connection.commit()

                print('Database update successfully\n')
                print()
                self.search_a_receber('-1', 'id', id)

        except sqlite3.Error as e:
            print('Error when update', e)
        finally:
            self.receiver.close_connection()

    def insert_despesa_empresa(self, data, valor, categoria_id, descricao):
        conn = self.receiver.connect()
        cursor = conn.cursor()

        insert_sql = '''
        INSERT INTO DespesasEmpresa (data, valor, categoria_id, descricao)
        VALUES (?, ?, ?, ?);
        '''

        cursor.execute(insert_sql, (data, valor, categoria_id, descricao))
        conn.commit()

        print(colored("Registro de despesas inserido com sucesso!", "green"))

        self.receiver.close_connection()
