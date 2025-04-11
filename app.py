from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        termo_busca = request.form['termo']
        # aqui você faz a lógica de busca usando o termo
        print(f"Usuário buscou por: {termo_busca}")
        # você pode redirecionar ou mostrar os resultados depois
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
# O código acima é um exemplo básico de uma aplicação Flask que renderiza um formulário e processa a busca do usuário.
# O arquivo HTML (index.html) deve estar na pasta templates e conter um formulário para o usuário inserir o termo de busca.