import sqlite3

def banco_versao_inicial():
	import sqlite3
	conexao = sqlite3.connect("db.sqlite3")
	cursor = conexao.cursor()

	sql = """
	CREATE TABLE IF NOT EXISTS usuario (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100)
	);
	"""
	cursor.execute(sql)
		
	sql = """
	CREATE TABLE IF NOT EXISTS fornecedor (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100) NOT NULL,
		email TEXT(100),
		telefone TEXT(20) NOT NULL,
		nota INTEGER NOT NULL
	);
	"""
	cursor.execute(sql)

	sql = """
	CREATE TABLE IF NOT EXISTS categoria (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100) NOT NULL
	);
	"""
	cursor.execute(sql)

	sql = """
	CREATE TABLE IF NOT EXISTS produto (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100) NOT NULL,
		descricao TEXT(250),
		preco REAL
	);
	"""
	cursor.execute(sql)

	sql = """
	CREATE TABLE IF NOT EXISTS categoria_produto(
		categoria_id INTEGER,
		produto_id INTEGER,
			FOREIGN KEY (categoria_id) REFERENCES categoria(id),
			FOREIGN KEY (produto_id) REFERENCES produto(id),
	CONSTRAINT pk_categoria_produto PRIMARY KEY (categoria_id, produto_id)
	);
	"""
	cursor.execute(sql)

	conexao.commit()
	conexao.close()

def cria_tabela(conexao):
	cursor = conexao.cursor()
	nome_da_tabela = input('Digite o nome da nova tabela:')
	sql = f"CREATE TABLE IF NOT EXISTS {nome_da_tabela}(id INTEGER PRIMARY KEY AUTOINCREMENT);"
	cursor.execute(sql)
	conexao.commit()
	while True:
		add_coluna = input('Adicionar coluna: S / N: ')
		if add_coluna == 's' or 'S':
			coluna = input("""
			Digite o nome da coluna e suas características:
				Por exemplo a coluna id:
					id INTEGER PRIMARY KEY AUTOINCREMENT
			OBS.: COLUNA id JÁ EXISTE POR PADRÃO!
			""")
			sql = f"ALTER TABLE {nome_da_tabela} ADD COLUMN {coluna};"
			cursor.execute(sql)
			conexao.commit()

		elif add_coluna == 'n' or 'N':
			break
			
		else:
			print('Opção inválida! Para continuar digite: S ou N!')

def deleta_tabela(conexao):
	cursor = conexao.cursor()
	tabela = input('Digite o nome da tabela que deseja deletar:')
	sql = f"DROP TABLE {tabela}"
	cursor.execute(sql)
	conexao.commit()

def atera_nome_da_tabela(conexao):
	cursor = conexao.cursor()
	nome_atual = input('Digite o nome da tabela que deseja alterar:')
	novo_nome = input('Digite o novo nome da tabela:')
	sql = f"ALTER TABLE {nome_atual} RENAME TO {novo_nome};"
	cursor.execute(sql)
	conexao.commit()
	print(f"O nome foi alterado com sucesso de: {nome_atual} para: {novo_nome}")

def altera_nome_da_coluna(conexao):
	cursor = conexao.cursor()
	tabela = input('Digite o nome da tabela que deseja alterar:')
	nome_atual = input('Digite o nome atual da coluna:')
	novo_nome = input('Digite o novo nome da coluna:')
	sql = f"ALTER TABLE {tabela} RENAME COLUMN {nome_atual} TO {novo_nome};"
	cursor.execute(sql)
	conexao.commit()
	print(f"O nome foi alterado com sucesso de: {nome_atual} para: {novo_nome}")
