from infra.db import con
from wrap_connection import transact

sql_criar = "INSERT INTO Mensagens (id_remetente, id_destinatario, data_hora, texto) VALUES (?, ?, ?, ?)"
sql_localizar_inicio_fim = "SELECT id_remetente, id_destinatario, data_hora, texto FROM Mensagens WHERE id in (?, ?) and id_destinatario = (?)"
localiza_msg_dest = "SELECT id_remetente, id_destinatario, data_hora, texto FROM Mensagens WHERE id_destinatario = (?)"
sql_localizar_msg = "SELECT id, data_hora FROM Mensagens WHERE id = (?)"


@transact(con)
def criar(msg):
    cursor.execute(sql_criar, (msg.id_remetente, msg.id_destinatario, msg.datetime, msg.texto))
    connection.commit()
    created = cursor.lastrowid
    return created


@transact(con)
def localiza_msg_destinatario(id_usuario, inicio, fim):
    if inicio is not None and fim is not None:
        mensagens = {'mensagens': []}
        cursor.execute(sql_localizar_inicio_fim, (inicio, fim, id_usuario))
        t = cursor.fetchall()
        if t is None:
            return None
        for x in t:
            mensagens['mensagens'].append({"de": x[0], "para": x[1], "datahora": x[2], "texto": x[3]})
        return mensagens
    else:
        mensagens = {'mensagens': []}
        cursor.execute(localiza_msg_dest, (id_usuario,))
        t = cursor.fetchall()
        if t is None:
            return None
        for x in t:
            mensagens['mensagens'].append({"de": x[0], "para": x[1], "datahora": x[2], "texto": x[3]})
        return mensagens


@transact(con)
def localiza_msg(id_msg):
    cursor.execute(sql_localizar_msg, (id_msg,))
    t = cursor.fetchone()
    if t is None:
        return None
    return {"id": t[0], "datahora": t[1]}