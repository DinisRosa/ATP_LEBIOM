import matplotlib.pyplot as plt


#MENU
def menu():
    print('''Bem vindo,
    (1) Carregar tabela metereológica
    (2) Guardar tabela metereológica
    (3) Calcular temperatura média de cada dia
    (4) Temperatura mínima mais baixa registrada na tabela
    (5) Calcular amplitude térmica
    (6) Dia com maior precipitação
    (7) Dias com precipitação maior que:
    (8) Maior número de dias com precipitação menor que:
    (9) Desenhar gráficos:
    (0) Sair
''')
    return int(input('O que deseja fazer? '))

#CARREGAR / GUARDAR EM FICHEIRO .txt
def carregaTabMeteo(fnome):
    tabela = []
    file = open(fnome, 'r')
    for linha in file:
        vals = linha.split('::')
        obj = ((int(vals[0]), int(vals[1]), int(vals[2])), float(vals[3]), float(vals[4]), float(vals[5]))
        tabela.append(obj)
    file.close()
    return tabela

def guardarTabMeteo(t, fnome):
    file = open(fnome, 'w')
    for data, min, max, precip in t:
        linha = f'{data[0]}::{data[1]}::{data[2]}::{min}::{max}::{precip}\n'
        file.write(linha)
    file.close()
    return

#FUNCTIONS
def medias(t):
    res = []
    for dia in t:
        mediaTemp = (dia[1] + dia[2]) / 2
        res.append((dia[0], mediaTemp))
    return res

def minMin(t):
    min = t[0][1]
    for i in range(len(t)-1):
        if t[i][1] < min:
            min = t[i][1]
    return min

def amplTerm(t):
    res = []
    for dia in t:
        ampTemp = dia[2] - dia[1]
        res.append((dia[0], amplTerm))
    return res

def maxChuva(t):
    max_prec = t[0][3]
    max_data = t[0][0]
    for i in range(len(t)-1):
        if t[i][3] >= max_prec:
            max_prec = t[i][3]
            max_data = t[i][0]
    return (max_data, max_prec)

def diasChuvosos(t, p):
    res = []
    for obj in t:
        if obj[3] >= p:
            res.append((obj[0], obj[3]))
    return res

def maxPeriodoCalor(t, p):
    consec = 0
    max_consec = 0
    for _, _, _, precip in t:
        if precip < p:
            consec +=1
        else:
            if consec > max_consec:
                max_consec = consec
            consec = 0
    return max_consec

#DESENHAR GRÁFICOS
def grafs(t):
    print('''Tipos de gráficos:
    (1) Gráfico de temperaturas mínimas e máximas
    (2) Gráfico de pluviosidade
''')
    op = int(input('Que gráfico deseja desenhar? '))
    if op == 1:
    #GRAF1
        plt.title('Temperatura mínima e máxima')
        plt.xlabel('DATAS')
        plt.ylabel('Temperatura miníma e máxima')
        #DADOS
        datas = [str(data) for data,*_ in t]
        tempMIN = [tmin for _, tmin, _, _ in t]
        tempMAX = [tmax for _, _, tmax, _ in t]
        #TIPO DE GRÁFICO
        plt.plot(datas,tempMIN, label = 'tempMin')
        plt.plot(datas, tempMAX, label = 'tempMax')

        plt.legend()
        plt.show()
    elif op == 2:
    #GRAF2
        plt.title('Pluviosidade')
        plt.xlabel('DATAS')
        plt.ylabel('Precipitação (mm / m^2)')
        #DADOS
        datas = [str(data) for data,*_ in t]
        precipVal = [precipVal for _, _, _, precipVal in t]
        #TIPO DE GRÁFICO
        plt.bar(datas,precipVal)
        plt.show()
    else:
        print('Opção inválida!')
    return