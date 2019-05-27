from services.usuario_services import localizar as localizar_dao


def verifica_segredo(id_usuario, segredo):
    usuario = localizar_dao(None, id_usuario)
    if usuario['segredo'] != segredo:
        return False
    else:
        return True