import sqlite3
from src.data_base.Connect_DB import Connect_DB
from src.data_base.Operation_Crud_OS import Operations_Crud_OS

os = Operations_Crud_OS()


class Operations_Crud_Estatisticas:

    def __init__(self):
        path = "data_base/cadastro_clientes.db"
        self.receiver = Connect_DB(path)

    def insert_estatistica(self, os_id, valor_id, cliente_id, atendimento, hora_trabalhada, km_rodado, data):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            cursor.execute('''
                INSERT INTO Estatisticas (os_id, valor_id, cliente_id, atendimento, hora, km_rodado, data)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (os_id, valor_id, cliente_id, atendimento, hora_trabalhada, km_rodado, data))

            connection.commit()

            print('Dados inseridos na tabela Estatisticas com sucesso.\n')

        except sqlite3.Error as e:
            print('Erro ao inserir dados na tabela Estatisticas:', e)

        finally:
            self.receiver.close_connection()

    def imprimir_tabela_por_ano_mes(self, ano=None, mes=None):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            if ano is not None and mes is not None:
                cursor.execute('''
                       SELECT c.nome, e.atendimento, e.hora_trabalhada, e.km_rodado, e.data
                       FROM Estatisticas e
                       JOIN Clientes c ON e.cliente_id = c.id
                       WHERE strftime('%Y', e.data) = ? AND strftime('%m', e.data) = ?
                   ''', (str(ano), str(mes).zfill(2)))
            else:
                cursor.execute('''
                       SELECT c.nome, e.atendimento, e.hora_trabalhada, e.km_rodado, e.data
                       FROM Estatisticas e
                       JOIN Clientes c ON e.cliente_id = c.id
                   ''')

            result = cursor.fetchall()

            if result:
                # Imprimir cabeçalho
                print(f"{'Nome': <20}{'Atendimento': <30}{'Hora Trabalhada': <20}{'Km Rodado': <15}{'Data': <15}")
                print('-' * 110)

                # Imprimir linhas da tabela
                for row in result:
                    print(f"{row[0]: <20}{row[1]: <30}{row[2]: <20}{row[3]: <15}{row[4]: <15}")

            else:
                print('Não há registros para o período especificado.')

        except sqlite3.Error as e:
            print('Erro ao imprimir tabela por ano e mês:', e)

        finally:
            self.receiver.close_connection()

    def total_km_rodado(self, ano, mes):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            # Comando SQL para somar a coluna km_rodado dentro de um ano e um determinado mês
            sql_total = "SELECT SUM(km_rodado) FROM Estatisticas WHERE strftime('%Y-%m', data) = ?"

            # Dados a serem usados na consulta
            data = (f"{ano:04d}-{mes:02d}",)

            # Executar o comando SQL
            cursor.execute(sql_total, data)

            # Obter o resultado
            result = cursor.fetchone()

            if result[0] is not None:
                return result[0]  # Retorna o total
            else:
                return 0  # Retorna 0 se não houver registros

        except sqlite3.Error as e:
            print(f"Erro ao calcular o total de km_rodado no ano {ano} e no mês {mes}: {e}")
            return 0

        finally:
            self.receiver.close_connection()
