#Create Menu:

def menu():
    print('''zdsdfsdfsd
Bem vindo ao jogo dos 21 Fósforos!
Neste jogo, tu e o computador, á vez, podem tirar 1, 2, 3 ou 4 fósforos.
Se ficares com o último fósforo perdes!
    a) Ser o primeiro a jogar
    b) Ser o segundo a jogar
    c) Sair
    ''')


#O jogador começa:

def PlayerStart():
    #em normal e branco \033[0;30m -> cor base do terminal
    #em negrito e branco \033[1;30m -> cor do número de fósforos
    #em negrito e vermelho \033[1;31m -> resposta inválida do jogador
    #em negrito e amarelo \033[1;33m -> cor do final
    #em negrito e azul \033[1;34m -> cor do jogador
    #em negrito e roxo \033[1;35m -> cor do pc
    
    total_fosforos = 21
    while total_fosforos > 1:
        player_turn = int(input('\033[0;34mO teu turno, quantos fósforos queres tirar: '))
        while player_turn < 1 or player_turn > min(4,total_fosforos):
            print(f'\033[1;31mNão é possível tirar esse número de fósforos! Por favor tire de 1 a {min(4,total_fosforos)} fósforos')
            player_turn = int(input('\033[0;34mO teu turno, quantos fósforos queres tirar: '))
        total_fosforos -= player_turn
        print(f'\033[1;30mFicaram/Ficou {total_fosforos} fósforos')
        total_fosforos -= (5 - player_turn) 
        print(f'\033[0;35mO pc tirou {5 - player_turn} fósforos!\n\033[1;30mFicaram/Ficou {total_fosforos} fósforos')
    print('\033[1;33mO pc ganhou! Boa sorte para a próxima!\033[0;30m')



# O pc começa:

import random as rd

def PcStart():
    total_fosforos = 21
    pc_turn = rd.randint(1, 4)
    total_fosforos -= pc_turn
    print(f'\033[0;35m{pc_turn}\n\033[1;30mT = {total_fosforos}')

    playerWin = False
    gameOver = False

    while total_fosforos > 1 and not gameOver:
        #plogica para o player
        player_turn = int(input('\033[0;34mO teu turno, quantos fósforos queres tirar: 1, 2, 3 ou 4: '))
        while player_turn < 1 or player_turn > min(4,total_fosforos):
            print(f'\033[1;31mNão é possível tirar esse número de fósforos! Por favor tire de 1 a {min(4,total_fosforos)} fósforos')
            player_turn = int(input('\033[0;34mO teu turno, quantos fósforos queres tirar: '))

        total_fosforos -= player_turn
        print(f'\033[1;30mT = {total_fosforos}')


        if total_fosforos == 1:
            gameOver = True
            playerWin = True
        else:
            #logica do PC
            if total_fosforos <= 5:
                pc_turn = total_fosforos - 1
            else:
                if total_fosforos % 5 == 1:
                    pc_turn = rd.randint(1, 4)
                else:
                    pc_turn = abs(3 - (total_fosforos % 5))
            
            total_fosforos -= pc_turn
            print(f'\033[0;35m{pc_turn}\n\033[1;30mT = {total_fosforos}')


            if total_fosforos == 1:
                gameOver = True
                playerWin = False
            

    if playerWin:
        print('\033[1;33mGanhaste! PARABENS!!!!')
    else:
        print('\033[1;33mO pc ganhou! Boa sorte para a próxima!\033[0;30m')        





def PcStart2():
    gameOver = False

    total_fosforos = 21
    pc_turn = rd.randint(1, 4)
    total_fosforos -= pc_turn
    print(f'\033[0;35m{pc_turn}\n\033[1;30mT = {total_fosforos}')

    player_turn = int(input('\033[0;34mO teu turno, quantos fósforos queres tirar: 1, 2, 3 ou 4: '))
    while player_turn < 1 or player_turn > min(4, total_fosforos):
        print(f'\033[1;31mNão é possível tirar esse número de fósforos! Por favor tire de 1 a {min(4, total_fosforos)} fósforos')
        player_turn = int(input('\033[0;34mO teu turno, quantos fósforos queres tirar: '))
    
    total_fosforos -= player_turn
    print(f'\033[1;30mT = {total_fosforos}')

    while total_fosforos > 1 and not gameOver:
        if pc_turn + player_turn != 5:
            pc_turn = 5 - (total_fosforos % 5)
        

        total_fosforos -= pc_turn
        print(f'\033[0;35m{pc_turn}\n\033[1;30mT = {total_fosforos}')

#O JOGO:

menu()
modo_de_jogo = input('Que é que deseja fazer? ')
while modo_de_jogo != 'c':
    if modo_de_jogo == 'a':
        PlayerStart()
        menu()
        modo_de_jogo = input('Que é que deseja fazer?')
    elif modo_de_jogo == 'b':
        print('In development')
        PcStart()
        menu()
        modo_de_jogo = input('Que é que deseja fazer?')
    else:
        print('Opcão inválida Escolha uma opção válida, por favor!')
        modo_de_jogo = input('Que é que deseja fazer?')
print('Obrigado! Volte sempre!')
