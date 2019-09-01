#Arthur Stevam 
#Sexta - Feira, 30 de Agosto de 2019
#Classe Principal

from aluno import Aluno
from turma import Turma

data_nascimento = '01/08/2019'
numero_cpf = '321001990-05'
numero_rg = '543213'
aluno_um = Aluno('Cleber', data_nascimento, numero_cpf, numero_rg)
aluno_dois = Aluno('Claudia', data_nascimento, numero_cpf, numero_rg)
aluno_tres = Aluno('Fernandis', data_nascimento, numero_cpf, numero_rg)
aluno_quatro = Aluno('Marieles', data_nascimento, numero_cpf, numero_rg)
aluno_cinco = Aluno('Lucio', data_nascimento, numero_cpf, numero_rg)
aluno_um.adicionarNota(10, False)
aluno_um.adicionarNota(10, False)
aluno_dois.adicionarNota(9, False)
aluno_dois.adicionarNota(7, 30)
aluno_tres.adicionarNota(7, 20)
aluno_tres.adicionarNota(7, False)
aluno_quatro.adicionarNota(4, False)
aluno_quatro.adicionarNota(4, False)
aluno_cinco.adicionarNota(1, 50)
aluno_cinco.adicionarNota(1, 50)
turma = Turma([aluno_um, aluno_dois,aluno_tres,aluno_quatro,aluno_cinco], 10)

print(turma.estado)
turma.verificaFinal(2)
print(turma.estado)
