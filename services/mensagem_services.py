import datetime
from model.mensagem import Mensagem
from infra.log import Log
from services.usuario_services import localizar as localizar_usuario_dao
from dao.mensagens_dao import \
    criar as criar_dao, \
    localiza_msg as localiza_msg, \
    localiza_msg_destinatario as localiza_msg_destinatario


class SegredosNaoCoincidem(Exception):
    pass


class UsuarioRemetenteNaoExiste(Exception):
    pass


class UsuarioDestinatarioNaoExiste(Exception):
    pass


def localizar(id_usuario, inicio, fim):
    return localiza_msg_destinatario(id_usuario, inicio, fim)


def criar(de, para, segredo, texto):
    data = datetime.datetime.now()
    usuario_from = localizar_usuario_dao(None, de)
    usuario_to = localizar_usuario_dao(None, para)
    if usuario_from is None:
        raise UsuarioRemetenteNaoExiste()
    if usuario_to is None:
        raise UsuarioDestinatarioNaoExiste()
    if usuario_from["segredo"] != segredo:
        raise SegredosNaoCoincidem()
    log = Log(None)
    id_criado = criar_dao(Mensagem(None, de, para, data, texto))
    log.finalizar(Mensagem(id_criado, de, para, data, texto))
    criado = localiza_msg(id_criado)
    return criado





