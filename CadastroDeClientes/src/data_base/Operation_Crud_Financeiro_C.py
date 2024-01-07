import sqlite3
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

    def insert_a_receber(self, id_os, valor, status,  data):
        try:
            if not self.id_cliente_exists(id_os):
                print(f'Error: id_os {id_os} does not exist in "O.S" table.')
                return

            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute('INSERT INTO "A_Receber" VALUES(NULL, ?, ?, ?, ?)', (id_os, valor, status, data))

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
