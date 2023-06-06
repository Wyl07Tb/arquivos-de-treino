import sqlite3

def inserir_categoria():
    conexao = sqlite3.connect("Banco.sqlite3")
    cursor = conexao.cursor()

    nome = input("Digite o nome da categoria: ")

    sql = 'INSERT INTO categoria(nome) VALUES(?)'
    valores = [nome]
    cursor.execute(sql,valores)

    conexao.commit()
    print('Categoria inserida com SUCESSO!')
    conexao.close()