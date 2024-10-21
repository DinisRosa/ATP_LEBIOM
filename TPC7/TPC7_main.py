from TPC7_functions import *

TABELA_METEREOLOGICA = []

op = menu()

while op !=0:
    if op == 1:
        TABELA_METEREOLOGICA = carregaTabMeteo('meteorologia.txt')
    elif op == 2:
        guardarTabMeteo(TABELA_METEREOLOGICA, 'meteorologia.txt')
    elif op == 3:
        print(medias(TABELA_METEREOLOGICA))
    elif op == 4:
        print(minMin(TABELA_METEREOLOGICA))
    elif op == 5:
        print(amplTerm(TABELA_METEREOLOGICA))
    elif op == 6:
        print(maxChuva(TABELA_METEREOLOGICA))
    elif op == 7:
        p = float(input('Digite o valor de precipitação: '))
        print(diasChuvosos(TABELA_METEREOLOGICA, p))
    elif op == 8:
        p = float(input('Digite o valor de precipitação: '))
        print(maxPeriodoCalor(TABELA_METEREOLOGICA, p))
    elif op == 9:
        grafs(TABELA_METEREOLOGICA)
    op = menu()

print('Obrigado! Volte sempre!')