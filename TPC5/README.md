# RESUMO DO TPC5
## Data: 2024/10/07
## Autor: DSBR

## Resumo:

O TPC5 consistiu em criar uma aplicação para um cinema onde se pode:
* adicionar cinemas
* adicionar tamanho da sala
* saber quais os lugares ocupados da sala
* adicionar/remover marcação de lugar


Estre projeto está dividido em dois ficheiros de código python e um ficheiro .txt:
* 'TPC5_main.py' onde se encontra o main loop do programa
* 'TPC5_functions.py' onde estão defenidas todas as funções do programas
* 'lista_de_cinemas.txt' onde est+a guardado todo o cinema (nomes de filmes, total de lugares e lugares ocupados)


'lista_de_cinemas.txt'
* 'nomeFilme::maxLugares::ints'
* nomeFilme -> corresponde ao nome do filme
* maxLugares -> corresponde ao total de lugares disponiveis
* ints -> correspode aos lugares ocupados do filme, -1 se não houver nenhum (defalt) ou ints separados entre si por '::'


As funções estão divididas em grupos:
* LER / GUARDAR AS SALAS DE CINEMA NO FICHEIRO .txt
- lerCinema(nomeCinematxt): criação da função que cria ou lê um ficheiro .txt (retorna um cinema)
- guardarCinema(nomeCinematxt, cinema): guardar um cinema em um ficheiro .txt


* MENU
- menu(): dá print de todas as opões possiveis do programa, interface do programa


* FUNÇÕES PRINCIPAIS
- showCinema(cinema): mostra no ecrã uma 'tabela' com os vários filmes, sala e total máximo de lugares
- showMovies(cinema): mostra apenas os filmes que estão no cinema
- occupiedChairs(cinema, filme): lista os lugares que estão ocupados para um respetico filme
- addMovie(cinema, sala): adiciona uma sala com filme e máximo de lugares. considera sala vazia, sem lugares ocupados
- addOccupChair(cinema, filme, lugar): adiciona uma marcação de lugar num determinado filme
- retirarLugar(cinema, filme, lugar): remove uma marcação de lugar num determinado filme


* FUNÇÕES AUXILIARES (são usadas na criação das funções principais, não aparecem no main loop do programa)
- filmeExiste(cinema, filme): retorna o idx de um determinado filme
- ordenaNumeros(lista): retorna a lista de ints por ordem crescente
- ordenaLugares(cinema): usando a função acimaa, ordena os lugares ocupados de todas as salas do cinema
- maxList(list): retorna o maior int de uma lista
- maxLenString(list): retorna o número de caracteres do filme com maior nome 
- linha(len=44): desenha uma linha de '-' com uma certe len