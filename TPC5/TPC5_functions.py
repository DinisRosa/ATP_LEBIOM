#MENU
def menu():
    print('''
BEM VINDO ao Cinema!
    (1) Listar filmes
    (2) Adicionar filmes
    (3) Escolher filme para ver
    (4) Listar lugares ocupados na sala
    (5) Escolher lugar
    (6) Retirar lugar/marcação

    (0) Sair
''')
    return int(input('O que deseja fazer? '))



#FUNÇÕES PRINCIPAIS
def showCinema(cinema):
    maxstring = maxLenString(cinema)
    linha(maxstring + 39)
    print('CINEMA'.center(maxstring + 39))
    linha(maxstring + 39)
    print('Filme'.center(maxstring) + '          Lugares Totais           Sala')
    linha(maxstring + 39)
    i = 1
    for sala in cinema:
        print(str(sala[0]).center(maxstring) + str(sala[1]).center(34) + str(i).center(5))
        i += 1
    linha(maxstring + 39)
    return

def showMovies(cinema):
    maxstring = maxLenString(cinema)
    offset = len(cinema) // 10 + 3
    linha(maxstring + offset)
    for i, sala in enumerate(cinema):
        print(f'({i + 1}) {sala[0]}'.center(maxstring))
    linha(maxstring + offset)
    return

def occupiedChairs(cinema, filme):
    idx = filmeExiste(cinema, filme)
    if idx != -1:
        lugaresPorOrdem = ordenaNumeros(cinema[idx][2])
        if cinema[idx][2] != []:
            print(f'Os lugares ocupados da sala do filme {cinema[idx][0]} são: {lugaresPorOrdem}')
        else:
            print(f'O filme {cinema[idx][0]} ainda não tem espectadores. Pode escolher qualquer lugar da sala!')
    else:
        print(f'Não existe sala para o filme {filme}')
    return lugaresPorOrdem

def addMovie(cinema, sala):
    cinema.append(sala)
    return cinema

def verLugaresOcupados(cinema, filme, lugar):
    cinema[filmeExiste(cinema, filme)][2].append(lugar)
    return ordenaLugares(cinema)

def retirarLugar(cinema, filme, lugar):
    for idx, l in enumerate(cinema[filmeExiste(cinema, filme)][2]):
        if l == lugar:
            cinema[filmeExiste(cinema, filme)][2].pop(idx)
    return cinema


#Funções auxiliares
def filmeExiste(cinema, filme):
    idx = -1
    i = 0
    while idx == -1 and i < len(cinema):
            if cinema[i][0] == filme:
                idx = i
    return idx

def ordenaNumeros(lista):
    changes = True
    while changes:
        changes = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                changes = True
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista

def ordenaLugares(cinema):
    for sala in cinema:
        sala[2] = ordenaNumeros(sala[2])
    return cinema

def maxList(list):
    max = list[0]
    for l in list[1:]:
        if l > max:
            max = l
    return max

def maxLenString(list):
    string_len = [len(s[0]) for s in list]
    return maxList(string_len)

def linha(len=44):
    print('-' * len)
    return


#LER / GUARDAR AS SALAS DE CINEMA NO FICHEIRO .txt
def guardarCinema(nomeCinematxt, cinema):
    fichero = open(nomeCinematxt, 'w')
    for sala in cinema:
        lugaresOcupados = ''
        if sala[2] != []:
            for lugar in sala[2]:
                lugaresOcupados+=  '::' + str(lugar)
        else:
            lugaresOcupados = '::-1'
        fichero.write(f'{sala[0]}::{sala[1]}'+ lugaresOcupados + '\n')
    fichero.close()
    return

def lerCinema(nomeCinematxt):
    fichero = open(nomeCinematxt, 'r+')
    CINEMA = []
    for linha in fichero:
        if linha != '\n':
            sala = linha.strip('\n').split('::')
            sala[0] = str(sala[0])
            sala[1] = int(sala[1])
            
            lugaresOcupados = []
            if sala[2] != '-1':
                for i in sala[2:]:
                    lugaresOcupados.append(int(i))
                    sala.remove(i)
            else:
                sala.remove('-1') 
            sala.append(lugaresOcupados)
            CINEMA.append(sala)
    return CINEMA