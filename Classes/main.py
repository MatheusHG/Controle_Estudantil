#Arthur Stevam 
#Sexta - Feira, 30 de Agosto de 2019
#Classe Principal

from Classes.aluno import Aluno
from Classes.turma import Turma
from Classes.nota import Nota
from bd.acesso_bd import banco_de_dados

bd = banco_de_dados()
matricular = []

def matricularaluno():
    print('-' * 50)
    print('Matricular ALuno')
    nome = str(input('Nome: '))
    cpf = str(input('CPF: '))
    aluno = Aluno(nome, cpf)
    aprovado = 1 if aluno.aprovado is True else 0
    bd.insertaluno(aluno.matricula, aluno.nome, aluno.cpf, aprovado)
    print('ALuno matriculado com sucesso!')
    matricular.append(aluno)

def veralunos():
    lista_alunos = bd.gettodosalunos()
    aluno = Aluno("", "")
    for a in lista_alunos:
        print('-'*50)
        aluno.recebeentidade(a)
        print(f'{aluno.matricula} - {aluno.nome}')
    print('-'*50)

def verturmas():
    lista_turmas = bd.getturmas()
    turma = Turma(True)
    for t in lista_turmas:
        turma.turmaidentidade(t)
        print(turma.codigo_turma)

def criarturma():
    faltas = int(input('Qual será o limite de faltas da turma? '))
    turma = Turma(faltas)
    bd.insertturma(turma.codigo_turma, turma.limiteFaltas, turma.estado, turma.notas)
    quantidade_alunos = 0
    for a in matricular:
        bd.insertmatricula(a.matricula, turma.codigo_turma)
        quantidade_alunos += 1
    bd.conn.commit()
    matricular.clear()
    print(f'Turma criada com sucesso!\n{quantidade_alunos} matriculados na turma')

def infoturma():
    codigo = str(input('Informe o código da turma: '))
    lista_alunos = bd.getalunos(codigo)
    aluno = Aluno("", "")
    for a in lista_alunos:
        matricula = a[0]
        aluno.recebeentidade(bd.getaluno(matricula))
        print(aluno.nome)

def adicionarnotas():
    verturmas()
    codigo = str(input('Informe o código da turma: '))
    lista_aluno = bd.getalunos(codigo)
    aluno = Aluno("", "")
    turma = Turma(True)
    turma.turmaidentidade(bd.getturma(codigo))
    id = turma.notas
    for a in lista_aluno:
        aluno.recebeentidade(bd.getaluno(a[0]))
        nota = float(input(f'Nota de {aluno.nome}: ')) ## a[0] pega a matrícula do aluno
        peso = float(input(f'Peso da nota (0 para média aritmética): '))
        bd.isertnota(id, aluno.matricula, turma.codigo_turma, nota, peso)
        print('-'*50)
    id += 1
    bd.updatequantidadenotas(turma.codigo_turma, id)


def deletarnotas():
    verturmas()
    codigo = str(input('Informe o código da turma: '))
    id = int(input('Informe o numero da avaliação a ser excluída: '))
    bd.deletenota(id, codigo)
    turma = Turma(True)
    turma.turmaidentidade(bd.getturma(codigo))
    id = turma.notas
    id -= 1
    bd.updatequantidadenotas(codigo, id)

def verificaralunos(turma):
    arq = open("alunosfinal.txt", "w", encoding="utf-8")
    s = ""
    alunos_deletar = []
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
    arq.write(s)
    arq.close()

def deletaralunos(matricula):
    bd.deletealuno(matricula)

def menu():
    while True:
        print('1 - Matricular Aluno')
        print('2 - Ver Alunos')
        print('3 - Criar Turma')
        print('4 - Adicionar/Deletar Notas')
        print('5 - Verificar Aprovados/Reprovados e Finalistas')
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


menu()