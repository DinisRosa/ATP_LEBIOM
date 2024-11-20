from TPC6_functions import *


LISTA_TURMAS = {}


op = menu()
while op != 0:
    if op == 1:
        LISTA_TURMAS = adicionarTurma(LISTA_TURMAS)
    
    elif op == 2:    
        LISTA_TURMAS = adicionarAluno(LISTA_TURMAS)

    elif op == 3:
        listarTurmas(LISTA_TURMAS)

    elif op == 4:
        procurarAlunoPorID(LISTA_TURMAS)

    elif op == 5:
        guardarTurma(LISTA_TURMAS)
    
    elif op == 6:
        LISTA_TURMAS = carregarTurma(LISTA_TURMAS)

    op = menu()

print('Obrigao, volte sempre!!!')