def menu():
    print('MENU:\n1) pot(a,b)\n2) divisao(a,b)\n3) resto(a,b)\n4) serie(b,s,n)\n5) Sair')

def pot(a,b):
    result = 1
    while b > 0:
        result *= a
        b -= 1
    return result


menu()
op = input('Selecione a opção desejada: ')
while op != '5':
    if op == '1':
        a = int(input('digite a base'))
        b = int(input('digite a potência'))
        print(pot(a,b))
    #igual para as outras opções

    menu()
    op = input('Selecione a opção desejada: ')

print('Obrigado, volte sempre!')