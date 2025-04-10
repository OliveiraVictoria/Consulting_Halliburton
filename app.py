from flask import Flask, jsonify, render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# configuração do selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/livros')
def livros():
    driver.get('https://books.toscrape.com/')
    livros = []
    livros_elements = driver.find_elements('css selector', 'article.product_pod')

    for livro in livros_elements:
        titulo = livro.find_element('css selector', 'h3 a').get_attribute('title')
        preco_element = livro.find_element('css selector', '.price_color')
        preco_texto = preco_element.text
        preco_float = float(preco_texto.replace('£', ''))
        preco = f'R$ {preco_float * 6.5:.2f}'
        livros.append({'titulo': titulo, 'preco': preco})

    return jsonify(livros)

if __name__ == '__main__':
    app.run(debug=True)
# O código acima é um exemplo de uma API Flask que coleta informações de livros de um site usando Selenium.