import sqlite3

conn = sqlite3.connect('todo-app.db')

def criar_tabela_todo():
    """" cria a tabela 'tarefa`caso ela não exista """
    cursor = conn.cursor()
    conn.execute("""
    create table if not exists tarefa (
        cd_tarefa integer primary key autoincrement,
        tarefa text,
        concluido integer
    )
    """)

def add_tarefa(tarefa): # CREATE
    """" adiciona uma nova tarefa """
    conn.execute(
        "insert into tarefa (tarefa, concluido) values (?, 0)", (tarefa, ))
    conn.commit()

def remover_tarefa(cd_tarefa): # DELETE
    """" remove uma tarefa """
    conn.execute("delete from tarefa where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()

def concluir_tarefa(cd_tarefa): # UPDATE
    """ marca a tarefa como concluida """
    conn.execute("update tarefa set concluido = 1 where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()

def get_tarefas(): # READ
    """ retorna a lista de tarefas cadatradas """
    return conn.execute("select cd_tarefa, tarefa, concluido from tarefa") # retorna um cursor

# def editar_tarefa(cd_tarefa, tarefa):
#     """" edita uma tarefa existente """
#     conn.execute(
#         "uppdate from "
#     )
#     conn.commit()