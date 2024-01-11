import sqlite3
from src.data_base.Connect_DB import Connect_DB
db = Connect_DB('cadastro_clientes.db')

def tb_clientes():
    # Conectar ao banco de dados (se não existir, será criado)
    conn = sqlite3.connect('cadastro_clientes.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Definir o comando SQL para criar a tabela Clientes
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        contato TEXT NOT NULL,
        rua TEXT,
        bairro TEXT,
        cidade TEXT NOT NULL,
        phone TEXT,
        setor TEXT,
        relevancia TEXT NOT NULL,
        status TEXT NOT NULL,
        data TEXT NOT NULL
    );
    '''

    # Executar o comando SQL para criar a tabela
    cursor.execute(create_table_sql)

    # Commit para salvar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()
def criar_tabela_entradas_saidas():
    # Conectar ao banco de dados com suporte a chaves estrangeiras
    conn = sqlite3.connect("cadastro_clientes.db")
    conn.execute("PRAGMA foreign_keys = ON")  # Ativar verificação de chave estrangeira
    cursor = conn.cursor()

    try:
        # Verificar se a tabela Entradas existe
        if not cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Entradas'").fetchone():

            # Criar tabela Entradas com restrição de chave estrangeira
            cursor.execute('''
            CREATE TABLE Entradas (
                id INTEGER PRIMARY KEY,
                id_cliente INTEGER,
                valor REAL,
                data DATE,
                FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
            );
            ''')

        # Verificar se a tabela Saida existe
        if not cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Saida'").fetchone():

            # Criar tabela Saida
            cursor.execute('''
            CREATE TABLE Saida (
                id INTEGER PRIMARY KEY,
                valor REAL,
                data DATE
            );
            ''')

        # Commit e fechar conexão
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro: {e}")
    finally:
        conn.close()

def create_relevancia_table():
    connection = sqlite3.connect("cadastro_clientes.db")
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS relevancia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(10) NOT NULL
            );
        """)

        # Inserir registros de exemplo
        cursor.execute("INSERT INTO relevancia (descricao) VALUES ('FORTE');")
        cursor.execute("INSERT INTO relevancia (descricao) VALUES ('MEDIO');")
        cursor.execute("INSERT INTO relevancia (descricao) VALUES ('FRACO');")

        connection.commit()
    finally:
        connection.close()

def create_status_table():
    connection = sqlite3.connect("cadastro_clientes.db")
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS status (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(10) NOT NULL
            );
        """)

        # Inserir registros de exemplo
        cursor.execute("INSERT INTO status (descricao) VALUES ('ATIVO');")
        cursor.execute("INSERT INTO status (descricao) VALUES ('INATIVO');")
        cursor.execute("INSERT INTO status (descricao) VALUES ('PROSPC');")

        connection.commit()
    finally:
        connection.close()

def criar_tabela_viagens():
    path = "cadastro_clientes.db"

    try:
        connection = sqlite3.connect(path)
        cursor = connection.cursor()

        # Criar a tabela "viagens"
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS viagens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data DATE NOT NULL,
                km INTEGER NOT NULL,
                valor REAL NOT NULL,
                valor_comb REAL NOT NULL
            );
        ''')
        connection.commit()
        print("Tabela 'viagens' criada com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro: {e}")
    finally:
        connection.close()

