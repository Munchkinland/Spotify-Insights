from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola, Mundo!'

@app.route('/hello')
def hello():
    return '¡Hola desde /hello!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

