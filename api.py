from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

def coletar_livros():
    livros = []
    options = Options()
    options.add_argument('--headless')  # Executar sem abrir o navegador
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service()  # Pega o ChromeDriver que você já tem instalado no PATH
    driver = webdriver.Chrome(service=service, options=options)

    try:
        url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
        driver.get(url)
        time.sleep(2)  # Espera a página carregar

        elementos_livros = driver.find_elements(By.CLASS_NAME, 'product_pod')

        for elemento in elementos_livros:
            try:
                titulo = elemento.find_element(By.TAG_NAME, 'h3').text
                preco_texto = elemento.find_element(By.CLASS_NAME, 'price_color').text
                preco_float = float(preco_texto.replace('£', '').strip())

                livros.append({
                    'titulo': titulo,
                    'preco': preco_float
                })

            except Exception as e:
                print(f"Erro ao coletar livro: {e}")
                continue  # Pula este livro com erro

    finally:
        driver.quit()  # Fecha o navegador SEMPRE, com sucesso ou erro

    return livros

@app.route('/livros', methods=['GET'])
def get_livros():
    try:
        livros = coletar_livros()
        return jsonify(livros)
    except Exception as e:
        return jsonify({
            "error": "Erro ao carregar livros",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
# O código acima é um exemplo de uma API Flask que coleta informações de livros de um site usando Selenium.