def criar_tabela_carros():
    # Substitua pelo caminho e nome do seu banco de dados
    path = "cadastro_clientes.db"

    try:
        with sqlite3.connect(path) as connection:
            cursor = connection.cursor()

            # Criar a tabela "carros"
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS carros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    marca TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    placa TEXT NOT NULL,
                    ano INTEGER NOT NULL,
                    km_inicial INTEGER NOT NULL,
                    km_atual INTEGER NOT NULL,
                    autonomia INTEGER NOT NULL
                );
            ''')
            connection.commit()
            print("Tabela 'carros' criada  com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro: {e}")

def criar_tabela_tipo_ordem():
    # Substitua pelo caminho e nome do seu banco de dados
    path = "cadastro_clientes.db"

    try:
        with sqlite3.connect(path) as connection:
            cursor = connection.cursor()

            # Criar a tabela "tipo_ordem"
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tipo_ordem (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT NOT NULL,
                    valor TEXT NOT NULL
                );
            ''')

            # Inserir os valores PROSPECCAO, ATENDIMENTO, ORCAMENTO
            cursor.executemany('''
                INSERT INTO tipo_ordem (descricao, valor) VALUES (?, ?);
            ''', [('PROSPECCAO', 'PROSPECCAO'), ('ATENDIMENTO', 'ATENDIMENTO'), ('ORCAMENTO', 'ORCAMENTO')])

            connection.commit()
            print("Tabela 'tipo_ordem' criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro: {e}")

def criar_tabela_os():
    # Substitua pelo caminho e nome do seu banco de dados
    path = "cadastro_clientes.db"

    try:
        with sqlite3.connect(path) as connection:
            cursor = connection.cursor()

            # Criar a tabela "os"
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS os (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT NOT NULL,
                    cliente_id INTEGER,
                    km_inicial INTEGER,
                    km_final INTEGER,
                    financeiro REAL,
                    hora_inicial TEXT,
                    hora_final TEXT,
                    status_id INTEGER,
                    data TEXT,
                    FOREIGN KEY (cliente_id) REFERENCES Clientes(id),
                    FOREIGN KEY (status_id) REFERENCES status(id)
                );
            ''')

            connection.commit()
            print("Tabela 'os' criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro: {e}")


def tb_categoria():
    # Conectar ao banco de dados (se não existir, será criado)
    conn = sqlite3.connect('cadastro_clientes.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Definir o comando SQL para criar a tabela Categoria
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS Categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_categoria TEXT NOT NULL
    );
    '''

    # Executar o comando SQL para criar a tabela
    cursor.execute(create_table_sql)

    # Commit para salvar as alterações
    conn.commit()

    # Inserir valores na tabela Categoria
    insert_values_sql = '''
    INSERT INTO Categoria (nome_categoria)
    VALUES
        ('aluguel'),
        ('telefone'),
        ('tarifas bancaria'),
        ('impostos'),
        ('financiamento'),
        ('Mercado'),
        ('combustivel'),
        ('Cigarros'),
        ('Streaming'),
        ('Garagem'),
        ('seg_vida'),
        ('Internet'),
        ('Barbearia'),
        ('tv'),
        ('Agua'),
        ('luz'),
        ('pets');
    '''

    # Executar o comando SQL para inserir valores
    cursor.execute(insert_values_sql)

    # Commit para salvar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()


