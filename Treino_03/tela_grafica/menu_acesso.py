import  PySimpleGUI as sg
import requests
# Layout

# Configuração do Layout Login (linhas e colunas)
def Login():
    # Tema do PySimpleGUI
    sg.theme('Reddit')
    layout1 = [
        # linha de dados de usuário
        [sg.Text('Usuário'), sg.Input(key ='Usuário', size = (20,15))],
        # linha de senha de usuário
        [sg.Text('Senha', size = (5,1)), sg.Input(key  ='Senha', password_char='*', size = (20,15))],
        # linha de login
        [sg.Button('Entrar')]
    ]
    return  sg.Window('Login', layout1, finalize= True)

# Configuração do Layout Acesso 01
def Operacional():
    # Tema do PySimpleGUI
    sg.theme('Reddit')
    layout2 = [
        # Vizualização
        [sg.Text('[1] Vizualizar Categorias', size = (40,1))],
        [sg.Text('[2] Vizualizar Produtos')],
        # Criação
        [sg.Text('[3] Nova Categoria')],
        [sg.Text('[4] Novo Produto')],
        # Alteração
        [sg.Text('[5] Alterar Categoria')],
        [sg.Text('[6] Alterar Produto')],
        # Exclusão
        [sg.Text('[7] Excluir Categoria')],
        [sg.Text('[8] Excluir Produto', size = (40,2))],
        [sg.Text('Selecionar:', size = (30,1)), sg.Input(key ='Opção', size = (2,2))],
        [sg.Button('Voltar', size = (20,1)), sg.Button('Avançar', size = (20,1))]
    ]
    return sg.Window('Bem-Vindo', layout2, finalize= True)

# Configuração Layout Tela de Vizualização
def Tabela_Cat():
    sg.theme('Reddit')
    layout3 = [
        # Print de dados
        []

    ]

# Configuração Acesso 02
#def Supervisor():
    # Tema do PySimpleGUI
#    sg.theme('Reddit')
#    layout3 = [
        
        # Vizualização
#        [sg.Text('[1] Vizualizar Categorias', size = (40,1))],
#        [sg.Text('[2] Vizualizar Produtos')],
        # Criação
#        [sg.Text('[3] Nova Categoria')],
#        [sg.Text('[4] Novo Produto')],
        # Alteração
#        [sg.Text('[5] Alterar Categoria')],
#        [sg.Text('[6] Alterar Produto')],
        # Exclusão
#        [sg.Text('[7] Excluir Categoria')],
#        [sg.Text('[8] Excluir Produto')],
        
#        [sg.Text('Selecionar:'), sg.Input(key ='Opção', size = (2,2))],
#        [sg.Button('Voltar', size = (10,1)), sg.Button('Avançar', size = (10,1))]
#    ]
#    return sg.Window('Bem-Vindo', layout3, finalize= True)

#Janela
# Criação da janela
janela, janela2 = Login(), None
#Ler os Eventos
while True:
    window, eventos, valores = sg.read_all_windows()
    if window == janela and eventos == sg.WINDOW_CLOSED:
        print('Programa encerrado')
        break
    if window == janela2 and eventos == sg.WINDOW_CLOSED:
        print('Programa encerrado')
        break
    if window == janela and eventos == 'Entrar':
        if valores['Usuário'] == 'admin' and valores['Senha'] == '123456':
            print('Login Concluido')
            janela2 = Operacional()
            janela.hide()

    if window == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela.un_hide()
    if window == janela2 and eventos == 'Avançar':
        print('Opção selecionada')
        break
    

                    

                    
            