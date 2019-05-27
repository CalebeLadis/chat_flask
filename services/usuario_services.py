from model.usuario import Usuario
from infra.log import Log
from infra.criar_segredo import randomString
from dao.usuario_dao import \
    criar as criar_dao, \
    listar as listar_dao, \
    localizar as localizar_dao


class LoginJaExitente(Exception):
    pass


def listar():
    return listar_dao()


def localizar(nome, id_usuario):
    return localizar_dao(nome, id_usuario)


def criar(nome):
    if localizar_dao(nome, '') is not None:
        raise LoginJaExitente()
    segredo = randomString()
    log = Log(None)
    criado = Usuario(None, nome, segredo)
    criar_dao(criado)
    log.finalizar(criado)
    criado = localizar(nome, None)
    return criado

