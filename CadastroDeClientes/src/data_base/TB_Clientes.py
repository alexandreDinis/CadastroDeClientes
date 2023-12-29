import sqlite3
from datetime import datetime

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