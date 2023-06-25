from funcoes import *
import sqlite3

class Acesso_Nivel_3():
    def __init__(self):
        self.acesso = 5

    def menu_user_nivel(self):
        while True:
            print('Opções disponíveis para seu nível de acesso:')
            opcao = opcao_disponinel_por_nivel(self.acesso)
            if opcao == 0:
                break
            elif opcao == 1:
                mostra_tabela_categoria()
            elif opcao == 2:
                mostra_tabela_produto()
            elif opcao == 3:
                inseri_categoria()
            elif opcao == 4:
                inseri_produto()
            elif self.acesso > 5 and self.acesso < 8:
                if opcao == 5:
                    atualiza_categoria()
                elif opcao == 6:
                    atualiza_produto()
                else:
                    print('Opção invalida!')
            elif self.acesso > 7:
                if opcao == 7:
                    remove_categoria()
                elif opcao == 8:
                    remove_produto()
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