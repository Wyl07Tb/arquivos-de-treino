import sqlite3

def remove_categoria():
    conexao = sqlite3.connect('Banco.sqlite3')
    cursor = conexao.cursor()

    sql = 'SELECT id, nome FROM categoria'
    categorias = cursor.execute(sql)
    print("Categorias disponíveis:")
    for categoria in categorias:
        print("ID:", categoria[0], "/Categoria:", categoria[1])

    categoria_id = input("Digite o ID da categoria que deseja remover: ")

    sql = 'DELETE FROM categoria WHERE id = ?'
    valores = [categoria_id]
    cursor.execute(sql, valores)

    conexao.commit()
    print('Categoria removida com SUCESSO!')
    conexao.close()