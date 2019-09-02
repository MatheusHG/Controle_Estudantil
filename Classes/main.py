#Arthur Stevam 
#Sexta - Feira, 30 de Agosto de 2019
#Classe Principal

from Classes.aluno import Aluno
from Classes.turma import Turma
alunos = []

def matricularaluno():
    nome = str(input('Nome do Aluno: '))
    rg = str(input('RG: '))
    cpf = str(input('CPF: '))
    data_nascimento = str(input('Data de Nascimento: '))
    aluno = Aluno(nome, data_nascimento, cpf, rg)
    alunos.append(aluno)

def menu():
    while True:
        print('1 - Matricular Aluno')
        print('2 - Criar Turma')
        print('3 - Adicionar Notas')
        print('4 - Adicionar Falta')
        print('5 - Verificar Situação dos alunos')
        print('6 - Verificar Aprovados/Reprovados e Finalistas')
        print('7 - Encerrar Turma')
        opcao = int(input())

        if opcao == 1:
            matricularaluno()
        elif opcao == 2:
            faltas = int(input('Qual limite de faltas da turma? '))
            turma = Turma(alunos, faltas)
            print('Turma criada!')
        elif opcao == 3:
            turma.adicionarNotas()
        elif opcao == 4:
            nome = str(input('Qual nome do aluno? '))
            for a in alunos:
                if a.nome == nome:
                    a.adicionarFalta()
        elif opcao == 5:
            turma.getSituacaoAlunos()
        elif opcao == 6:
            notas = int(input('Quantas notas foram dadas aos alunos? '))
            turma.verificaFinal(notas)
        elif opcao == 7:
            turma.encerrarturma()

menu()