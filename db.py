import sqlite3

# conecta ao banco de dados 'todo-app'
# caso o banco não exista ele será criado
conn = sqlite3.connect("todo-app.db")

def criar_tabela_todo():
    """ cria a tabela 'usuario' caso ela não exista """
    cursor = conn.cursor()
    conn.execute("""
    create table if not exists usuario (
        cd_usuario integer primary key autoincrement,
        usuario text,
        concluido integer
    )
    """)

def add_usuario(usuario):
    """ adiciona uma nova usuario """
    conn.execute("insert into usuario (usuario, concluido) values (?, 0)", (usuario, ))
    conn.commit()

def remover_usuario(cd_usuario):
    """ remove a usuario da tabela """
    conn.execute("delete from usuario where cd_usuario = ?", (cd_usuario, ))
    conn.commit()

def concluir_usuario(cd_usuario):
    """ marca a usuario como concluida """
    conn.execute("update usuario set concluido = 1 where cd_usuario = ?", (cd_usuario, ))
    conn.commit()

def get_usuarios(): # retorna um cursor
    """ retorna a lista de usuarios cadastras """
    return conn.execute("select cd_usuario, usuario, concluido from usuario")