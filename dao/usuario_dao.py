from infra.db import con
from wrap_connection import transact
from model.usuario import Usuario

sql_criar = "INSERT INTO Usuario (nome, segredo) VALUES (?, ?)"
sql_localizar_com_id = "SELECT * FROM Usuario WHERE nome = ? or id = ?"
sql_localizar = "SELECT * FROM Usuario WHERE nome = ?"
sql_listar = "SELECT id, nome FROM Usuario"


@transact(con)
def criar(user):
    cursor.execute(sql_criar, (user.nome, user.segredo))
    connection.commit()


@transact(con)
def listar():
    cursor.execute(sql_listar)
    resultado = {"usr":[]}
    for p in cursor.fetchall():
        resultado["usr"].append({"id": p[0], "nome": p[1]})
    return resultado


@transact(con)
def localizar(nome, id_usuario):
    if id_usuario is not None:
        cursor.execute(sql_localizar_com_id, (nome, id_usuario))
    else:
        cursor.execute(sql_localizar, (nome,))
    t = cursor.fetchone()
    if t is None:
        return None
    return {"id": t[1], "segredo": t[2]}
