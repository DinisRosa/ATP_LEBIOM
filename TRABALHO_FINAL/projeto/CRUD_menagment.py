from DataSet_SaveLoad import *
from DataSet_Subdivision import *
from Add_Post import * 


### Ñ é assim que quero
def ProcurarPost_PorNome(dataSetNomes: list, nomeAutor: str)->list:
    Selected = []
    for author in dataSetNomes:
        pass
    


def ProcurarPost_PorDOI(base: list, baseDOI: list, DOI: int):
    pass




def idxPost(dataSet: list) -> int:
    print('''Como deseja procurar pelo post:
    (1) Por palavras chave
    (2) Por autores
    (3) Por data de publicação
    (4) Por DOI path
    (0) Sair''')

    op: str = input('Digite o número da opção: ')
    while op != '0':
        if op == '1': # keywords
            pass
        elif op == '2': # authors
            pass
        elif op == '3': # publish_date
            pass
        elif op == '4': # doi
            pass
        else:
            op = input('Digite uma opção válida: ')


def ApagarPost(base: list, idx: int) -> list:
    if idx == -1:
        print('Index não existe!')
    else:
        base.pop(idx)
    return base