def tabelas_financeiro_pessoal():
    # Conectar ao banco de dados (se não existir, será criado)
    conn = sqlite3.connect('cadastro_clientes.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Definir o comando SQL para criar a tabela Categoria
    create_categoria_table_sql = '''
    CREATE TABLE IF NOT EXISTS Categoria (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_categoria TEXT NOT NULL
    );
    '''

    # Executar o comando SQL para criar a tabela Categoria
    cursor.execute(create_categoria_table_sql)

    # Definir o comando SQL para criar a tabela DespesasFixas
    create_despesas_fixas_table_sql = '''
    CREATE TABLE IF NOT EXISTS DespesasFixas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        valor REAL NOT NULL,
        categoria_id INTEGER,
        descricao TEXT,
        FOREIGN KEY (categoria_id) REFERENCES Categoria (id)
    );
    '''

    # Executar o comando SQL para criar a tabela DespesasFixas
    cursor.execute(create_despesas_fixas_table_sql)

    # Definir o comando SQL para criar a tabela DespesasVariaveis
    create_despesas_variaveis_table_sql = '''
    CREATE TABLE IF NOT EXISTS DespesasVariaveis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        valor REAL NOT NULL,
        categoria_id INTEGER,
        descricao TEXT,
        FOREIGN KEY (categoria_id) REFERENCES Categoria (id)
    );
    '''

    # Executar o comando SQL para criar a tabela DespesasVariaveis
    cursor.execute(create_despesas_variaveis_table_sql)

    # Definir o comando SQL para criar a tabela DespesasInesperadas
    create_despesas_inesperadas_table_sql = '''
    CREATE TABLE IF NOT EXISTS DespesasInesperadas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        valor REAL NOT NULL,
        categoria_id INTEGER,
        descricao TEXT,
        FOREIGN KEY (categoria_id) REFERENCES Categoria (id)
    );
    '''

    # Executar o comando SQL para criar a tabela DespesasInesperadas
    cursor.execute(create_despesas_inesperadas_table_sql)

    # Commit para salvar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()


def tb_abastecimento():
    # Conectar ao banco de dados (se não existir, será criado)
    conn = sqlite3.connect('cadastro_clientes.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Definir o comando SQL para criar a tabela Clientes
    create_table_sql = '''
                CREATE TABLE IF NOT EXISTS Abastecimento (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    km INTEGER NOT NULL,
                    valor_comb REAL NOT NULL,
                    data TEXT NOT NULL
                );
                '''

    # Executar o comando SQL para criar a tabela
    cursor.execute(create_table_sql)

    # Commit para salvar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()

def criar_tabela_a_receber():
    # Conectar ao banco de dados (se não existir, será criado)
    conn = sqlite3.connect('cadastro_clientes.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Definir o comando SQL para criar a tabela A_Receber
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS A_Receber (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        os_id INTEGER NOT NULL,
        valor REAL NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (os_id) REFERENCES OS(id)
    );
    '''

    # Executar o comando SQL para criar a tabela
    cursor.execute(create_table_sql)

    # Commit para salvar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()

def tb_estatisticas():
    # Conectar ao banco de dados (se não existir, será criado)
    db = Connect_DB('cadastro_clientes.db')
    conn = db.connect()

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Definir o comando SQL para criar a tabela Estatisticas
    create_table_sql = '''
     CREATE TABLE IF NOT EXISTS Estatisticas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        os_id INTEGER,
        valor_id INTEGER,
        cliente_id INTEGER,
        atendimento TEXT,
        hora_trabalhada REAL,
        hora REAL,
        km_rodado REAL,
        data TEXT,
        FOREIGN KEY (os_id) REFERENCES os(id),
        FOREIGN KEY (cliente_id) REFERENCES Clientes(id)
    );
    '''

    # Executar o comando SQL para criar a tabela
    cursor.execute(create_table_sql)

    # Commit para salvar as alterações no banco de dados
    conn.commit()

    # Fechar a conexão com o banco de dados
    db.close_connection()


def criar_tabela_despesa_empresa():
    # Conectar ao banco de dados (se não existir, será criado)
    conn = sqlite3.connect('cadastro_clientes.db')

    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # Definir o comando SQL para criar a tabela DespesaEmpresa
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS DespesaEmpresa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT NOT NULL,
        valor REAL NOT NULL,
        id_categoria INTEGER NOT NULL,
        descricao TEXT,
        FOREIGN KEY (id_categoria) REFERENCES Categoria(id)
    );
    '''

    # Executar o comando SQL
    cursor.execute(create_table_sql)

    # Confirmar a transação
    conn.commit()

    # Fechar a conexão com o banco de dados
    conn.close()


def gerdor_de_tableas():

    tb_clientes()
    criar_tabela_entradas_saidas()
    create_relevancia_table()
    create_status_table()
    criar_tabela_viagens()
    criar_tabela_carros()
    criar_tabela_os()
    tb_categoria()
    tabelas_financeiro_pessoal()

criar_tabela_despesa_empresa()



