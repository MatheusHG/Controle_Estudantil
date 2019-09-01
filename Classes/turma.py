#Arthur Stevam
#Sábado, 31 de Agosto de 2019
#Classe Turma

class Turma():

    def __init__(self, lista_alunos, faltas):
        self.alunos = lista_alunos
        self.limiteFaltas = faltas
        self.estado = True
        self.codigo_turma = f'2019008{len(self.alunos)}{faltas}'

    def getAlunos(self):
        s = ""
        for a in self.alunos:
            s += f'\n{a}\n'
            s += ('-'*10)
        return s

    def encerrarPeriodo(self):
        self.estado = False

    def getSituacaoAlunos(self):
        for a in self.alunos:
            notas = ''
            for n in a.getNotas():
                notas += f'{n:.1f}| '
            print('-'*10)
            print(f'{a.nome}\nNotas: {notas}\nFaltas: {a.faltas}')
