import random

#Create Menu:

def menu():
    print('''
Bem vindo ao jogo dos 21 Fósforos!
Neste jogo, tu e o computador, á vez, podem tirar 1, 2, 3 ou 4 fósforos.
Se ficares com o último fósforo perdes!
    (1) Ser o primeiro a jogar
    (2) Ser o segundo a jogar

    (0) Sair
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
            print(f'\033[1;31mNão é possível tirar esse número de fósforos! Por favor tire de 1 a {min(4,total_fosforos)} fósforos.')
            player_turn = int(input('\033[0;34mO teu turno, quantos fósforos queres tirar: '))
        total_fosforos -= player_turn
        print(f'\033[1;30mFicaram/Ficou {total_fosforos} fósforos.')
        total_fosforos -= (5 - player_turn) 
        print(f'\033[0;35mO pc tirou {5 - player_turn} fósforos!\n\033[1;30mFicaram/Ficou {total_fosforos} fósforos.')
    print('\033[1;33mO pc ganhou! Boa sorte para a próxima!]\033[0;30m]')


# O pc começa:

def PcStart():
    total_fosforos = 21
    pc_turn = random.randint(1, 4)
    total_fosforos -= pc_turn
    print(f'\033[0;35m{pc_turn}\n\033[1;30mFicaram {total_fosforos} fosforos \033[m')


    while total_fosforos > 1:
        #logica para o player
        player_turn = int(input('\033[0;34mO teu turno, quantos fósforos queres tirar: 1, 2, 3 ou 4:\033[m '))
        while player_turn < 1 or player_turn > min(4,total_fosforos):
            print(f'\033[1;31mNão é possível tirar esse número de fósforos! Por favor tire de 1 a {min(4,total_fosforos)} fósforos.\033[m')
            player_turn = int(input('\033[0;34mO teu turno, quantos fósforos queres tirar:\033[m '))

        total_fosforos -= player_turn
        print(f'\033[1;30mFicaram {total_fosforos} fosforos \033[m')


        if total_fosforos == 1:
            print('\033[1;33mGanhaste! PARABENS!!!!\033[m')
        else:
            #logica do PC
            if total_fosforos % 5 == 1:
                pc_turn = random.randint(1,4)
            else:
                if (total_fosforos + player_turn) % 5 == 1:
                    pc_turn = 5 - player_turn
                else:
                    if total_fosforos < 5:
                        player_turn = total_fosforos - 1
                    else:
                        pc_turn_prev = pc_turn
                        if pc_turn + player_turn < 5:
                            pc_turn = 5 - (player_turn + pc_turn_prev)
                        else:
                            pc_turn = 10 - (pc_turn_prev + player_turn)

                  
            total_fosforos -= pc_turn
            print(f'\033[0;35m{pc_turn}\n\033[1;30mFicaram {total_fosforos} fosforos \033[m')

            if total_fosforos == 1:
                print('\033[1;33mO pc ganhou! Boa sorte para a próxima!\033[m')

#O JOGO:

menu()
op = int(input('Que é que deseja fazer? '))
while op != 0:
    if op == 1:
        PlayerStart()
    elif op == 2:
        PcStart()
    else:
        print('Opcão inválida Escolha uma opção válida, por favor!')
    menu()
    op = int(input('Que é que deseja fazer? '))
print('Obrigado! Volte sempre!')
