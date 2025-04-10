import requests
from bs4 import BeautifulSoup
import sqlite3
import time

# Conectar/criar o banco de dados
conn = sqlite3.connect('livros.db')
cursor = conn.cursor()

# Criar a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preco TEXT,
        link TEXT,
        categoria TEXT
    )
''')
conn.commit()

# Função para buscar a categoria na página do livro
def buscar_categoria(url_livro):
    try:
        response = requests.get(url_livro)
        soup = BeautifulSoup(response.text, 'html.parser')
        categoria_tag = soup.find('a', class_='bread-crumb')
        if categoria_tag:
            return categoria_tag.text.strip()
    except:
        return None

# Função principal
def coletar_livros():
    url = 'https://www.darksidebooks.com.br/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    produtos = soup.find_all('div', class_='shelf-product')

    for produto in produtos:
        a_tag = produto.find('a')
        nome = produto.find('span', class_='shelf-product-title').text.strip()
        preco = produto.find('span', class_='skuBestPrice').text.strip()
        link = 'https://www.darksidebooks.com.br' + a_tag['href']
        
        categoria = buscar_categoria(link)
        
        cursor.execute('''
            INSERT INTO livros (nome, preco, link, categoria)
            VALUES (?, ?, ?, ?)
        ''', (nome, preco, link, categoria))
        conn.commit()
        
        print(f'Livro salvo: {nome} | {preco} | {categoria}')

# Rodar a coleta
coletar_livros()

# Fechar a conexão
conn.close()