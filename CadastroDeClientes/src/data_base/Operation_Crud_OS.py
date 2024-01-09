import sqlite3
from prettytable import PrettyTable
from src.data_base.Connect_DB import Connect_DB


class Operations_Crud_OS:

    def __init__(self):

        path = r"data_base/cadastro_clientes.db"
        self.receiver = Connect_DB(path)

    def insert(self, tipo, cliente_id, km_inicial, km_final, financeiro,status_id, data_inicial, data_final):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            cursor.execute('''
                   INSERT INTO os (tipo, cliente_id, km_inicial, km_final, financeiro, status_id, data_inicial, data_final)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)
               ''', (tipo, cliente_id, km_inicial, km_final, financeiro, status_id, data_inicial, data_final))

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
                    table.field_names = table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro", "Status ID",
                     "Data Inicial", "Data Final"]

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
                    table.field_names = table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro", "Status ID",
                     "Data Inicial", "Data Final"]

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

    def update(self, tipo, cliente_id, km_inicial, km_final, financeiro, status_id, data_inicial, data_final, id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            set_values = ""
            values = []

            validation = self.search_db(-1, 'id', id)

            if validation != -1:

                if tipo is not None and tipo.strip() != "":
                    set_values += "tipo=?, "
                    values.append(tipo)
                else:
                    cursor.execute(f'SELECT tipo FROM os WHERE id = ?', (id,))
                    set_values += "tipo=?, "
                    tipo = cursor.fetchone()[0]
                    values.append(tipo)

                if cliente_id is not None and cliente_id.strip() != "":
                    set_values += "cliente_id=?, "
                    values.append(cliente_id)
                else:
                    cursor.execute(f'SELECT cliente_id FROM os WHERE id = ?', (id,))
                    set_values += "cliente_id=?, "
                    cliente_id = cursor.fetchone()[0]
                    values.append(cliente_id)

                if km_inicial is not None and km_inicial != "":
                    set_values += "km_inicial=?, "
                    values.append(km_inicial)
                else:
                    cursor.execute(f'SELECT km_inicial FROM os WHERE id = ?', (id,))
                    set_values += "km_inicial=?, "
                    km_inicial = cursor.fetchone()[0]
                    values.append(km_inicial)

                if km_final is not None and km_final != "":
                    set_values += "km_final=?, "
                    values.append(km_final)
                else:
                    cursor.execute(f'SELECT km_final FROM os WHERE id = ?', (id,))
                    set_values += "km_final=?, "
                    km_final = cursor.fetchone()[0]
                    values.append(km_final)

                if financeiro is not None and financeiro != "":
                    set_values += "financeiro=?, "
                    values.append(financeiro)
                else:
                    cursor.execute(f'SELECT financeiro FROM os WHERE id = ?', (id,))
                    set_values += "financeiro=?, "
                    financeiro = cursor.fetchone()[0]
                    values.append(financeiro)

                if status_id is not None and status_id.strip() != "":
                    set_values += "status_id=?, "
                    values.append(status_id)
                else:
                    cursor.execute(f'SELECT status_id FROM os WHERE id = ?', (id,))
                    set_values += "status_id=?, "
                    status_id = cursor.fetchone()[0]
                    values.append(status_id)

                if data_inicial is not None and data_inicial.strip() != "":
                    set_values += "data_inicial=?, "
                    values.append(data_inicial)
                else:
                    cursor.execute(f'SELECT data_inicial FROM os WHERE id = ?', (id,))
                    set_values += "data_inicial=?, "
                    data_inicial = cursor.fetchone()[0]
                    values.append(data_inicial)

                if data_final is not None and data_final != "":
                    set_values += "data_final=?, "
                    values.append(data_final)
                else:
                    cursor.execute(f'SELECT data_final FROM os WHERE id = ?', (id,))
                    set_values += "data_final=?, "
                    data_final = cursor.fetchone()[0]
                    values.append(data_final)

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

    def update_cliente_id(self, cliente_id, id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            validation = self.search_db(-1, 'id', id)

            if validation != -1:
                if cliente_id is not None and cliente_id.strip() != "":
                    query = 'UPDATE os SET cliente_id=? WHERE id=?'
                    cursor.execute(query, (cliente_id, id))

                    connection.commit()

                    print('Database update successfully\n')
                    print()
                    self.search_db(-1, 'id', id)

        except sqlite3.Error as e:
            print('Error when update', e)
        finally:
            self.receiver.close_connection()

    def delete(self, id):
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

    def imprimir_tabela_tipo_ordem(self):
        """Imprime as colunas id e descricao da tabela tipo_ordem em formato de tabela."""

        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM tipo_ordem")
            dados = cursor.fetchall()

            # Cria a tabela usando PrettyTable
            tabela = PrettyTable(["ID", "Descrição"])
            for linha in dados:
                tabela.add_row(linha)

            print(tabela)

        except sqlite3.Error as e:
            print("Erro ao imprimir tabela:", e)

        finally:
            self.receiver.close_connection()

    def get_descricao_by_id(self, tipo_ordem_id):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            # Consulta SQL para obter a coluna 'descricao' da tabela 'tipo_ordem' para um ID específico
            sql_query = 'SELECT descricao FROM tipo_ordem WHERE id = ?'

            cursor.execute(sql_query, (tipo_ordem_id,))
            result = cursor.fetchone()

            if result:
                descricao = result[0]
                return descricao
            else:
                return None

        except sqlite3.Error as e:
            print('Error in search', e)
        finally:
            self.receiver.close_connection()

    def filtrar_os_por_parametros(self, ano=None, mes=None, status_id=None, cliente=None):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            # Construir a consulta SQL base
            sql_query = 'SELECT * FROM os WHERE 1=1'

            # Adicionar condições ao SQL com base nos parâmetros fornecidos
            params = []

            if ano:
                sql_query += ' AND strftime("%Y", data_inicial) = ?'
                params.append(ano)
            if mes:
                sql_query += ' AND strftime("%m", data_inicial) = ?'
                params.append(mes)
            if status_id:
                sql_query += ' AND status_id = ?'
                params.append(status_id)
            if cliente:
                sql_query += ' AND cliente_id = ?'
                params.append(cliente)

            # Executar a consulta SQL
            cursor.execute(sql_query, tuple(params))
            result = cursor.fetchall()

            if result:
                # Exibir os resultados em uma tabela padrão
                table = PrettyTable()
                table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro", "Status ID",
                                     "Data Inicial", "Data Final"]

                for row in result:
                    table.add_row(row)

                print("\nOS found:")
                print(table)
                print("-" * 160)
                return result
            else:
                print('No OS found with the specified filters')
                return None

        except sqlite3.Error as e:
            print('Error in filtering OS', e)
        finally:
            self.receiver.close_connection()

    def filtrar_os_por_filtros_interativos(self):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            filtros = {
                "ano": None,
                "mes": None,
                "status_id": None,
                "cliente_id": None
            }

            while True:
                print("\nFiltros atuais:")
                for i, (chave, valor) in enumerate(filtros.items(), 1):
                    print(f"{i}. {chave.capitalize()}: {valor or 'Nenhum'}")

                print("Escolha um número para adicionar/remover filtro:")
                print("1. Ano")
                print("2. Mês")
                print("3. Status")
                print("4. Cliente ID")
                print("5. Limpar filtros")
                print("0. Fechar")

                opcao = int(input("Opção: "))

                if opcao == 1:
                    chave = "ano"
                elif opcao == 2:
                    chave = "mes"
                elif opcao == 3:
                    chave = "status_id"
                elif opcao == 4:
                    chave = "cliente_id"
                elif opcao == 5:
                    filtros = {chave: None for chave in filtros}
                    print("Filtros limpos.")
                    continue
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida. Tente novamente.")
                    continue

                valor = input(f"Digite o valor para o filtro {chave.capitalize()}: ")
                filtros[chave] = valor

            # Construir a consulta SQL base
            sql_query = 'SELECT * FROM os WHERE 1=1'

            # Adicionar condições ao SQL com base nos parâmetros fornecidos
            params = []

            for chave, valor in filtros.items():
                if valor:
                    if chave == "ano":
                        sql_query += ' AND strftime("%Y", data_inicial) = ?'
                    elif chave == "mes":
                        sql_query += ' AND strftime("%m", data_inicial) = ?'
                    else:
                        sql_query += f' AND {chave} = ?'

                    params.append(valor)

            # Executar a consulta SQL
            cursor.execute(sql_query, tuple(params))
            result = cursor.fetchall()

            if result:
                # Exibir os resultados em uma tabela padrão
                table = PrettyTable()
                table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro", "Status ID",
                                     "Data Inicial", "Data Final"]

                for row in result:
                    table.add_row(row)

                print("\nOS found:")
                print(table)
                print("-" * 160)
                return result
            else:
                print('No OS found with the specified filters')
                return None

        except sqlite3.Error as e:
            print('Error in filtering OS', e)
        finally:
            self.receiver.close_connection()

    def mostrar_tabela_geral_os(self):
        try:
            connection = self.receiver.connect()
            cursor = connection.cursor()

            cursor.execute('SELECT * FROM os')
            result = cursor.fetchall()

            if result:
                table = PrettyTable()
                table.field_names = ["ID", "Tipo", "Cliente ID", "KM Inicial", "KM Final", "Financeiro", "Status ID",
                                     "Data Inicial", "Data Final"]

                for row in result:
                    table.add_row(row)

                print("\nTabela Geral de OS:")
                print(table)
                print("-" * 160)
            else:
                print('Nenhuma OS encontrada.')
        except sqlite3.Error as e:
            print('Erro ao mostrar tabela geral de OS', e)
        finally:
            self.receiver.close_connection()

