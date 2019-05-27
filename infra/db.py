from wrap_connection import transact
import sqlite3

create_usuario = """CREATE TABLE IF NOT EXISTS Usuario
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome varchar (50),
segredo varchar (11)
)"""

create_mensagens = """CREATE TABLE IF NOT EXISTS Mensagens
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
id_remetente INTEGER NOT NULL,
id_destinatario INTEGER NOT NULL,
data_hora DATETIME,
texto varchar (200),
FOREIGN KEY (id_remetente) REFERENCES Usuario(id_remetente),
FOREIGN KEY (id_destinatario) REFERENCES Usuario(id_destinatario)
)"""

tables = [create_usuario, create_mensagens]


def con():
    return sqlite3.connect("chat.db")


@transact(con)
def criar_db():
    for x in tables:
        cursor.execute(x)
