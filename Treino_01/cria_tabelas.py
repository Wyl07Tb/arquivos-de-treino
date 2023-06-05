import sqlite3
conexao = sqlite3.connect("Banco.sqlite3")
cursor = conexao.cursor()
#######################################################################################
sql = """
CREATE TABLE categoria (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100)
);
 """
cursor.execute(sql)

sql = """
CREATE TABLE produtos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT(100),
	categoria_id INTEGER,
	CONSTRAINT produtos_FK FOREIGN KEY (categoria_id) REFERENCES categoria(id)
);
"""
cursor.execute(sql)
#######################################################################################
conexao.commit()
conexao.close()