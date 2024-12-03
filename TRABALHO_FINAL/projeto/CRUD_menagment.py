import json
from datetime import datetime


# ABRIR/GUARDAR .json
def Abrir_DataSet(file_name: str) -> list:
    file: list = open(file_name, 'r', encoding = 'utf8')
    DATA_SET: list = json.load(file)
    return DATA_SET


def Guardar_DataSet(file_name: str, dataSet: list):
    file = open(file_name, 'w', encoding = 'utf8')
    json.dump(dataSet, file, ensure_ascii = False)
    file.close()


def ProcurarPost_PorNome(dataSet: list, nomeAutor: str):
    postsDoAutor = []
    for post in dataSet:
        for autor in post['authors']:
            if autor['name'] == nomeAutor:
                postsDoAutor.append(post['title'])

    return postsDoAutor


def novoPost_Data():
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


def novoPost_KeyWords():
    keywords = input('Quais as palavras-chave da publicação que quer adicionar: ')
    while keywords == '':
        keywords = input('Por favor digite palavras-chave válidas! ')
    
    return keywords


def novoPost_doiPath():
    doiPath = input('Digite o caminho DOI da publicação que quer adicionar: ')
    while doiPath == '':
        doiPath = input('Por favor digite um DOI válido! ')

    return doiPath


def novoPost_pdfPath():
    pdfPath = input('Digite o caminho de PDF da publicação que quer adicionar: ')
    while pdfPath == '':
        pdfPath = input('Por favor digite um caminho de PDF válido! ')

    return pdfPath


def novoPost_Title():
    title = input('Digite o título da publicação que quer adicionar: ')
    while title == '':
        title = input('Por favor digite um título válido! ')

    return title

def novoPost_Url():
    urlPath =  input('Digite o caminho URL da publicação que quer adicionar: ')
    while urlPath == '':
        urlPath = input('Por favor digite um URL válido! ')

    return urlPath


def novoPost():
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

def idxPost(dataSet: list):
    print(f'Como deseja procurar pelo post:')
    for i, key in enumerate(dataSet[0].keys()):
        print(f'    ({i+1}) {key}')
    op = input('>>>> ')
    if op == '1': # abstract
        pass
    if op == '2': # keywords
        pass
    if op == '3': # authors
        pass
    if op == '4': # doi
        pass
    if op == '5': # pdf
        pass
    if op == '6': # publish_date
        pass
    if op == '7': # title
        pass
    if op == '8': # url
        pass




def ApagarPost():
    pass

