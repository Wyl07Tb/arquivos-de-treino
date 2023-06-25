#Imports do programa e conexao do banco.
from funcoes import *
from dev_funcoes import *
from niveis_de_acesso import *
import sqlite3
conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()
#-------------------------------

#cria_tabela(conexao)
#deleta_tabela(conexao)
#mostra_tabela_categoria(conexao)3
#mostra_tabela_produto(conexao)
#atera_nome_da_tabela(conexao)

#-------------------------------
conexao.close()