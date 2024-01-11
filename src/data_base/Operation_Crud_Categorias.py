from prettytable import PrettyTable
import sqlite3
from src.data_base.Connect_DB import Connect_DB


class Operation_Crud_Categorias:

    def __init__(self):
        path = "data_base/cadastro_clientes.db"
        self.receiver = Connect_DB(path)

    def insert_categoria(self, nome_categoria):
        try:
            # Conectar ao banco de dados
            conn = self.receiver.connection()

            # Criar um cursor para executar comandos SQL
            cursor = conn.cursor()

            # Comando SQL para inserir na tabela Categoria
            sql_insert = "INSERT INTO Categoria (nome_categoria) VALUES (?)"

            # Dados a serem inseridos
            data = (nome_categoria,)

            # Executar o comando SQL
            cursor.execute(sql_insert, data)

            # Confirmar a transação
            conn.commit()

            print("Inserção bem-sucedida na tabela Categoria.")

        except sqlite3.Error as e:
            print(f"Erro ao inserir na tabela Categoria: {e}")

        finally:
            # Fechar a conexão com o banco de dados
            self.receiver.close_connection()

    def search_categorias(self):
        try:
            # Conectar ao banco de dados
            conn = self.receiver.connection()

            # Criar um cursor para executar comandos SQL
            cursor = conn.cursor()

            # Comando SQL para buscar todas as categorias
            sql_search = "SELECT * FROM Categoria LIMIT 5"

            # Executar o comando SQL
            cursor.execute(sql_search)

            # Obter os resultados
            rows = cursor.fetchall()

            # Criar uma tabela PrettyTable para exibir os resultados
            table = PrettyTable()
            table.field_names = ["ID", "Nome da Categoria"]

            # Adicionar linhas à tabela (máximo de 5 linhas)
            for row in rows[:5]:
                table.add_row(row)

            # Imprimir a tabela
            print(table)

        except sqlite3.Error as e:
            print(f"Erro ao buscar na tabela Categoria: {e}")

        finally:
            # Fechar a conexão com o banco de dados
            self.receiver.close_connection()

    def get_categoria_by_id(self, categoria_id):
        try:
            # Conectar ao banco de dados
            conn = self.receiver.connection()

            # Criar um cursor para executar comandos SQL
            cursor = conn.cursor()

            # Comando SQL para buscar uma categoria por ID
            sql_get_categoria = "SELECT nome_categoria FROM Categoria WHERE id = ?"

            # Dados a serem usados na consulta
            data = (categoria_id,)

            # Executar o comando SQL
            cursor.execute(sql_get_categoria, data)

            # Obter o resultado
            result = cursor.fetchone()

            if result:
                return result[0]  # Retorna o nome da categoria
            else:
                return None  # Retorna None se a categoria não for encontrada

        except sqlite3.Error as e:
            print(f"Erro ao buscar categoria por ID: {e}")
            return None

        finally:
            # Fechar a conexão com o banco de dados
            self.receiver.close_connection()


    def insert_relevancia(self, descricao):
        try:
            # Conectar ao banco de dados
            conn = self.receiver.connection()

            # Criar um cursor para executar comandos SQL
            cursor = conn.cursor()

            # Comando SQL para inserir na tabela Categoria
            sql_insert = "INSERT INTO relevancia (descricao) VALUES (?)"

            # Dados a serem inseridos
            data = (descricao,)

            # Executar o comando SQL
            cursor.execute(sql_insert, data)

            # Confirmar a transação
            conn.commit()

            print("Inserção bem-sucedida na tabela Categoria.")

        except sqlite3.Error as e:
            print(f"Erro ao inserir na tabela Categoria: {e}")

        finally:
            # Fechar a conexão com o banco de dados
            self.receiver.close_connection()

    def insert_status(self, descricao):
        try:
            # Conectar ao banco de dados
            conn = self.receiver.connection()

            # Criar um cursor para executar comandos SQL
            cursor = conn.cursor()

            # Comando SQL para inserir na tabela Categoria
            sql_insert = "INSERT INTO status (descricao) VALUES (?)"

            # Dados a serem inseridos
            data = (descricao,)

            # Executar o comando SQL
            cursor.execute(sql_insert, data)

            # Confirmar a transação
            conn.commit()

            print("Inserção bem-sucedida na tabela Categoria.")

        except sqlite3.Error as e:
            print(f"Erro ao inserir na tabela Categoria: {e}")

        finally:
            # Fechar a conexão com o banco de dados
            self.receiver.close_connection()


