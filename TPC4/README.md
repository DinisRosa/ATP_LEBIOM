# RESUMO DO TPC4
## DATA: 30/09/2024
## AUTOR: DSBR

## RESUMO:

Este trabalho teve o intuito de trabalhar com listas de ints
Tivemos de criar várias funções de manipulação de listas de ints, tais como:
(Estas são para a criação da lista interna)
* inputList() e randomList() que criam listas, a primeira em que o operador dá um número maximo de valores e depois indica N ints para ser a lista interna, o outro pede na mesma o N mas é o pc que 'escolhe' os valores usando random.randint(0,100)

(Estas recebem a lista interna e devolvem um int ou str)
* somaList(list), devolve a soma da lista
* meanList(list), devolve a média da lista
* maxList(list) ou minList(list), devolvem, respetivamente o maior e menor int da lista
* isMintoMax(list) ou isMaxtoMin(list), devolvem 'SIM' ou 'NÃO' se a lista estiver, respetivamente, por ordem crescente ou decrescente

(Esta recebe a lista interna e um int)
* findElement(list, elem), devolve o index da primeira aparição do elem na lista, se não existir na lista devolve -1

MAIN LOOP
* função menu() que dá um print de todas as opões possiveis do programa, interface do programa

(while op != 0)
* 'op' recebe o int(input) do usuário com o número da opção que quer realizar, 1 to 9
* se op = 0, o programa sai do loop e despede-se do usuário


