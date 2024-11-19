# RESUMO DO TPC7
## Data: 2024/10/21
## Autor: DSBR

## Resumo:

O TPC7 consistiu em criar app para trabalhar com tabelas metereológicas

FUNCIONALIDADES
* Carregar/Guardar a tabela metereológica num fucheiro .txt
* Calcular temperatura média e amplitude térmica
* Procurar pela temperatura mínima da tabela, dia com maior precipitação, com precipitação superior a um valor
* 'Dias ensularados'

Estre projeto está dividido em dois ficheiros de código python e um ficheiro .txt:
* 'TPC5_main.py' onde se encontra o main loop do programa
* 'TPC5_functions.py' onde estão defenidas todas as funções do programas
* 'metereologia.txt' onde está guardada a tabela metereológica


'metereologia.txt'
* 'ano::mês::dia::tmin::tmax::precip'
* (data) -> data relativa aos registos feitos
* tmin, tmax -> temperaturas mínima e máxima
* precip -> precipitação em mm / m^2


As funções estão divididas em grupos:
* CARREGAR / GUARDAR EM FICHEIRO .txt
    - carregaTabMeteo(fnome): carrega uma tabela de metereologia de um ficheiro .txt (retorna uma tabela)
    - guardarTabMeteo(t, fnome): guardar uma tabela em um ficheiro .txt

* MENU
    - menu(): dá print de todas as opões possiveis do programa, interface do programa

* FUNCTIONS
    - medias(t): calcula a média da temperatura diária
    - minMin(t): temperatura mínima da tabela
    - amplTerm(t): calcula a amplitude térmica diária
    - maxChuva(t): dia e valor da maior qunatidade de precipitação
    - diasChuvosos(t, p): calcula o totla de dias com precipitação assima de p
    - maxPeriodoCalor(t, p): calcula o maior número consecutivo de dias com precipitação abaixo de p

* DESENHAR GRÁFICOS
    - grafs(t): duas opções -> 1º plot da temperatura mínima e máxima 2º bar plot dos valores de precipitação
