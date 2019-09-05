#Arthur Stevam 
#Sexta - Feira, 30 de Agosto de 2019
#Classe Principal

from bd.acesso_bd import banco_de_dados
import Classes.Controller as Controller
from Classes.turma import Turma

bd = banco_de_dados()

def menu():
    while True:
        print('1 - Matricular Aluno')
        print('2 - Ver Alunos')
        print('3 - Criar Turma')
        print('4 - Adicionar Notas')
        print('5 - Verificar Aprovados/Reprovados e Finalistas')
        print('0 - Sair')
        opcao = int(input())
        while 0 > opcao or opcao > 5:
            opcao = int(input())
        if opcao == 1:
            Controller.criaraluno()
        elif opcao == 2:
            Controller.veralunos()
        elif opcao == 3:
            Controller.criarturma()
        elif opcao == 4:
            Controller.verturmas()
            codigo = (input('Código da turma que deseja adicionar notas: '))
            turma = Turma(0)
            turma.recebeentidade(bd.getturma(codigo))
            turma.adicionarnotas()
        elif opcao == 5:
            Controller.verturmas()
            codigo = str(input('Código da turma: '))
            turma = Turma(0)
            turma.recebeentidade(bd.getturma(codigo))
            turma.encerrarturma()
        else:
            bd.desconecta()
            break

menu()