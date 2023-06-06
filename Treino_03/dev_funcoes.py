import sqlite3

def banco_versao_inicial():
	import sqlite3
	conexao = sqlite3.connect("Banco.sqlite3")
	cursor = conexao.cursor()

	sql = """
	CREATE TABLE IF NOT EXISTS categoria (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100)
	);
	"""
	cursor.execute(sql)

	sql = """
	CREATE TABLE IF NOT EXISTS produtos (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		nome TEXT(100)
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
	sql = f"""
    CREATE TABLE IF NOT EXISTS {nome_da_tabela}(
        id INTEGER PRIMARY KEY AUTOINCREMENT
    );
    """
	cursor.execute(sql)
	conexao.commit()

def deleta_tabela(conexao):
	cursor = conexao.cursor()
	tabela = input('Digite o nome da tabela que deseja deletar:')
	sql = f"DROP TABLE {tabela}"
	cursor.execute(sql)
	conexao.commit()