import sqlite3

# Conectar (vai criar o banco se não existir)
conn = sqlite3.connect('produtos.db')
cursor = conn.cursor()

# Criar a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        preco TEXT
    )
''')

conn.commit()
conn.close()

print("Banco e tabela criados com sucesso!")
