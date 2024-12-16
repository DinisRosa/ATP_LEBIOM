import json
from datetime import datetime


# ABRIR/GUARDAR .json
def Abrir_DataSet(file_name: str) -> list:
    file: list = open(file_name, 'r', encoding = 'utf8')
    DATA_SET: list = json.load(file)
    return DATA_SET


def Guardar_DataSet(file_name: str, dataSet: list) -> None:
    file = open(file_name, 'w', encoding = 'utf8')
    json.dump(dataSet, file, ensure_ascii = False)
    file.close()


# Subdivisão da base de dados para facilitar pesquisa
def all_DOI_path(base: list) -> list:
    DOI_path = []
    for i, pub in enumerate(base):
        if 'doi' in pub.keys():
            DOI_path.append((pub['doi'][29:], i))
    return sorted(DOI_path, key=lambda tuplo: int(tuplo[0]))


def all_PublishDates(base: list) -> list:
    Pub_Dates = []
    for i, pub in enumerate(base):
        if 'publish_date' in pub.keys():
            Pub_Dates.append((pub['publish_date'][:11], i))
            
    return sorted(Pub_Dates, key=lambda data: int(data[0].split('-')[0] + data[0].split('-')[1] + data[0].split('-')[2]))


def all_KeyWords(base: list) -> list:
    KeyWords = []
    for i, pub in enumerate(base):
        if 'keywords' in pub.keys():
                KeyWords.append(([''.join(char for char in pub['keywords'] if char not in '!,?')]))
                KeyWords.append((pub['keywords'].split(','), i))
    return KeyWords


def all_Authors(base: list) -> list:
    Authors = []
    for i, pub in enumerate(base):
        if 'authors' in pub.keys():
            Authors.append(([nome['name'] for nome in pub['authors']], i))
    return Authors

# Adicionar novo post
def novoPost_Data() -> str:
    MaxdaysPerMonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 29)
    publish_year = input('Digite o ano da publicação que quer adicionar: ')
    while (not publish_year.isdigit()) or (1900 > int(publish_year) or int(publish_year) > datetime.now().year):
        publish_year = input('Por favor digite um ano válido (desde 1900)! ')

    publish_month = input('Digite o mês (1 a 12) da publicação que quer adicionar: ')
    while (not publish_month.isdigit()) or (0 > int(publish_month) or int(publish_month) > 12) or int(publish_month) > datetime.now().month:
        publish_month = input('Por favor digite um mês válido (1 a 12)! ')

    publish_day = input('Digite o dia da publicação que quer adicionar: ')
    isInvalid = True
    while isInvalid:
        if not publish_day.isdigit(): # str ñ pode ser convertido para int
            publish_day = input('Por favor digite um dia válido! ')
        else: # str pode ser convertido para int
            if int(publish_year) == datetime.now().year and int(publish_month) == datetime.now().month and int(publish_day) > datetime.now().day:
                    publish_day = input('Por favor digite um dia válido! ') # dia futuro

            if int(publish_month) != 2: # ñ é fevereiro
                idx = int(publish_month) - 1
            else: #se for fevereiro
                if int(publish_year) % 4 == 0 and (int(publish_year) % 100 != 0 or int(publish_year) % 400 == 0):
                    idx = 12 # é bissexto
                else:
                    idx = 1 # normal
            if (0 > int(publish_day) or int(publish_day) > MaxdaysPerMonth[idx]):
                publish_day = input('Por favor digite um dia válido! ') # dia inexistente no mês escolhido
            else: # data possível
                isInvalid = False
    return f'{publish_year}-{publish_month}-{publish_day}'


def novoPost_Abstract():
    abstract = input('Digite o abstrato da publicação que quer adicionar: ')
    while abstract == '':
        abstract = input('Por favor digite um abstrato válido! ')
    
    return abstract


def novoPost_KeyWords() -> str:
    print('EX: "Portugal, Medicina, Hospital, ..."')
    keywords = input('Quais as palavras-chave da publicação que quer adicionar: ')
    while keywords == '':
        keywords = input('Por favor digite palavras-chave válidas! ')
    
    return keywords


def novoPost_doiPath() -> str:
    doiPath = input('Digite o caminho DOI da publicação que quer adicionar: ')
    while doiPath == '':
        doiPath = input('Por favor digite um DOI válido! ')

    return doiPath


def novoPost_pdfPath() -> str:
    pdfPath = input('Digite o caminho de PDF da publicação que quer adicionar: ')
    while pdfPath == '':
        pdfPath = input('Por favor digite um caminho de PDF válido! ')

    return pdfPath


def novoPost_Title() -> str:
    title = input('Digite o título da publicação que quer adicionar: ')
    while title == '':
        title = input('Por favor digite um título válido! ')

    return title


def novoPost_Url() -> str:
    urlPath =  input('Digite o caminho URL da publicação que quer adicionar: ')
    while urlPath == '':
        urlPath = input('Por favor digite um URL válido! ')

    return urlPath


def novoPost_Authors() -> list:
    Autores = []
    maisAutor = True
    while maisAutor:
        autor = input('Qual o nome do autor da publicação que quer adicionar: ')
        while autor == '':
            autor = input('Por favor digite um nome válido! ')
        Autores.append(autor)
        continuar = input('Dseja continuar: (S) SIM, (N) NÃO: ')
        maisAutor = True if continuar.upper() == 'S' else False
    
    return Autores


def novoPost() -> dict:
    newPost = {
        "abstract": novoPost_Abstract(),
        "keywords": novoPost_KeyWords(),
        "authors": [],
        "doi": novoPost_doiPath(),
        "pdf": novoPost_pdfPath(),
        "publish_date": novoPost_Data(),
        "title": novoPost_Title(),
        "url": novoPost_Url()
    }

    return newPost


### Ñ é assim que quero
def ProcurarPost_PorNome(dataSet: list, nomeAutor: str):
    postsDoAutor = []
    for post in dataSet:
        for autor in post['authors']:
            if autor['name'] == nomeAutor:
                postsDoAutor.append(post['title'])

    return postsDoAutor


def ProcurarPost_PorDOI(base: list, baseDOI: list, DOI: int):
    pass


# ERRADO
def BinarySearch(lista: list, alvo: any) -> int:
    min: int = 0
    max: int = len(lista) - 1
    idx: int = (min+max) // 2
    while lista[idx][1] != alvo or min >= max:
        if lista[idx][1] < alvo:
            min = idx + 1
        else:
            max = idx - 1
        idx = (min+max) // 2
    return idx


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

