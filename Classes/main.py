#Arthur Stevam 
#Sexta - Feira, 30 de Agosto de 2019
#Classe Principal

from aluno import Aluno
from turma import Turma

data_nascimento = input()
numero_cpf = input()
numero_rg = input()
aluno_um = Aluno('Cleber', data_nascimento, numero_cpf, numero_rg)
aluno_dois = Aluno('Claudia', data_nascimento, numero_cpf, numero_rg)
aluno_tres = Aluno('Fernandis', data_nascimento, numero_cpf, numero_rg)
aluno_quatro = Aluno('Marieles', data_nascimento, numero_cpf, numero_rg)
aluno_cinco = Aluno('Lucio', data_nascimento, numero_cpf, numero_rg)

turma = Turma([aluno_um, aluno_dois,aluno_tres,aluno_quatro,aluno_cinco], 10)
print(turma.getAlunos())
