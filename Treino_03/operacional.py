#Imports do programa e conexao do banco.
from funcoes import *
from dev_funcoes import *
import sqlite3
conexao = sqlite3.connect('Banco.sqlite3')
cursor = conexao.cursor()
#-------------------------------

#cria_tabela(conexao)
#deleta_tabela(conexao)
#mostra_tabela_categoria(conexao)3
#mostra_tabela_produto(conexao)
#atera_nome_da_tabela(conexao)

#-------------------------------
conexao.close()