import sqlite3

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

def gerdor_de_tableas():

    tb_clientes()
    criar_tabela_entradas_saidas()
    create_relevancia_table()
    create_status_table()


gerdor_de_tableas()
