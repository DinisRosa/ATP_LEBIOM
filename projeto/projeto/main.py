from Interface.main_Import_InterfaceFolder import *
from Interface.interfaceDone import *

def UI():
    print('''Bem vindo ao Projeto Final!
SISTEMA DE PUBLICAÇÕES CIENTÍFICAS
Escolha a interface que deseja utilizar:
    (1) Interface Gráfica
    (2) Interface de Comandos''')
    return input('Digite o num da opção que deseja escolher: ')

def menu():
    print('''Vem vindo ao Projeto Final
SISTEMA DE PUBLICAÇÕES CIENTÍFICAS
    (1) Load DataSet
    (2) Print DataSet
    (3) Guardar DataSet
    (4) Adicionar Post
    (5) Apagar Post
    (6) HelpMe
    (0) SAIR''')
    op = input('Digite o num da opção que deseja fazer: ') 
    while not op.isdigit():
        op = input('Digite o num da opção que deseja fazer: ')
    
    return int(op)

def Terminal_Interface():
    DATA_SET: list = []
    op = menu()
    while op != 0:
        if op == 1:
            DATA_SET = Abrir_DataSet('../TRABALHO_FINAL/DataSet_Main.json')
            print(f'DataSet carregado com sucesso! {len(DATA_SET)} publicações encontradas.')
            doiDict, pdDict, kwDict, autDict = UpdateIndexes(DATA_SET) 

        elif op == 2:
            if DATA_SET != []:
                PrintDataSet(DATA_SET)
            else: print('Não tem nenhum dataset carregado!')

        elif op == 3:
            Guardar_DataSet('../TRABALHO_FINAL/DataBase_New.json', DATA_SET)

        elif op == 4:
            DATA_SET.append(novoPost())
            doiDict, pdDict, kwDict, autDict = UpdateIndexes(DATA_SET)
        
        elif op == 5:
            idx = idxPost(doiDict, pdDict, kwDict, autDict)
            if idx != [-1]:
                DATA_SET = ApagarPost(DATA_SET, idx)
                doiDict, pdDict, kwDict, autDict = UpdateIndexes(DATA_SET)

        elif op == 6:
            print('''Se precisar de ajuda, consulte o arquivo README.md no repositório do projeto no GitHub.
    Link Repo: https://github.com/DinisRosa/ATP_LEBIOM/tree/main/TRABALHO_FINAL''')
        op = menu()
    print('Obrigado, volte sempre!')


o = UI()
if o == '1':
    print('Interface Gráfica')
    GUI_main()
elif o == '2':
    Terminal_Interface()
else:
    print('''Opção inválida! Tente novamente.
Reinicie o programa para escolher a interface desejada.''')