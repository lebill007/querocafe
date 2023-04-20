from flask import Flask

app = Flask(__name__)

#rota para a pagina principal da aplicação
@app.route('/')
def start():
    return "quero café 2...5"

