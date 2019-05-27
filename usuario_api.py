from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import  to_dict, to_dict_list
from services.usuario_services import \
    listar as sercive_listar, \
    localizar as service_localizar, \
    criar as service_criar, \
    LoginJaExitente

usuario_app = Blueprint('usuario_app', __name__, template_folder='templates')

campos = ["nome"]
tipos = [str]


@usuario_app.route('/usr', methods=['GET'])
def usuario():
    lista = sercive_listar()
    return jsonify(lista)


@usuario_app.route('/usr', methods=['POST'])
def novo_usuario():
    dados = request.get_json()
    if not validar_campos(dados, campos, tipos):
        return '', 422
    try:
        criado = service_criar(**dados)
        return jsonify(to_dict(criado))
    except LoginJaExitente:
        return '', 409

@usuario_app.route('/usr/<string:login>', methods=['GET'])
def localiza_aluno(login):
        x = service_localizar(login)
        if x is not None:
                return jsonify(to_dict(x))
        return jsonify(x)
