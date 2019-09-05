##Arthur Stevam
##Terça - Feira, 03 de Agosto de 2019
##Controller

from bd.acesso_bd import banco_de_dados
from Classes.aluno import Aluno
from Classes.nota import Nota
from Classes.turma import Turma
import re

cpf_formato = r'\d{3}.\d{3}.\d{3}-\d{2}'
nome_formato = r'([A-Z][a-z]+\s)+'
matricular = []
bd = banco_de_dados()

def veralunos():
    try:
        lista_alunos = bd.gettodosalunos()
        aluno = Aluno("", "")
        for a in lista_alunos:
            print('-'*50)
            aluno.recebeentidade(a)
            print(f'{aluno.get_matricula()} - {aluno.get_nome()}')
        print('-'*50)
    except:
        print('Erro ao tentar acessar dados. Tente novamente mais tarde!')

def verturmas():
    try:
        lista_turmas = bd.getturmas()
        turma = Turma(0)
        for t in lista_turmas:
            turma.recebeentidade(t)
            print(turma.get_codigo_turma())
    except:
        print('Erro ao tentar acessar dados. Tente novamente mais tarde!')

def criarturma():
    faltas = int(input('Qual será o limite de faltas da turma? '))
    turma = Turma(faltas)
    turma.salvar()
    turma.matricularalunos(matricular)
    matricular.clear()

def criaraluno():
    print('-' * 50)
    print('Matricular Aluno')
    while True:
        nome = str(input('Nome Completo: '))
        if re.match(nome_formato, nome): break
        else: print('Digite um nome válido!')
    while True:
        cpf = str(input('CPF (000.000.000-00): '))
        if re.match(cpf_formato, cpf): break
        else: print('Formato de cpf deve estar correto 000.000.000-00')
    aluno = Aluno(nome, cpf)
    aluno.salvar()
    matricular.append(aluno)

