import os
import PySimpleGUI as sg
import json
from datetime import datetime
import matplotlib.pyplot as plt
from Interface.main_Import_InterfaceFolder import *
caminho_ficheiro = 'DataSet_Main.json'

# Funções para gestão de ficheiros
def carregar_dados(path=None):
    dados = []
    if not path:
        caminho_ficheiro = sg.popup_get_file('Selecione o arquivo para importar', no_window=True)
    else:
        caminho_ficheiro = path
    try:
        file: list = open(caminho_ficheiro, 'r', encoding = 'utf8')
        DATA_SET: list = json.load(file)
        dados = DATA_SET
    except FileNotFoundError:
        print('Erro ao abrir o arquivo. O arquivo não existe ou não está acessível. Base de dados inicializada como vazia.')

    return dados

def guardar_dados(base, path=None):
    if not path:
        caminho_ficheiro = sg.popup_get_file('Salvar como', save_as=True, no_window=True, file_types=(("JSON Files", "*.json"),))
    else:
        caminho_ficheiro = path
    try:
        file = open(caminho_ficheiro, 'w', encoding = 'utf8')
        json.dump(base, file, ensure_ascii = False)
        file.close()
        sg.popup('Dados guardados com sucesso!')
    except Exception as e:
        sg.popup_error(f'Erro ao guardar os dados: {e}')



