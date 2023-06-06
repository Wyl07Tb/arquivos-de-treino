from inserir_categoria import *
from inserir_produto import *
from atualiza_categoria import *
from atualiza_produto import *
from remove_categoria import *
from remove_produto import *

while True:
    print('''
    0) Sair;
    1) Inserir categoria;
    2) Inserir produto;
    3) Atualizar categoria;
    4) Atualizar produto;
    5) Remover categoria;
    6) Remover produto.
    ''')
    opcao = int(input('Digite a opção desejada:'))
    if opcao == 0:
        break
    elif opcao == 1:
        inserir_categoria()
    elif opcao == 2:
        inserir_produto()
    elif opcao == 3:
        atualiza_categoria()
    elif opcao == 4:
        atualiza_produto()
    elif opcao == 5:
        remove_categoria()
    elif opcao == 6:
        remove_produto()
    else:
        print('Opção invalida!')