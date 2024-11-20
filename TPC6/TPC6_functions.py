import json


#MENU
def menu():
    print('''Bem vindo á app de turmas:
    (1) Criar uma turma
    (2) Inserir um aluno na turma
    (3) Listar turmas
    (4) Consultar um aluno por id
    (5) Guardar a turma em ficheiro
    (6) Carregar uma turma dum ficheiro
    (0) Sair da aplicação
''')
    return int(input('O que deseja fazer? '))


#FUNCTIONS
def adicionarTurma(listaDeTurmas: dict):
    nomeDaTurma = input('Qual o nome da turma? ')
    if nomeDaTurma not in listaDeTurmas.keys():
        classRoom = {
            "className": nomeDaTurma,
            "alunos": []
        }
        print(f'A turma {nomeDaTurma} foi criada!')
        listaDeTurmas[nomeDaTurma] = classRoom
    else:
        print(f'Turma {nomeDaTurma} já existe!!')
    return listaDeTurmas


def adicionarAluno(listaDeTurmas: dict):
    print(f'Turmas existentes: {[t for t in listaDeTurmas.keys()]}')
    nomeDaTurma = input('Qual o nome da turma em que quer adicionar um aluno? ')

    if nomeDaTurma in [t for t in listaDeTurmas.keys()]: 
        aluno = {
            "id": input('Qual o ID do aluno: '),
            "nomeAluno": input('Qual o nome do aluno: '),
            "notas": (int(input('Qual a nota dos TPCs: ')),
                    int(input('Qual a nota do projeto final: ')),
                    int(input('Qual a nota do teste: ')))
        }
        if aluno not in listaDeTurmas[nomeDaTurma]['alunos']:
            listaDeTurmas[nomeDaTurma]['alunos'].append(aluno)
            print(f'O aluno {aluno["nomeAluno"]} foi adicionado á turma {nomeDaTurma}!')
        else:
            print(f'O aluno {aluno["nomeAluno"]} já exite!')
    else:
        print(f'Turma {nomeDaTurma} não existe!')
    return listaDeTurmas


def listarTurmas(listaDeTurmas: dict):
    for turma in listaDeTurmas:
        print(f'----Turma {listaDeTurmas[turma]['className']}----')
        for aluno in listaDeTurmas[turma]['alunos']:
            print(
f'''Nome: {aluno['nomeAluno']}
ID: {aluno['id']}
Notas: TPCs- {aluno['notas'][0]}; PF- {aluno['notas'][1]}; T- {aluno['notas'][2]}
-----''')



def procurarAlunoPorID(listaDeTurmas: dict):
    idAluno = input('Qual o id do aluno que quer procurar? ')
    alunoExiste = False
    for turma in listaDeTurmas:
        for aluno in listaDeTurmas[turma]['alunos']:
            if aluno['id'] == idAluno:
                alunoExiste = True
                print(
f'''Turma: Turma {turma}
Nome: {aluno['nomeAluno']}
ID: {aluno['id']}
Notas: TPCs- {aluno['notas'][0]}; PF- {aluno['notas'][1]}; T- {aluno['notas'][2]}''')
    if not alunoExiste:
        print(f'Aluno com ID: {idAluno} não exite!')


#GUARDAR/CARREGAR turma em .txt
def guardarTurma(listaDeTurmas: dict):
    print(f'Turmas existentes: {[t for t in listaDeTurmas.keys()]}')
    nomeDaTurma = input('Qual o nome da turma que quer guardar? ')
    fnome = f'./TPC6/Turma_{nomeDaTurma}.txt'
    file = open(fnome, 'w')
    for aluno in listaDeTurmas[nomeDaTurma]['alunos']:
        linha = f'{nomeDaTurma}::{aluno['id']}::{aluno['nomeAluno']}::{aluno['notas'][0]}::{aluno['notas'][1]}::{aluno['notas'][2]}\n'
        print(linha)
        file.write(linha)
    file.close()


def carregarTurma(listaDeTurmas):
    nomeDaTurma = input('Qual o nome da turma que quer carregar? ')
    if nomeDaTurma not in listaDeTurmas.keys():
        fnome = f'./TPC6/Turma_{nomeDaTurma}.txt'
        file = open(fnome, 'r')
        listaDeAlunos = []
        for linha in file:
            params = linha.split('::')
            aluno = {
            "id": params[1],
            "nomeAluno": params[2],
            "notas": (int(params[3]), int(params[4]), int(params[5]))
            }
            listaDeAlunos.append(aluno)
        classRoom = {
            "className": nomeDaTurma,
            "alunos": listaDeAlunos
        }
        listaDeTurmas[nomeDaTurma] = classRoom
        print(f'Turma {nomeDaTurma} adicionada com sucesso!')
    else:
        print(f'Turma {nomeDaTurma} já exite!')
    return listaDeTurmas

