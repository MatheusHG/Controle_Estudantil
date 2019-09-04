#Arthur Stevam 
#Sexta - Feira, 30 de Agosto de 2019
#Classe Principal

from Classes.aluno import Aluno
from Classes.turma import Turma
from Classes.nota import Nota
from bd.acesso_bd import banco_de_dados
import re

cpf_formato = r'\d{3}.\d{3}.\d{3}-\d{2}'
nome_formato = r'([A-Z][a-z]+\s)+'

bd = banco_de_dados()
matricular = []

def matricularaluno():
    print('-' * 50)
    print('Matricular ALuno')
    while True:
        nome = str(input('Nome Completo: '))
        if re.match(nome_formato, nome): break
        else: print('Digite um nome válido!')
    while True:
        cpf = str(input('CPF (000.000.000-00): '))
        if re.match(cpf_formato, cpf): break
        else: print('Formato de cpf deve estar correto 000.000.000-00')
    aluno = Aluno(nome, cpf)
    aprovado = 1 if aluno.aprovado is True else 0
    try:
        bd.insertaluno(aluno.matricula, aluno.nome, aluno.cpf, aprovado)
        print('ALuno matriculado com sucesso!')
        matricular.append(aluno)
    except:
        print('Erro ao tentar salvar aluno. Tente novamente mais tarde!')

def veralunos():
    try:
        lista_alunos = bd.gettodosalunos()
        aluno = Aluno("", "")
        for a in lista_alunos:
            print('-'*50)
            aluno.recebeentidade(a)
            print(f'{aluno.matricula} - {aluno.nome}')
        print('-'*50)
    except:
        print('Erro ao tentar acessar dados. Tente novamente mais tarde!')

def verturmas():
    try:
        lista_turmas = bd.getturmas()
        turma = Turma(True)
        for t in lista_turmas:
            turma.turmaidentidade(t)
            print(turma.codigo_turma)
    except:
        print('Erro ao tentar acessar dados. Tente novamente mais tarde!')

def criarturma():
    faltas = int(input('Qual será o limite de faltas da turma? '))
    turma = Turma(faltas)
    try:
        bd.insertturma(turma.codigo_turma, turma.limiteFaltas, turma.estado, turma.notas)
        quantidade_alunos = 0
        for a in matricular:
            bd.insertmatricula(a.matricula, turma.codigo_turma)
            quantidade_alunos += 1
        bd.conn.commit()
        matricular.clear()
        print(f'Turma criada com sucesso!\n{quantidade_alunos} matriculados na turma')
    except:
        print('Erro ao salvar turma. Tente novamente mais tarde!')

def infoturma():
    codigo = str(input('Informe o código da turma: '))
    try:
        lista_alunos = bd.getalunos(codigo)
        aluno = Aluno("", "")
        for a in lista_alunos:
            matricula = a[0]
            aluno.recebeentidade(bd.getaluno(matricula))
            print(aluno.nome)
    except:
        print('Erro ao tentar acessar dados. Tente novamente mais tarde!')

def adicionarnotas():
    verturmas()
    codigo = str(input('Informe o código da turma: '))
    try:
        lista_aluno = bd.getalunos(codigo)
        aluno = Aluno("", "")
        turma = Turma(True)
        turma.turmaidentidade(bd.getturma(codigo))
        id = turma.notas
        for a in lista_aluno:
            aluno.recebeentidade(bd.getaluno(a[0]))
            while True:
                nota = float(input(f'Nota de {aluno.nome}: ')) ## a[0] pega a matrícula do aluno
                peso = float(input(f'Peso da nota (0 para média aritmética): '))
                if 0 <= nota <= 10  and (peso == 0 or 10 <= peso  <= 100) : break
            bd.isertnota(id, aluno.matricula, turma.codigo_turma, nota, peso)
            print('-'*50)
        id += 1
        bd.updatequantidadenotas(turma.codigo_turma, id)
    except:
        print('Erro ao salvar turma. Tente novamente mais tarde!')

def deletarnotas():
    verturmas()
    codigo = str(input('Informe o código da turma: '))
    id = int(input('Informe o numero da avaliação a ser excluída: '))
    try:
        bd.deletenota(id, codigo)
        turma = Turma(True)
        turma.turmaidentidade(bd.getturma(codigo))
        id = turma.notas
        id -= 1
        bd.updatequantidadenotas(codigo, id)
    except:
        print('Erro ao tentar deletar notas. Tente novamente mais tarde!')

def verificaralunos(turma):
    try:
        s = ""
        lista_alunos = bd.getalunos(turma)
        aluno = Aluno("","")
        for a in lista_alunos:
            aluno.recebeentidade(bd.getaluno(a[0]))
            lista_notas = bd.getnotas(turma, aluno.matricula)
            nota = Nota(0, 0)
            quantidade = 0
            soma = 0
            tipo = 0
            for n in lista_notas:
                nota.recebeidentidade(n)
                if nota.peso == 0 or tipo == 1:
                    quantidade += 1
                    soma += nota.nota
                    tipo = 1
                else:
                    soma += (nota.nota * nota.peso)/100
            if tipo == 1:
                media = soma/quantidade
            else:
                media = soma
            if media >= 7:
                situacao = 'Aprovado'
            elif media >= 4:
                situacao = 'Final'
            else:
                situacao = 'Reprovado'
            s += f'{aluno.nome} -- Média: {media:.1f} -- {situacao}\n'
            print(f'{aluno.nome} -- Média: {media:.1f} -- {situacao}')
            deletaralunos(aluno.matricula)
        bd.deleteturma(turma)
        salvar = int(input('Deseja gerar arquivo .txt com o relatório dos alunos? 1 - Sim | 2 - Não'))
        if salvar == 1:
            arq = open("alunosfinal.txt", "w", encoding="utf-8")
            arq.write(s)
            arq.close()
    except:
        print('Erro ao tentar resgatar valores. Tente novamente mais tarde!')

def deletaralunos(matricula):
    try:
        bd.deletealuno(matricula)
    except:
        print('Erro ao tentar deletar aluno. Tente novamente mais tarde!')

def menu():
    while True:
        print('1 - Matricular Aluno')
        print('2 - Ver Alunos')
        print('3 - Criar Turma')
        print('4 - Adicionar/Deletar Notas')
        print('5 - Verificar Aprovados/Reprovados e Finalistas')
        print('0 - Sair')
        opcao = int(input())
        while 0 > opcao or opcao > 5:
            opcao = int(input())


        if opcao == 1:
            matricularaluno()
        elif opcao == 2:
            veralunos()
        elif opcao == 3:
            criarturma()
        elif opcao == 4:
            escolha = int(input('1- Adicionar notas\n2- Deletar notas\n'))
            adicionarnotas() if escolha == 1 else deletarnotas()
        elif opcao == 5:
            verturmas()
            turma = str(input('Código da turma: '))
            verificaralunos(turma)
        else:
            bd.desconecta()

menu()