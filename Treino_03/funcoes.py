import sqlite3

#Mostra o conteudo da tabela categori.
def mostra_tabela_categoria(conexao):
    cursor = conexao.cursor()
    sql = 'SELECT id, nome FROM categoria'
    categorias = cursor.execute(sql)
    print("Categorias disponíveis:")
    for categoria in categorias:
        print("ID:", categoria[0], "/Categoria:", categoria[1])
    conexao.commit()

#Mostra o conteudo da tabela produto.
def mostra_tabela_produto(conexao):
    cursor = conexao.cursor()
    sql = 'SELECT id, nome, categoria_id FROM produto'
    produto = cursor.execute(sql)
    print("Produtos disponíveis:")
    for produto in produto:
        print("ID:", produto[0], "/Produto:", produto[1], "/Categoria ID:", produto[2])
    conexao.commit()

#Define o menu interativo a mostrar de acordo com o nível do usuario.
def opcao_disponinel_por_nivel(acesso):
    opcao = ['0:Sair', '1:Visualizar as categorias', '2:Visualizar os produtos', 
    '3:Inserir categoria', '4:Inserir produto', '5:Atualizar categoria',
    '6:Atualizar produto', '7:Remover categoria', '8:Remover produto']
    
    for opcao in opcao[0:acesso]:
                print(opcao)
    
    selecao = int(input('Digite a opção dezejada:'))
    return selecao

#Menu interativo usuario nivel_01.
def menu_user_nivel01(conexao):
    while True:
        print('Opções disponíveis para seu nível de acesso:')
        opcao = opcao_disponinel_por_nivel(9)
        if opcao == 0:
            break
        elif opcao == 1:
            mostra_tabela_categoria(conexao)
        elif opcao == 2:
            mostra_tabela_produto(conexao)
        elif opcao == 3:
            inseri_categoria(conexao)
        elif opcao == 4:
            inseri_produto(conexao)
        elif opcao == 5:
            atualiza_categoria(conexao)
        elif opcao == 6:
            atualiza_produto(conexao)
        elif opcao == 7:
            remove_categoria(conexao)
        elif opcao == 8:
            remove_produto(conexao)
        else:
            print('Opção invalida!')

#Menu interativo usuario nivel_02.
def menu_user_nivel02(conexao):
    while True:
        print('Opções disponíveis para seu nível de acesso:')
        opcao = opcao_disponinel_por_nivel(7)
        if opcao == 0:
            break
        elif opcao == 1:
            mostra_tabela_categoria(conexao)
        elif opcao == 2:
            mostra_tabela_produto(conexao)
        elif opcao == 3:
            inseri_categoria(conexao)
        elif opcao == 4:
            inseri_produto(conexao)
        elif opcao == 5:
            atualiza_categoria(conexao)
        elif opcao == 6:
            atualiza_produto(conexao)
#        elif opcao == 7:
#            remove_categoria(conexao)
#        elif opcao == 8:
#            remove_produto(conexao)
        else:
            print('Opção invalida!')

#Menu interativo usuario nivel_03.
def menu_user_nivel03(conexao):
    while True:
        print('Opções disponíveis para seu nível de acesso:')
        opcao = opcao_disponinel_por_nivel(9)
        if opcao == 0:
            break
        elif opcao == 1:
            mostra_tabela_categoria(conexao)
        elif opcao == 2:
            mostra_tabela_produto(conexao)
        elif opcao == 3:
            inseri_categoria(conexao)
        elif opcao == 4:
            inseri_produto(conexao)
#        elif opcao == 5:
#            atualiza_categoria(conexao)
#        elif opcao == 6:
#            atualiza_produto(conexao)
#        elif opcao == 7:
#            remove_categoria(conexao)
#        elif opcao == 8:
#            remove_produto(conexao)
        else:
            print('Opção invalida!')

#Inseri uma categoria.
def inseri_categoria(conexao):
    cursor = conexao.cursor()

    nome = input("Digite o nome da categoria: ")

    sql = 'INSERT INTO categoria(nome) VALUES(?)'
    valores = [nome]
    cursor.execute(sql,valores)

    conexao.commit()
    print('Categoria inserida com SUCESSO!')

#Atualiza uma categoria.
def atualiza_categoria(conexao):    
    cursor = conexao.cursor()

    mostra_tabela_categoria(conexao)

    categoria_id = input("Digite o ID da categoria que deseja atualizar: ")

    nome = input('Digite o novo nome da categoria: ')

    sql = 'UPDATE categoria SET nome = ? WHERE id = ?'
    valores = [nome, categoria_id]
    cursor.execute(sql, valores)

    conexao.commit()
    print('Categoria atualizada com SUCESSO!')

#Remove uma categoia
def remove_categoria(conexao):
    cursor = conexao.cursor()

    sql = 'SELECT id, nome FROM categoria'
    categorias = cursor.execute(sql)
    print("Categorias disponíveis:")
    for categoria in categorias:
        print("ID:", categoria[0], "/Categoria:", categoria[1])

    categoria_id = input("Digite o ID da categoria que deseja remover: ")

    sql = 'DELETE FROM categoria WHERE id = ?'
    valores = [categoria_id]
    cursor.execute(sql, valores)

    conexao.commit()
    print('Categoria removida com SUCESSO!')

#Inseri um produto.
def inseri_produto(conexao):
    cursor = conexao.cursor()

    nome = input("Digite o nome do produto: ")

    sql = 'SELECT id, nome FROM categoria'
    categorias = cursor.execute(sql)
    print("Categorias disponíveis:")
    for categoria in categorias:
        print("ID:", categoria[0], "Categoria:", categoria[1])

    categoria_id = input("Digite o 'ID' da categoria referente ao produto: ")

    sql = 'INSERT INTO produto (nome,categoria_id) VALUES (?, ?)'
    valores = [nome,categoria_id]
    cursor.execute(sql,valores)

    conexao.commit()
    print('Produto inserido com SUCESSO!')

#Atualiza um produto
def atualiza_produto(conexao):
    cursor = conexao.cursor()

    mostra_tabela_produto(conexao)

    produto_id = input("Digite o ID do produto que deseja atualizar: ")

    nome = input('Digite o novo nome do produto: ')
    categoria_id = input('Digite o ID da nova categoria: ')

    sql = 'UPDATE produtos SET nome = ?, categoria_id = ? WHERE id = ?'
    valores = [nome, categoria_id, produto_id]
    cursor.execute(sql, valores)

    conexao.commit()
    print('Produto atualizado com SUCESSO!')

#Remove um produto.
def remove_produto(conexao):
    cursor = conexao.cursor()

    sql = 'SELECT id, nome, categoria_id FROM produtos'
    produtos = cursor.execute(sql)
    print("Produtos disponíveis:")
    for produto in produtos:
        print("ID:", produto[0], "/Produto:", produto[1], "/Categoria ID:", produto[2])

    produto_id = input("Digite o ID do produto que deseja remover: ")

    sql = 'DELETE FROM produtos WHERE id = ?'
    valores = [produto_id]
    cursor.execute(sql, valores)

    conexao.commit()
    print('Produto removido com SUCESSO!')