# Funções para lidar com os dados de publicações
def criar_publicacao():
    layout = [
        [sg.Text('Título:'), sg.InputText(key='title')],
        [sg.Text('Resumo:'), sg.InputText(key='abstract')],
        [sg.Text('Palavras-chave (separado por ,):'), sg.InputText(key='keywords')],
        [sg.Text('Autores (separado por,):'), sg.InputText(key='authors')],
        [sg.Text('DOI:'), sg.InputText(key='doi')],
        [sg.Text('Caminho do PDF:'), sg.InputText(key='pdf')],
        [sg.Text('URL:'), sg.InputText(key='url')],
        [sg.Text('Data de publicação (YYYY-MM-DD):'), sg.InputText(key='publish_date')],
        [sg.Button('Salvar'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Adicionar Publicação', layout)

    run = True
    while run:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Cancelar':
            window.close()
            run = False
        elif evento == 'Salvar':
            if not values['title'] or not values['abstract'] or not values['publish_date']:
                sg.popup_error('Por favor, preencha os campos obrigatórios!')
                continue
            try:
                data_publicacao = datetime.strptime(values['publish_date'], '%Y-%m-%d')
                data_atual = datetime.now()
                if data_publicacao > data_atual:
                    sg.popup_error('A data de publicação não pode ser posterior à data atual!')
                    continue
                dados = carregar_dados(path=caminho_ficheiro)
                values['authors'] = [{'name': name} for name in values['authors'].split(',')]
                novoP = {key: values[key] for key in values.keys() if values[key] != ''}
                dados.append(novoP)
                guardar_dados(base=dados, path=caminho_ficheiro)
                sg.popup('Publicação adicionada com sucesso!')
                window.close()
                run = False
            except ValueError:
                sg.popup_error('Data de publicação inválida! Use o formato YYYY-MM-DD.')



def atualizar_publicacao():
    dados = carregar_dados(path=caminho_ficheiro)
    titulos = [pub['title'] for pub in dados if 'title' in pub.keys()]
    layout = [
        [sg.Text('Selecione a publicação para atualizar:')],
        [sg.Combo(titulos, key='titulo', size=(50, 1))],
        [sg.Button('Selecionar'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Atualizar Publicação', layout)
    finnished = False
    while not finnished:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            window.close()
            finnished = True
        elif event == 'Selecionar':
            titulo = values['titulo']
            if titulo:
                pub = next(pub for pub in dados if pub['title'] == titulo)
                layout_atualizar = [
                    [sg.Text('Título:'), sg.InputText(pub['title'], key='title')],
                    [sg.Text('Resumo:'), sg.Multiline(pub['abstract'], key='abstract')],
                    [sg.Text('Palavras-chave (uma por linha):'), sg.Multiline(pub['keywords'], key='keywords')],
                    [sg.Text('Autores (um por linha):'), sg.Multiline(pub['authors'], key='authors')],
                    [sg.Text('DOI:'), sg.InputText(pub['doi'], key='doi')],
                    [sg.Text('Caminho do PDF:'), sg.InputText(pub['pdf'], key='pdf')],
                    [sg.Text('URL:'), sg.InputText(pub['url'], key='url')],
                    [sg.Text('Data de publicação (YYYY-MM-DD):'), sg.InputText(pub['publish_date'], key='publish_date')],
                    [sg.Button('Salvar'), sg.Button('Cancelar')]
                ]
                window_atualizar = sg.Window('Atualizar Publicação', layout_atualizar, size=(800, 300))

                finnished2 = False
                while not finnished2:
                    event_atualizar, values_atualizar = window_atualizar.read()
                    if event_atualizar in [sg.WINDOW_CLOSED, 'Cancelar']:
                        window_atualizar.close()
                        finnished2 = True
                    elif event_atualizar == 'Salvar':
                        try:
                            data_publicacao = datetime.strptime(values_atualizar['publish_date'], '%Y-%m-%d')
                            data_atual = datetime.now()
                            if data_publicacao > data_atual:
                                sg.popup_error('A data de publicação não pode ser posterior à data atual!')
                                continue
                            pub.update(values_atualizar)
                            guardar_dados(base=dados, path=caminho_ficheiro)
                            sg.popup('Publicação atualizada com sucesso!')
                            window_atualizar.close()
                            finnished2 = True
                            return values_atualizar
                        except ValueError:
                            sg.popup_error('Data de publicação inválida! Use o formato YYYY-MM-DD.')


def pesquisar_publicacao():
    layout = [
        [sg.Text('Pesquisar Publicação')],
        [sg.Button('Filtrar por Título')],
        [sg.Button('Filtrar por Autor')],
        [sg.Button('Filtrar por Data de Publicação')],
        [sg.Button('Filtrar por Palavras-chave')],
        [sg.Button('Voltar')]
    ]
    window = sg.Window('Pesquisar Publicação', layout)
    run = True
    while run:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Voltar':
            window.close()
            return None
        elif event == 'Filtrar por Título':
            return filtro_titulo()
        elif event == 'Filtrar por Autor':
            return filtro_autor()
        elif event == 'Filtrar por Data de Publicação':
            return filtro_data_publicacao()
        elif event == 'Filtrar por Palavras-chave':
            return filtro_palavras_chave()
        run = False
base = carregar_dados(path=caminho_ficheiro)


def filtro_titulo():
    layout = [
        [sg.Text('Digite o título para filtrar:'), sg.InputText(key='titulo')],
        [sg.Button('Pesquisar'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Filtrar por Título', layout)
    run = True
    while run:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Cancelar':
            window.close()
            run = False
        elif evento == 'Pesquisar':
            titulo = values['titulo'].lower()
            dados = carregar_dados(path=caminho_ficheiro)
            if not titulo:
                sg.popup('Sem resultados', font=('Helvetica', 12), title='Resultado da Pesquisa')
                continue
            resultados = []
            for pub in dados:
                if 'title' not in pub.keys():
                    continue
                if titulo == pub['title'].lower():
                    resultados.append(pub)
            if not resultados:
                sg.popup('Nenhuma publicação encontrada para o título especificado.', font=('Helvetica', 12), title='Resultado da Pesquisa')
                continue
            else:
                exibir_resultados(resultados)
            window.close()
            run = False

def filtro_autor():
    layout = [
        [sg.Text('Digite o autor para filtrar:'), sg.InputText(key='autor')],
        [sg.Button('Pesquisar'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Filtrar por Autor', layout)
    run = True
    while run:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Cancelar':
            window.close()
            run = False
        elif evento == 'Pesquisar':
            autor = values['autor'].lower().strip()
            if not autor:
                sg.popup('Sem resultados', font=('Helvetica', 12), title='Resultado da Pesquisa')
                continue
            dados = carregar_dados(path=caminho_ficheiro)
            resultados = []
            for pub in dados:
                autores = [a['name'].lower().strip() for a in pub['authors']]
                if any(autor in a for a in autores):
                    resultados.append(pub)
            if resultados:
                exibir_resultados(resultados)
            else:
                sg.popup('Nenhuma publicação encontrada para o autor especificado.', font=('Helvetica', 12), title='Resultado da Pesquisa')
            window.close()
            run = False
            return resultados

def filtro_data_publicacao():
    layout = [
        [sg.Text('Digite a data de publicação para filtrar (YYYY-MM-DD ou apenas o ano):'), sg.InputText(key='data')],
        [sg.Button('Pesquisar'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Filtrar por Data de Publicação', layout)

    finnished = False
    while not finnished:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Cancelar':
            window.close()
            finnished = True
        elif evento == 'Pesquisar':
            data = values['data']
            dados = carregar_dados(path=caminho_ficheiro)
            if len(data) == 4:  # Se o usuário digitou apenas o ano
                resultados = [pub for pub in dados if 'publish_date' in pub.keys() and pub['publish_date'].startswith(data)]
            else:
                resultados = [pub for pub in dados if data in pub['publish_date']]
            resultados.sort(key=lambda x: x['publish_date'], reverse=True)
            exibir_resultados(resultados)
            window.close()
            finnished = True
            return resultados


def filtro_palavras_chave():
    layout = [
        [sg.Text('Digite a palavra-chave para filtrar:'), sg.InputText(key='palavra_chave')],
        [sg.Button('Pesquisar'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Filtrar por Palavras-chave', layout)
    while True:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Cancelar':
            window.close()
            return None
        elif evento == 'Pesquisar':
            palavra_chave = values['palavra_chave'].lower()
            dados = carregar_dados(path=caminho_ficheiro)
            resultados = []
            for pub in dados:
                if 'keywords' in pub:
                    if palavra_chave in pub['keywords'].lower():
                        resultados.append(pub)
            if not resultados:
                sg.popup('Nenhuma publicação encontrada para a palavra-chave especificada.', font=('Helvetica', 12), title='Resultado da Pesquisa')
                continue
            else:
                exibir_resultados(resultados)
            window.close()
            return resultados

def exportar_dados_parcial(dados_parciais):
    caminho_exportacao = sg.popup_get_file('Salvar como', save_as=True, no_window=True, file_types=(("JSON Files", "*.json"),))
    if caminho_exportacao:
        try:
            with open(caminho_exportacao, 'w') as ficheiro:
                json.dump(dados_parciais, ficheiro, indent=4)
            sg.popup('Dados parciais exportados com sucesso!')
        except Exception as e:
            sg.popup_error(f'Erro ao exportar os dados parciais: {e}')

def exibir_resultados(resultados):
    layout = [[sg.Text('Resultados da Pesquisa', font=('Helvetica', 16), justification='center')]]
    for pub in resultados:
        layout.append([sg.Text('Título:', font=('Helvetica', 12, 'bold')), sg.Text(pub['title'])])
        layout.append([sg.Text('Resumo:', font=('Helvetica', 12, 'bold')), sg.Text(pub['abstract'])])
        layout.append([sg.Text('Palavras-chave:', font=('Helvetica', 12, 'bold')), sg.Text(pub['keywords'] if 'keywords' in pub else 'N/A')])
        layout.append([sg.Text('Autores:', font=('Helvetica', 12, 'bold')), sg.Text(', '.join(autor['name'] for autor in pub['authors']))])
        layout.append([sg.Text('DOI:', font=('Helvetica', 12, 'bold')), sg.Text(pub['doi'] if 'doi' in pub else 'N/A')])
        layout.append([sg.Text('Caminho do PDF:', font=('Helvetica', 12, 'bold')), sg.Text(pub['pdf'] if 'pdf' in pub else 'N/A')])
        layout.append([sg.Text('URL:', font=('Helvetica', 12, 'bold')), sg.Text(pub['url'] if 'url' in pub else 'N/A')])
        layout.append([sg.Text('Data de publicação:', font=('Helvetica', 12, 'bold')), sg.Text(pub['publish_date'] if 'publish_date' in pub else 'Sem data')])
        layout.append([sg.Text('-' * 40)])
    layout.append([sg.Button('Exportar Pesquisa'), sg.Button('Fechar')])
    window = sg.Window('Resultados da Pesquisa', layout, location=(100,100), modal=True, size=(800, 600))
    run = True
    while run:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Fechar':
            window.close()
            run = False
        elif evento == 'Exportar Pesquisa':
            exportar_dados_parcial(resultados)
            sg.popup('Pesquisa exportada com sucesso!')
            run = False

def analise_post():
    layout = [
        [sg.Button('Análise por Autor')],
        [sg.Button('Análise por Palavras-chave')],
        [sg.Button('Voltar')]
    ]
    window = sg.Window('Análise do Post', layout)
    finnished = False
    while not finnished:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Voltar':
            window.close()
            finnished = True
            return
        elif evento == 'Análise por Autor':
            analisar_por_autor(base)
            return
        elif evento == 'Análise por Palavras-chave':
            analisar_por_palavra_chave(base)
            return


def gerar_grafico_publicacoes_por_ano(base):
    anos = {}
    for pub in base:
        if 'publish_date' not in pub:
            continue
        ano = pub['publish_date'].split('-')[0]
        anos[ano] = anos.get(ano, 0) + 1
    anos = dict(sorted(anos.items()))
    plt.bar(anos.keys(), anos.values())
    plt.xlabel('Ano')
    plt.ylabel('Número de Publicações')
    plt.title('Distribuição de Publicações por Ano')
    plt.show()



def PrintDataSet(base):
    layout_base = [[sg.Text('Lista de Publicações')]]
    for i, pub in enumerate(base):
        if 'publish_date' in pub:
            pub_info = f"{i}: '{pub['title'][:90]} (...)' ({pub['publish_date']})" if len(pub['title']) > 90 else f"{i}: '{pub['title']}' ({pub['publish_date']})"
        else:
            if 'title' in pub:
                pub_info = f"{i}: '{pub['title'][:90]} (...)' (Sem data)" if len(pub['title']) > 90 else f"{i}: '{pub['title']}' (Sem data)"
        layout_base.append([sg.Text(pub_info)])

    layout = [
        [sg.Column(layout_base, scrollable=True, vertical_scroll_only=True, size=(800, 500))]
    ]
    layout.append([sg.Button('Fechar')])

    window = sg.Window('Publicações', layout, location=(0, 0), size=(800, 600))
    window.read()
    window.close()

def gerenciar_publicacoes(base):
    layout = [
        [sg.Listbox(
            values=[f"{i}: {post['title']}" for i, post in enumerate(base) if 'title' in post.keys()],
            size=(50, 10), key='publicacoes', enable_events=True
        )],
        [sg.Button('Adicionar'), sg.Button('Apagar'), sg.Button('Fechar')]
    ]

    window = sg.Window('Gerir Publicações', layout)

    while True:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Fechar':
            window.close()
            return
        elif evento == 'Adicionar':
            nova_publicacao = criar_publicacao()
            if nova_publicacao:
                base.append(nova_publicacao)
                window['publicacoes'].update(
                    [f"{i}: {post['title']}" for i, post in enumerate(base)]
                )
        elif evento == 'Apagar':
            if values['publicacoes']:
                idx = int(values['publicacoes'][0].split(':')[0])
                confirm = sg.popup_yes_no(f"Tem certeza de que deseja apagar '{base[idx]['title']}'?")
                if confirm == 'Yes':
                    del base[idx]
                    window['publicacoes'].update(
                        [f"{i}: {pub['title']}" for i, pub in enumerate(base) if 'title' in pub.keys()]
                    )

def analisar_por_autor(base):
    autores = {}
    for i, pub in enumerate(base):
        if 'authors' in pub.keys():
            pubAuthors: list[str] = [nome['name'] for nome in pub['authors']]
            for author in pubAuthors:
                if author not in autores:
                    autores[author] = [pub]
                else:
                    autores[author].append(pub)

    autores_ordenados = sorted(autores.items(), key=lambda x: (-len(x[1]), x[0])) 

    layout_autores = [
        [sg.Text('Autores e Publicações', font=('Helvetica', 16), justification='center', pad=(0, 20))]
    ]

    for autor, publicacoes in autores_ordenados[:20]:
        layout_autores.append([sg.Text(f"{autor} ({len(publicacoes)} publicações):", font=('Helvetica', 14, 'bold'), pad=(0, 10))])
        for pub in publicacoes:
            if 'publish_date' in pub:
                layout_autores.append([sg.Text(f"  - {pub['title']} ({pub['publish_date']})", font=('Helvetica', 12), pad=(20, 5))])
            else:
                if 'title' in pub:
                    layout_autores.append([sg.Text(f"  - {pub['title']} (Sem Data)", font=('Helvetica', 12), pad=(20, 5))])

    

    layout = [
        [sg.Column(layout_autores, scrollable=True, vertical_scroll_only=True, size=(800, 500))],
        [sg.Button('Fechar', size=(10, 1), pad=(0, 20))]
    ]

    window = sg.Window('Análise por Autor', layout, modal=True, size=(800, 600), location=(100, 100))
    run = True
    while run:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Fechar':
            window.close()
            run = False

def analisar_por_palavra_chave(base):
    palavras_chave: dict[str, list[int]] = {}
    for i, pub in enumerate(base):
        if 'keywords' in pub.keys():
            pubKeyWords: list[str] = ''.join(char for char in pub['keywords'] if char not in '!.?').split(',')
            for key in pubKeyWords:
                if key[0] == ' ':
                    key = key[1:]
                if key not in palavras_chave:
                    palavras_chave[key] = [pub]
                else:
                    palavras_chave[key].append(pub)

    palavras_ordenadas = sorted(palavras_chave.items(), key=lambda x: (-len(x[1]), x[0])) 

    layout_palavras = [
        [sg.Text('Palavras-chave e Publicações', font=('Helvetica', 16), justification='center', pad=(0, 20))]
    ]

    for palavra, publicacoes in palavras_ordenadas[:20]:
        layout_palavras.append([sg.Text(f"{palavra} ({len(publicacoes)} publicações):", font=('Helvetica', 14, 'bold'), pad=(0, 10))])
        for pub in publicacoes:
            layout_palavras.append([sg.Text(f"  - {pub['title']} ({pub['publish_date']})", font=('Helvetica', 12), pad=(20, 5))])

    layout = [
        [sg.Column(layout_palavras, scrollable=True, vertical_scroll_only=True, size=(800, 500))],
        [sg.Button('Fechar', size=(10, 1), pad=(0, 20))]
    ]

    window = sg.Window('Análise por Palavra-chave', layout, modal=True, size=(800, 600), location=(100, 100))
    run = True
    while run:
        evento, values = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Fechar':
            window.close()
            run = False

# Novas Funções para Estatísticas Avançadas
def gerar_grafico_publicacoes_por_mes(base):
    # Extrair anos únicos das publicações
    anos = sorted(set(pub['publish_date'].split('-')[0] for pub in base if  'publish_date' in pub))
    
    # Layout para selecionar o ano
    layout = [
        [sg.Text('Selecione o ano:')],
        [sg.Combo(anos, key='ano')],
        [sg.Button('Gerar Gráfico'), sg.Button('Cancelar')]
    ]
    
    window = sg.Window('Distribuição de Publicações por Mês', layout)
    
    run = True
    while run:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            window.close()
            run = False
        elif event == 'Gerar Gráfico':
            ano = values['ano']
            if ano:
                meses = {str(i).zfill(2): 0 for i in range(1, 13)}
                for pub in base:
                    if 'publish_date' not in pub:
                        continue
                    data = pub['publish_date'].split('-')
                    if data[0] == ano:
                        meses[data[1]] += 1
                meses = dict(sorted(meses.items(), key= lambda tuplo: tuplo[0])[:20])
                plt.bar(meses.keys(), meses.values())
                plt.xlabel('Mês')
                plt.ylabel('Número de Publicações')
                plt.title(f'Distribuição de Publicações por Mês em {ano}')
                plt.show()
            window.close()
            run = False

def gerar_grafico_top_autores(base):
    autores = {}
    for i, pub in enumerate(base):
        if 'authors' in pub.keys():
            pubAuthors: list[str] = [nome['name'] for nome in pub['authors']]
            for author in pubAuthors:
                if author not in autores:
                    autores[author] = 0
                else:
                    autores[author] += 1
    top_autores = dict(sorted(autores.items(), key= lambda tuplo: tuplo[1], reverse=True)[:20])
    plt.barh(top_autores.keys(), top_autores.values())
    plt.xlabel('Número de Publicações')
    plt.ylabel('Autores')
    plt.title('Top 20 Autores com Mais Publicações')
    plt.gca().invert_yaxis()
    plt.show()

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
    
    # Layout para selecionar o autor
    layout = [
        [sg.Text('Selecione o autor:')],
        [sg.Combo([autor for autor in sorted(autores.keys())], key='autor')],
        [sg.Button('Gerar Gráfico'), sg.Button('Cancelar')]
    ]
    
    window = sg.Window('Distribuição de Publicações por Ano (Autor)', layout)
    
    finnished = False
    while not finnished:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            window.close()
            finnished = True
            return
        
        elif event == 'Gerar Gráfico':
            autor = values['autor']
            if autor:
                publicacoes = autores[autor]
                anos = {}
                for i in publicacoes:
                    if 'publish_date' not in base[i]:
                        continue
                    ano = base[i]['publish_date'][:4]
                    if ano not in anos:
                        anos[ano] = 1
                    else:
                        anos[ano] += 1
                anos = dict(sorted(anos.items(),key=lambda tuplo: tuplo[0])[:20])
                plt.bar(anos.keys(), anos.values())
                plt.xlabel('Ano')
                plt.ylabel('Número de Publicações')
                plt.title(f'Distribuição de Publicações de {autor} por Ano')
                plt.show()
            window.close()
            finnished = True
            return

def gerar_grafico_top_palavras_chave(base):
    palavras_chave = {}
    for i, pub in enumerate(base):
        if 'keywords' in pub.keys():
            pubKeyWords: list[str] = ''.join(char for char in pub['keywords'] if char not in '!.?').split(',')
            for key in pubKeyWords:
                if key[0] == ' ':
                    key = key[1:]
                if key not in palavras_chave:
                    palavras_chave[key] = 1
                else:
                    palavras_chave[key] += 1

    top_palavras = sorted(palavras_chave.items(), key=lambda tuplo: tuplo[1], reverse=True)[:20]
    top_palavras = dict(top_palavras)   

    plt.barh(top_palavras.keys(), top_palavras.values())
    plt.xlabel('Frequência')
    plt.ylabel('Palavras-chave')
    plt.title('Top 20 Palavras-chave mais Frequentes')
    plt.gca().invert_yaxis()
    plt.show()

def gerar_grafico_palavras_chave_por_ano(base):
    anos = sorted(set(pub['publish_date'].split('-')[0] for pub in base if 'publish_date' in pub))
    layout = [
        [sg.Text('Selecione o ano:')],
        [sg.Combo(anos, key='ano')],
        [sg.Button('Gerar Gráfico'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Palavras-chave por Ano', layout)
    finnished = False
    while not finnished:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            window.close()
            finnished = True
            return
        elif event == 'Gerar Gráfico':
            ano = values['ano']
            if ano:
                palavras_chave = {}
                publicacoes = [pub for pub in base if 'publish_date' in pub and pub['publish_date'][:4] == ano]
                for pub in publicacoes:
                        if 'keywords' not in pub.keys():
                            continue
                        pubKeyWords: list[str] = ''.join(char for char in pub['keywords'] if char not in '!.?').split(',')
                        for key in pubKeyWords:
                            if key[0] == ' ':
                                key = key[1:]
                            if key not in palavras_chave:
                                palavras_chave[key] = 1
                            else:
                                palavras_chave[key] += 1
                if palavras_chave:
                    palavras_chave = dict(sorted(palavras_chave.items(), key= lambda tuplo: tuplo[1], reverse=True)[:20])
                    plt.bar(palavras_chave.keys(), palavras_chave.values())
                    plt.xlabel('Palavras-chave')
                    plt.ylabel('Número de Publicações')
                    plt.title(f'Palavras-chave em {ano}')
                    plt.xticks(rotation=45)
                    plt.show()
                else:
                    sg.popup('Nenhuma palavra-chave encontrada para o ano especificado.', font=('Helvetica', 12), title='Resultado da Pesquisa')
            window.close()
            finnished = True
            return

def mostrar_ajuda():
    comandos = [
        "1. Adicionar Publicação",
        "2. Gerir Publicações",
        "3. Pesquisar Publicações",
        "4. Análise por Autor",
        "5. Análise por Palavra-chave",
        "6. Estatísticas de Publicação",
        "7. Mostrar Ajuda"
    ]
    sg.popup("Comandos disponíveis:", *comandos)

def importar_dados():
    caminho_importacao = sg.popup_get_file('Selecione o arquivo para importar')
    if caminho_importacao:
        novos_dados = carregar_dados(path=caminho_importacao)
        if novos_dados:
            base.extend(novos_dados)
            sg.popup('Dados importados com sucesso!')

base = carregar_dados(path=caminho_ficheiro)

# GUI Principal
def GUI_main(caminho_ficheiro='DataSet_Main.json'):
    sg.theme('DarkAmber')
    base = carregar_dados(path=caminho_ficheiro)

    layout_principal = [
        [sg.Text('Sistema de Gestão de Publicações', font=('Helvetica', 20), justification='center')],
        [sg.TabGroup([
            [sg.Tab('Gestão de Publicações', [
                [sg.Button('Adicionar Publicação')],
                [sg.Button('Apagar Publicação')],
                [sg.Button('Atualizar Publicação')],
                [sg.Text('')], [sg.Text('')], [sg.Text('')], [sg.Text('')], [sg.Text('')], [sg.Text('')],
                [sg.Push(), sg.Button('Carregar DataSet'), sg.Button('Guardar DataSet')],
            ])],
            [sg.Tab('Estatísticas', [
            [sg.Button('Distribuição por Ano')],
            [sg.Button('Distribuição por Mês')],
            [sg.Button('Top Autores')],
            [sg.Button('Publicações por Ano (Autor)')],
            [sg.Button('Top Palavras-chave')],
            [sg.Button('Palavras-chave por Ano')]
            ])],
            [sg.Tab('Pesquisar', [
                [sg.Button('Pesquisar Publicação')],
                [sg.Button('Análise do Post')],
            ])],
            [sg.Tab('Visualizar Publicações', [
                [sg.Button('Listar Publicações')]
            ])]
        ])],
        [sg.Button('Help')],
        [sg.Button('Sair')]
    ]

    executar = True
    base = carregar_dados(path=caminho_ficheiro)
    window = sg.Window('Gestor de Publicações', layout_principal, size=(800, 600))

    while executar:
        evento, _ = window.read()
        if evento == sg.WINDOW_CLOSED or evento == 'Sair':
            guardar_dados(path=caminho_ficheiro, base=base)
            executar = False
        elif evento == 'Adicionar Publicação':
            nova_publicacao = criar_publicacao()
            if nova_publicacao:
                base.append(nova_publicacao)
        elif evento == 'Apagar Publicação':
            gerenciar_publicacoes(base)
        elif evento == 'Atualizar Publicação':
            atualizar_publicacao()
        elif evento == 'Carregar DataSet':
            base = carregar_dados()
            sg.popup('Dataset carregado com sucesso!')
        elif evento == 'Guardar DataSet':
            guardar_dados(base=base)
            sg.popup('Dataset guardado com sucesso!')
        elif evento == 'Exportar Dados Parciais':
            resultados = pesquisar_publicacao()  # Supondo que esta função retorna os resultados da pesquisa
            if resultados:
                exportar_dados_parcial(resultados)
        elif evento == 'Pesquisar Publicação':
            pesquisar_publicacao()
            pass
        elif evento == 'Distribuição por Ano':
            gerar_grafico_publicacoes_por_ano(base)
        elif evento == 'Distribuição por Mês':
            gerar_grafico_publicacoes_por_mes(base)
        elif evento == 'Top Autores':
            gerar_grafico_top_autores(base)
        elif evento == 'Publicações por Ano (Autor)':
            gerar_grafico_publicacoes_por_ano_autor(base)
        elif evento == 'Top Palavras-chave':
            gerar_grafico_top_palavras_chave(base)
        elif evento == 'Palavras-chave por Ano':
            gerar_grafico_palavras_chave_por_ano(base)
        elif evento == 'Listar Publicações':
            PrintDataSet(base)
        elif evento == 'Análise do Post':
            analise_post()
        elif evento == 'Help':
            mostrar_ajuda()
        

    window.close()

if __name__ == "__main__":
    GUI_main()
