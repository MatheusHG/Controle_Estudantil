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

    def verificaFinal(self, quantidade_notas):
        for a in self.alunos:
            if a.notas[0].peso != False:
                tipo_media = 1
        s = ''
        situacao = ''
        for a in self.alunos:
            media = a.getMedia(quantidade_notas, tipo_media)
            if media == False:
                return False
            elif media >= 7:
                situacao = 'Aprovado'
            elif media >= 4:
                situacao = 'Final'
            else:
                situacao = 'Reprovado'
            s += f'{a.nome} -- {situacao} -- Média: {media:.1f}\n'
        print(s)

    def getSituacaoAlunos(self):
        for a in self.alunos:
            notas = ''
            for n in a.getNotas():
                notas += f'{n:.1f}| '
            print('-'*10)
            print(f'{a.nome}\nNotas: {notas}\nFaltas: {a.faltas}')

    def getReprovados(self):
        l = []
        for a in self.alunos:
            if a.aprovado == False:
                l.append(a)
        return l

    def getAprovados(self):
        l = []
        for a in self.alunos:
            if a.aprovado == True:
                l.append(a)
        return l
    
