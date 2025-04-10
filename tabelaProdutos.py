import sqlite3

# Conectar (ou criar) o banco
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

# Criar a tabela produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    preco TEXT
)
''')

# Salvar e fechar
conn.commit()
conn.close()

print("Banco e tabela criados com sucesso!")
