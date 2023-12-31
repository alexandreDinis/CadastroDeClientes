import sqlite3

from src.data_base.Connect_DB import Connect_DB


class Operations_Crud_Financeiro:

    def __init__(self):
        path = "data_base/cadastro_clientes"
        self.receiver = Connect_DB(path)

    def inserir_entrada(self, id_cliente, valor, data, ):

        try:
            # Conecta ao banco de dados financeiro
            conn_financeiro = self.receiver.connect()

            # Conecta ao banco de dados cadastro_clientes
            conn_cadastro_clientes = Connect_DB("cadastro_clientes.db").connect()

            # Verifica se o cliente existe
            cursor_cadastro_clientes = conn_cadastro_clientes.cursor()
            cursor_cadastro_clientes.execute(
                "SELECT COUNT(*) FROM Clientes WHERE id = ?", (id_cliente,)
            )
            count = cursor_cadastro_clientes.fetchone()[0]

            if count == 0:
                raise ValueError("Cliente não existe")

            # Insere a entrada
            cursor_financeiro = conn_financeiro.cursor()
            cursor_financeiro.execute(
                "INSERT INTO Entradas (id_cliente, valor, data) VALUES (?, ?, ?, )",
                (id_cliente, valor, data,),
            )
            conn_financeiro.commit()

            return cursor_financeiro.lastrowid

        finally:
            # Fecha as conexões com os bancos de dados
            if conn_cadastro_clientes:
                conn_cadastro_clientes.close()
            if conn_financeiro:
                conn_financeiro.close()