# criando uma aplicação web 01
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'pagina principal'

@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):
    return 'ola, ' + nome

if __name__ == '__main__':
    app.run()
