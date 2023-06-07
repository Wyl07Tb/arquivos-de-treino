#Imports do programa e conexao do banco.
from funcoes import *
from dev_funcoes import *
import sqlite3
conexao = sqlite3.connect('Banco.sqlite3')
cursor = conexao.cursor()
#-------------------------------
menu_user_nivel01(conexao)
#-------------------------------
conexao.close()

#-------------------------------

