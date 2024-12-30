from Interface.main_Import_InterfaceFolder import *
import PySimpleGUI as sg


base = Abrir_DataSet('DataSet_Main.json')

#print(len(base))
doiDict = all_DOI_path(base)
pdDict = all_PublishDates(base)
kwDict = all_KeyWords(base)
autDict = all_Authors(base)



'''
a = idxPost(doiDict, pdDict, kwDict, autDict)
print(a)
'''
#print(kwDict)


#ApagarPost(base, [1,2,3])
#PrintDataSet(base)

def gerar_grafico_publicacoes_por_ano_autor(base):
    # Extrair autores únicos das publicações
    autores = {}
    for i, pub in enumerate(base):
        if 'authors' in pub.keys():
            pubAuthors: list[str] = [nome['name'] for nome in pub['authors']]
            for author in pubAuthors:
                if author not in autores:
                    autores[author] = [i]
                else:
                    autores[author].append(i)
    
    print(autores)

    escolha = input('Escolha um autor para ver o gráfico de publicações por ano: ')
    publicacoes = autores[escolha]
    anos = {}
    for i in publicacoes:
        ano = base[i]['publish_date'][:4]
        if ano not in anos:
            anos[ano] = 1
        else:
            anos[ano] += 1



gerar_grafico_publicacoes_por_ano_autor(base)