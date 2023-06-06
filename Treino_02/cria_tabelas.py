import sqlite3
conexao = sqlite3.connect("Banco.sqlite3")
cursor = conexao.cursor()
#######################################################################################
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
	nome TEXT(100),
    categoria_id INTEGER,
		FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);
"""
cursor.execute(sql)

sql = """
CREATE TABLE IF NOT EXISTS categoria_produtos(
	categoria_id INTEGER,
	produto_id INTEGER,
		FOREIGN KEY (categoria_id) REFERENCES categoria(id),
		FOREIGN KEY (produto_id) REFERENCES produtos(id),
CONSTRAINT pk_categoria_produto PRIMARY KEY (categoria_id, produto_id)
);
"""
cursor.execute(sql)

#######################################################################################
conexao.commit()
conexao.close()