from HelperFunctions import *

def menu():
    print('''Vem vindo ao Projeto Final
SISTEMA DE PUBLICAÇÕES CIENTÍFICAS
    (1) Load DataSet
    (2) Print DataSet
    (3) Guardar DataSet
    (4) Adicionar Post
    (5) Apagar Post
    ()
    ()
    (0) SAIR''')
    op = input('Digite o num da opção que deseja fazer: ') 
    while not op.isdigit():
        op = input('Digite o num da opção que deseja fazer: ')
    
    return int(op)


DATA_SET: list = []
op = menu()
while op != 0:
    if op == 1:
        DATA_SET = Abrir_DataSet('../TRABALHO_FINAL/DataSet_Main.json')
        print(f'DataSet carregado com sucesso! {len(DATA_SET)} publicações encontradas.')
        doiDict, pdDict, kwDict, autDict = UpdateIndexes(DATA_SET) 

    elif op == 2:
        PrintDataSet(DATA_SET)

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
    op = menu()
print('Obrigado, volte sempre!')


