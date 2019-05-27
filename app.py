from flask import Flask, jsonify
from usuario_api import usuario_app
from mensagen_api import mensagem_app
from infra.to_dict import to_dict, to_dict_list
from infra.db import criar_db

app = Flask(__name__)
app.register_blueprint(usuario_app)
app.register_blueprint(mensagem_app)
app.debug = 1

@app.route('/')
def all():
    from services.usuario_services import listar as listar_usuario
    database = {
        "USUARIOS": to_dict_list(listar_usuario())
    }
    return jsonify(to_dict(database))


criar_db()

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
