from CRUD_menagment import *

def menu():
    print('''Vem vindo ao Projeto Final
SISTEMA DE PUBLICAÇÕES CIENTÍFICAS
    (1) Load DataSet
    (2) Print DataSet
    (3) Guardar DataSet
    (4) Adicionar Post
    ()
    ()
    ()
    (0) SAIR''')
    op = input('Digite o num da opção que deseja fazer: ') 
    while not op.isdigit():
        op = input('Digite o num da opção que deseja fazer: ')
    
    return int(op)



op = menu()
while op != 0:
    if op == 1:
        DATA_SET: list = Abrir_DataSet('../TRABALHO_FINAL/DataSet_Main.json')

    elif op == 2:
        print(DATA_SET)

    elif op == 3:
        Guardar_DataSet('../TRABALHO_FINAL/DataBase_New.json', DATA_SET)


    elif op == 4:
        DATA_SET.append(novoPost())
    op = menu()
print('Obrigado, volte sempre!')