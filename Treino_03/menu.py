#Imports do programa e conexao do banco.
from funcoes import *
from dev_funcoes import *
import sqlite3
conexao = sqlite3.connect('Banco.sqlite3')
cursor = conexao.cursor
conexao.execute('ALTER TABLE produtos DROP COLUMN categoria_id')

