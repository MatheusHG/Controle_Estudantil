#Arthur Stevam
#Sábado, 31 de Agosto de 2019
#Classe Turma
from Classes.nota import Nota


class Turma():

    def __init__(self, lista_alunos, faltas):
        self.alunos = lista_alunos
        self.limiteFaltas = faltas
        self.estado = True
        self.codigo_turma = f'2019008{len(self.alunos)}{faltas}'
        self.final = []

    def getAlunos(self):
        s = ""
        for a in self.alunos:
            s += f'\n{a}\n'
            s += ('-'*10)
        return s

    def verificaFinal(self, quantidade_notas):
        for a in self.alunos:
            if a.notas[0].peso is not False:
                tipo_media = 1
        s = ''
        situacao = ''
        for a in self.alunos:
            media = a.getMedia(quantidade_notas, tipo_media)
            if media is False:
                self.notaAluno(a.matricula)
            elif media >= 7:
                situacao = 'Aprovado'
            elif media >= 4:
                situacao = 'Final'
                self.final.append(a)
            else:
                situacao = 'Reprovado'
            a.setmedia(media)
            s += f'{a.nome} -- {situacao} -- Média: {media:.1f}\n'
        print(s)

    def getsituacaoaluno(self, matricula_aluno):
        if matricula_aluno in self.alunos:
            for a in self.alunos:
                if a.matricula == matricula_aluno:
                    if a.aprovado is True:
                        return 'Aprovado'
                    else:
                        return 'Reprovado'
                else:
                    return 'Aluno não está na turma.'

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
            if a.aprovado is False:
                l.append(a)
        return l

    def getAprovados(self):
        l = []
        for a in self.alunos:
            if a.aprovado is True:
                l.append(a)
        return l

    def adicionarNotas(self):
            for a in self.alunos:
                n = float(input(f'{a.nome}\nNota: '))
                peso = int(input('Peso da Nota\n(Se não houver peso digite 0): '))
                if peso == 0:
                    peso = False
                a.adicionarNota(n, peso)
                print('Nota Adicionada!')

    def adicionarnotasfinal(self):
        opcao = 1
        while opcao != 0:
            for a in self.final:
                n = float(input(f'{a.nome}\nNota Final: '))
                a.notafinal(n)
                print('Nota Adicionada!')

    def notaAluno(self, matricula_aluno):
        if matricula_aluno in self.alunos:
            for a in self.alunos:
                if a.matricula == matricula_aluno:
                    n = float(input(f'{a.nome}\nNota: '))
                    peso = int(input('Peso da Nota\n(Se não houver peso digite 0): '))
                    if peso == 0:
                        peso = False
                    a.adicionarNota(n, peso)
                    print('Nota Adicionada!')
        else:
            print('Aluno não está na turma.')

    def encerrarturma(self):
        for a in self.final:
            media_atual = a.media * 0.6 + a.final * 0.4
            if media_atual >= 5.0:
                a.aprovado == True
            else:
                a.aprovado == False
            a.media = media_atual
            self.getsituacaoaluno(a)



    
