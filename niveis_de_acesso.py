from funcoes import *
import sqlite3

class Acesso_Nivel_3():
    def __init__(self):
        self.acesso = 5
        self.conexao = abre_conexao('db.sqlite3')

    def menu_user_nivel(self):
        while True:
            print('Opções disponíveis para seu nível de acesso:')
            opcao = opcao_disponinel_por_nivel(self.acesso)
            if opcao == 0:
                break
            elif opcao == 1:
                mostra_tabela_categoria(self.conexao)
            elif opcao == 2:
                mostra_tabela_produto(self.conexao)
            elif opcao == 3:
                inseri_categoria(self.conexao)
            elif opcao == 4:
                inseri_produto(self.conexao)
            elif self.acesso > 5 and self.acesso < 8:
                if opcao == 5:
                    atualiza_categoria(self.conexao)
                elif opcao == 6:
                    atualiza_produto(self.conexao)
                else:
                    print('Opção invalida!')
            elif self.acesso > 7:
                if opcao == 7:
                    remove_categoria(self.conexao)
                elif opcao == 8:
                    remove_produto(self.conexao)
                else:
                    print('Opção invalida!')
            else:
                print('Opção invalida!')

class Acesso_Nivel_2(Acesso_Nivel_3):
    def __init__(self):
        super().__init__()
        self.acesso = 7
       
class Acesso_Nivel_1(Acesso_Nivel_3):
    def __init__(self):
        super().__init__()
        self.acesso = 9