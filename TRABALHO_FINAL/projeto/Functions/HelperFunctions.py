from Functions.main_Import_FunctionsFolder import *

def idxPost(doiDict: dict, pdDict: dict, kwDict: dict, autDict: dict) -> list:
    print('''Como deseja procurar pelo post:
    (1) Por palavras chave
    (2) Por autores
    (3) Por data de publicação
    (4) Por DOI path''')

    op: str = input('Digite o número da opção: ')
    
    Pubs = [-1]

    if op == '1':  # keywords
        keyword = input('Digite uma palavra chave: ')
        if keyword in kwDict:
            Pubs =  kwDict[keyword]
        else:
            print('Palavra chave não encontrada.')
    
    elif op == '2':  # authors
        author = input('Digite o nome do autor: ')
        if author in autDict:
            Pubs = autDict[author]
        else:
            print('Autor não encontrado.')
    
    elif op == '3':  # publish_date
        date = input('Digite a data de publicação (YYYY-MM-DD): ')
        if date in pdDict:
            Pubs = pdDict[date]
        else:
            print('Data de publicação não encontrada.')
    
    elif op == '4':  # doi
        doi = input('Digite o DOI path: ')
        if doi in doiDict:
            Pubs = doiDict[doi]
        else:
            print('DOI não encontrado.')

    else:
        print('Digite uma opção válida.')
        idxPost(doiDict, pdDict, kwDict, autDict)

    return Pubs


def PrintDataSet(base: list)-> None:
    for i, pub in enumerate(base):
        print(f'\033[92m{i:-^20}\033[0m')
        if 'title' in pub:
            print(f'\033[34mTítulo:\033[0m {pub["title"]}')
        if 'publish_date' in pub:
            print(f'\033[34mData de publicação:\033[0m {pub["publish_date"]}')
        if 'authors' in pub:
            print(f'\033[34mAutor(es):\033[0m {[nome["name"] for nome in pub["authors"]]}')
    return None