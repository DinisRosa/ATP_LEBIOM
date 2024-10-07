import random


def menu():
    print('''Bem vindo!
    (1) Criar Lista 
    (2) Ler Lista
    (3) Soma de todos os valores da lista
    (4) Média dos valores da lista
    (5) Maior da lista
    (6) Menor lista
    (7) A lista está ordenada por oredem crescente?
    (8) A lista está ordenada por oredem decrescente?
    (9) Procurar por um elemento
    (0) Sair
''')
    
    return int(input('O que deseja fazer? Indique o número: '))


### Criação das funções de criação de listas:
def inputList():
    N = int(input('Digite o numero maximo de elementos que deseja: '))
    return [int(input(f'Digite num {i+1}/{N}: ')) for i in range(N)]

def randomList():
    N = int(input('Digite o numero maximo de elementos que deseja: '))
    return [random.randint(0, 100) for i in range(N)]

### Criação das várias funções de manipulação de listas:
def somaList(list):
    soma = 0
    for n in list:
        soma += n
    return soma

def meanList(list):
    return somaList(list) / len(list)

def maxList(list):
    max = list[0]
    for l in list[1:]:
        if l > max:
            max = l
    return max

def minList(list):
    min = list[0]
    for l in list[1:]:
        if l < min:
            min = l
    return min

def isMintoMax(list):
    isOrdered = True
    i = 0
    while isOrdered or i < len(list)-1:
        if list[i] > list[i+1]:
            isOrdered = False
        i += 1
    return print('SIM') if isOrdered else print('NÃO')

def isMaxtoMin(list):
    isOrdered = True
    i = 0
    while isOrdered or i < len(list)-1:
        if list[i] < list[i+1]:
            isOrdered = False
        i += 1
    return print('SIM') if isOrdered else print('NÃO')

def findElement(list, elem):
    for idx, n in enumerate(list):
        if n == elem:
            return idx, n
    else:
        return -1, n
        




#MAIN CODE
op = menu()
internalList = []
while op != 0:
    #OPERADOR METEU UM NÚMERO INVÁLIDO
    if op not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('Operação inválida. Digite um número válido!')
        op = menu()

    #CRIAÇÃO DA LISTA INTERNA:
    #PELO PC
    if op == 1:
        internalList = randomList()
        print(f'A lista interna guardada é agora: {internalList}')
        op = menu()
    #PELO OPERADOR
    elif op == 2:
        internalList = inputList()
        print(f'A lista interna guardada é agora: {internalList}')
        op = menu()
    #SÓ SE PREOCEGUE PARA AS OUTRAS OPERAÇÕES SE A LISTA INTERNA TIVER SIDO CRIADA
    if (op != 1 or 2) and internalList == []:
        op = int(input('''Crie ou Leie primeiro uma lista antes de fazer outras operações:
    (1) Criar Lista 
    (2) Ler Lista
    (0) Sair
'''))
    #OPERAÇÕES:
    #SOMA DOS VALORES DA LISTA
    elif op == 3:
        print(f'A soma de todos os valores da lista interna é {somaList(internalList)}')
        op = menu()
    #MÉDIA DOS VALRES DA LISTA
    elif op == 4:
        print(f'A média da lista interna é {meanList(internalList)}')
        op = menu()
    #MAIOR DA LISTA
    elif op == 5:
        print(f'O maior valor da lista interna é {maxList(internalList)}')
        op = menu()
    #MENOR DA LISTA
    elif op == 6:
        print(f'O menos valores da lista interna é {minList(internalList)}')
        op = menu()
    #LISTA ORDENADA POR ORDEM CRESCENTE
    elif op == 7:
        isMintoMax(internalList)
        op = menu()
    #LISTA POR OREDEM DECRESCENTE
    elif op == 8:
        isMaxtoMin(internalList)
        op = menu()
    #PROCURAR POR NÚMERO NA LISTA
    elif op == 9:
        elem = int(input('Que número quer ver se está na lista interna? '))
        idx, n = findElement(internalList, elem)
        if idx != -1:
            print(f'O {n} está na lista no index {idx}')
        else: print(f'O {n} não está na lista')
        op = menu()

#END MESSAGE
print('Obrigado, volte sempre!!')