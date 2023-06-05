import sqlite3
conexao = sqlite3.connect('Banco.sqlite3')
cursor = conexao.cursor()

sql = 'SELECT id, nome, categoria_id FROM produtos'
produtos = cursor.execute(sql)
print("Produtos disponíveis:")
for produto in produtos:
    print("ID:", produto[0], "/Produto:", produto[1], "/Categoria ID:", produto[2])

produto_id = input("Digite o ID do produto que deseja atualizar: ")

nome = input('Digite o novo nome do produto: ')
categoria_id = input('Digite o ID da nova categoria: ')

sql = 'UPDATE produtos SET nome = ?, categoria_id = ? WHERE id = ?'
valores = [nome, categoria_id, produto_id]
cursor.execute(sql, valores)

conexao.commit()
print('Produto atualizado com SUCESSO!')
conexao.close()