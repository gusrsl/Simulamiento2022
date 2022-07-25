from flask import Flask

server = Flask(__name__)

@server.route('/')
def hola():
    return 'Bienvenido Admin'

if __name__ == '__main__':
    server.run() 
    