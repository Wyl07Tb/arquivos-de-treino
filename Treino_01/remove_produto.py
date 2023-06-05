import sqlite3
conexao = sqlite3.connect('Banco.sqlite3')
cursor = conexao.cursor()

sql = 'SELECT id, nome, categoria_id FROM produtos'
produtos = cursor.execute(sql)
print("Produtos disponíveis:")
for produto in produtos:
    print("ID:", produto[0], "/Produto:", produto[1], "/Categoria ID:", produto[2])

produto_id = input("Digite o ID do produto que deseja remover: ")

sql = 'DELETE FROM produtos WHERE id = ?'
valores = [produto_id]
cursor.execute(sql, valores)

conexao.commit()
print('Produto removido com SUCESSO!')
conexao.close()