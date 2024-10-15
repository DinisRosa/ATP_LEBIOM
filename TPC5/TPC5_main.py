from TPC5_functions import *


#INICIALIZANDO O CINEMA
CINEMA = lerCinema('lista_de_cinemas.txt')
FILME = ''
LUGAR = -1
OCCUPIED_CHAIRS = []


#MAIN CODE
op = menu()
while op != 0:
    if CINEMA == [] and (op != 2 or 0):
        op = int(input('''CINEMA SEM SALAS!
    (2) Adicionar sala e respetivo filme
    (0) Sair
'''))
    else:
        #(1) Listar filmes
        if op == 1:
            showCinema(CINEMA)

        #(2) Adicionar filmes
        elif op == 2:
            Filme = str(input('Que filme quer adicionar: '))
            TotalLugares = int(input('Número total de lugares: '))
            sala = [Filme, TotalLugares, []]
            CINEMA = addMovie(CINEMA, sala)

        #(3) Escolher filme para ver
        elif op == 3:
            showMovies(CINEMA)
            numFILME = int(input('Escolha um filme da lista, digitando o número: '))
            if numFILME > len(CINEMA):
                print('Número não existe, digite número válido.')
            else:
                print(CINEMA[numFILME - 1][0])
                FILME = CINEMA[numFILME - 1][0]
                

        #(4) Listar lugares ocupados na sala
        elif op == 4:
            if FILME != '':
                OCCUPIED_CHAIRS = occupiedChairs(CINEMA, FILME)
            else:
                print('Escolha um filme primeiro.')

        #(5) Escolher lugar
        elif op == 5:
            LUGAR = int(input('Digite o lugar que quer escolher: '))
            if LUGAR not in OCCUPIED_CHAIRS and LUGAR < CINEMA[filmeExiste(CINEMA, FILME)][1]:
                verLugaresOcupados(CINEMA, FILME, LUGAR)
                print(f'Guardou o lugar {LUGAR} para o filme {FILME}')
            else: 
                print(f'Lugar {LUGAR} já ocupado ou não existe! Escolha outro!')
            
        #(6) Retirar marcação do filme
        elif op == 6:
            if LUGAR != -1 and FILME != '':
                print(f'A sua marcação do lugar {LUGAR} no filme {FILME} vai ser removida!')
                CINEMA = retirarLugar(CINEMA, FILME, LUGAR)
                LUGAR = -1
                FILME = ''
            else:
                print('Não podemos remover a sua marcação porque não temos nenhuma!')
                
        op = menu()
        guardarCinema('lista_de_cinemas.txt', CINEMA)

print('OBRIGADO, volte sempre!')