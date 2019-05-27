from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
from infra.verifica_segredo import verifica_segredo
from services.usuario_services import localizar as localizar_usuario_dao
from services.mensagem_services import \
    criar as service_criar, \
    localizar as service_localizar, \
    SegredosNaoCoincidem, \
    UsuarioRemetenteNaoExiste, \
    UsuarioDestinatarioNaoExiste

mensagem_app = Blueprint('mensagem_app', __name__, template_folder='templates')

campos_post = ["de", "para", "segredo", "texto"]
tipos_post = [int, int, str, str]
campos_get = ['segredo', 'inicio', 'fim']
tipos_get = [str, int, int]


@mensagem_app.route("/msg", methods=['POST'])
def nova_msg():
    dados = request.get_json()
    if not validar_campos(dados, campos_post, tipos_post):
        return '', 422
    try:
        criado = service_criar(**dados)
        return jsonify(to_dict(criado))
    except SegredosNaoCoincidem:
        return '', 403
    except UsuarioDestinatarioNaoExiste:
        return '', 404
    except UsuarioRemetenteNaoExiste:
        return '', 404


@mensagem_app.route('/msg/<int:id_usuario>', methods=['GET'])
def localiza_msg(id_usuario):
    segredo = request.args.get("segredo")
    inicio = request.args.get("inicio")
    fim = request.args.get("fim")
    segredo_verificado = verifica_segredo(id_usuario, segredo)
    if not segredo_verificado:
        return '', 403
    if segredo is None and type(segredo) is not str:
        return '', 422
    if inicio is not None and fim is not None:
        if not validar_campos({"segredo": segredo, "inicio": inicio, "fim": fim}, campos_get, tipos_get):
            return '', 422
    lista = service_localizar(id_usuario, inicio, fim)
    return jsonify(lista)