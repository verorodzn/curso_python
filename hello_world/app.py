''' Hola mundo en Flask '''
from flask import Flask
app = Flask(__name__)

@app.route('/') # Home Page o raíz o índice
def index():
    return '''<html>
                    <head>
                        <title>Hello World</title>
                        <body>
                            <h1>Hello World</h1>
                            <p> Ir a la página de <a href="/about">About</a></p>
                        </body>
            </html>'''

def about():
    return '''<html>
                    <head>
                        <title>About</title>
                        <body>
                            <h1>About</h1>
                            <p> Ir a la página de <a href="/index">Inicio</a></p>
                        </body>
            </html>'''

if __name__ == '__main__':
    app.run(debug=True) # Activar el modo de depuración/debug