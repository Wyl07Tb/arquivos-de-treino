import sqlite3

def inserir_produto():
    conexao = sqlite3.connect("Banco.sqlite3")
    cursor = conexao.cursor()

    nome = input("Digite o nome do produto: ")

    sql = 'SELECT id, nome FROM categoria'
    categorias = cursor.execute(sql)
    print("Categorias disponíveis:")
    for categoria in categorias:
        print("ID:", categoria[0], "Categoria:", categoria[1])

    categoria_id = input("Digite o 'ID' da categoria referente ao produto: ")

    sql = 'INSERT INTO produtos (nome,categoria_id) VALUES (?, ?)'
    valores = [nome,categoria_id]
    cursor.execute(sql,valores)

    conexao.commit()
    print('Produto inserido com SUCESSO!')
    conexao.close()