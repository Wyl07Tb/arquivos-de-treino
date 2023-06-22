import sqlite3
conexao = sqlite3.connect("db.sqlite3")
cursor = conexao.cursor()

print('''---------------------------
--------BEM-VINDO(A)--------
----------------------------
[1] Criar Tabela
[2] Excluir Tabela
[3] Alterar nome Tabela
[4] Alterar nome Coluna
[5] Sair
''')
opcao = input()

sql_usuario = """
	CREATE TABLE IF NOT EXISTS usuario (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100)
	);
	"""
cursor.execute(sql_usuario)
		
sql_fornecedor = """
	CREATE TABLE IF NOT EXISTS fornecedor (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100) NOT NULL,
		email TEXT(100),
		telefone TEXT(20) NOT NULL,
		nota INTEGER NOT NULL
	);
	"""
cursor.execute(sql_fornecedor)

sql_categoria = """
	CREATE TABLE IF NOT EXISTS categoria (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100) NOT NULL
	);
	"""
cursor.execute(sql_categoria)

sql_produto = """
	CREATE TABLE IF NOT EXISTS produto (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100) NOT NULL,
		descricao TEXT(250),
		preco REAL
	);
	"""
cursor.execute(sql_produto)

sql_cat_prod = """
	CREATE TABLE IF NOT EXISTS categoria_produto(
		categoria_id INTEGER,
		produto_id INTEGER,
			FOREIGN KEY (categoria_id) REFERENCES categoria(id),
			FOREIGN KEY (produto_id) REFERENCES produto(id),
	CONSTRAINT pk_categoria_produto PRIMARY KEY (categoria_id, produto_id)
	);
	"""
cursor.execute(sql_cat_prod)

def criar_tabela():



#	nome_da_tabela = str(input('Digite o nome da nova tabela:'))
#	sql = f"CREATE TABLE IF NOT EXISTS {nome_da_tabela}(id INTEGER PRIMARY KEY AUTOINCREMENT);"
#	cursor.execute(sql)
#	while True:
#		add_coluna = str(input('Adicionar coluna: S / N: '))
#		if add_coluna == 's' or 'S':
#			coluna = str(input("""
#			Digite o nome da coluna e suas características:
#				Por exemplo a coluna id:
#					id INTEGER PRIMARY KEY AUTOINCREMENT
#			OBS.: COLUNA id JÁ EXISTE POR PADRÃO!
#			"""))
#			sql1 = f"ALTER TABLE {nome_da_tabela} ADD COLUMN {coluna};"
#			cursor.execute(sql1)
#
#		elif add_coluna == 'n' or 'N':
#			break
#			
#		else:
#			print('Opção inválida! Para continuar digite: S ou N!')#
	return criar_tabela

def deleta_tabela():
	tabela = input('Digite o nome da tabela que deseja deletar:')
	sql = f"DROP TABLE {tabela}"
	cursor.execute(sql)
	return deleta_tabela

def atualizar_nome_tabela():
	nome_atual = input('Digite o nome da tabela que deseja alterar:')
	novo_nome = input('Digite o novo nome da tabela:')
	sql = f"ALTER TABLE {nome_atual} RENAME TO {novo_nome};"
	cursor.execute(sql)

	print(f"O nome foi alterado com sucesso de: {nome_atual} para: {novo_nome}")
	

def atualizar_nome_coluna():
	tabela = input('Digite o nome da tabela que deseja alterar:')
	nome_atual = input('Digite o nome atual da coluna:')
	novo_nome = input('Digite o novo nome da coluna:')
	sql = f"ALTER TABLE {tabela} RENAME COLUMN {nome_atual} TO {novo_nome};"
	cursor.execute(sql)
	print(f"O nome foi alterado com sucesso de: {nome_atual} para: {novo_nome}")

if opcao == 1:
	criar_tabela()
if opcao == 2:
	deleta_tabela()
if opcao == 3:
	atualizar_nome_tabela()
if opcao == 4:
	atualizar_nome_coluna
if opcao == 5:
	quit()

conexao.commit()
conexao.close()