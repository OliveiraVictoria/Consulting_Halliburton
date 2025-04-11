import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def buscar_livros(query):
    resultados = {}

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)

    try:
        # Submarino
        driver.get(f"https://www.submarino.com.br/busca/{query}")
        time.sleep(2)
        livros_submarino = []
        elementos = driver.find_elements(By.CSS_SELECTOR, 'h2.product-name')[:5]  # pegar os 5 primeiros
        for el in elementos:
            livros_submarino.append(el.text)
        resultados['Submarino'] = livros_submarino

        # Americanas
        driver.get(f"https://www.americanas.com.br/busca/{query}")
        time.sleep(2)
        livros_americanas = []
        elementos = driver.find_elements(By.CSS_SELECTOR, 'h2.product-name')[:5]
        for el in elementos:
            livros_americanas.append(el.text)
        resultados['Americanas'] = livros_americanas

        # Estante Virtual
        driver.get(f"https://www.estantevirtual.com.br/busca?q={query}")
        time.sleep(2)
        livros_estante = []
        elementos = driver.find_elements(By.CSS_SELECTOR, '.title')[:5]
        for el in elementos:
            livros_estante.append(el.text)
        resultados['Estante Virtual'] = livros_estante

    except Exception as e:
        print(f"Erro durante busca: {e}")
    finally:
        driver.quit()

    return resultados
