# RESUMO DO TPC6
## Data: 2024/11/19
## Autor: DSBR

## Resumo:

O TPC6 consistiu na realização de um programa de administração de turmas


FUNCIONALIDADES
* Carregar/Guardar uma turma num fucheiro .txt
* Criar uma turma nova
* Adicionar um aluno a uma turma
* Listar os alunos de todas as turmas
* Procurar um aluno pelo seu ID


Este TPC está dividido em 2 ficheiros .py e 1 ficheiro .txt
* 'TPC6_main.py' onde se encotra o main loop do programa
* 'TPC6_functions.py' onde estão definidas todas as funções do programa
* 'Turma_A2.txt' é um ficheiro de exemplo de como é guardada uma turma


'Turma_A2.txt'
* este ficheiro tem como base 'Turma_X.txt' onde o X é o nome da turma; ex: Turma_A.txt; Turma_1234.txt
* representa apenas 1 turma
* nomeTurma::id::nomeAluno::notaTPC::notaTeste::notaPF


As funções estão divididas em grupos:
* CARREGAR / GUARDAR EM FICHEIRO .txt
    - carregarTurma(listaDeTurmas: dict): carrega uma turma de um ficheiro .txt (retorna a listaDeTurmas com a Turma adicionada)
    - guardarTurma(listaDeTurmas: dict): guardar uma turma em um ficheiro .txt

* MENU
    - menu(): dá print de todas as opões possiveis do programa, interface do programa

* FUNCTIONS
- LISTA_TURMAS: dicionário que representa todas as turmas, inicializado vazio
    - adicionarTurma(listaDeTurmas: dict): pede um nome de turma e adiciona essa turma com uma lista de alunos vazia
    - adicionarAluno(listaDeTurmas: dict): pede um nome de aluno, id, notas e adiciona a uma determinada turma
    - listarTurmas(listaDeTurmas: dict): escreve no ecrã de forma formatada os alunos de cada turma
    - procurarAlunoPorID(listaDeTurmas: dict): pede um ID e procura por todas as turmas por esse aluno
