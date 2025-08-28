# Controle de Turmas

# Criar Objeto Aluno, possui str Nome, int Idade, lista de float Notas.
# Criar Objeto Turma, possui str Nome, lista de objetos aluno.
# Metódos da Turma: Adicionar_aluno(aluno), media_turma(), aluno_maior_media()
import json

try:
    a = open("Turma.json", "x")
except FileExistsError:
    a = open("Turma.json", "r")
finally:
    a.close()
    
class Aluno:
    def __init__ (self, nome, idade, notas = {"bimestre1": 0, "bimestre2": 0}):
        self.nome = nome
        self.idade = idade
        self.notas = notas
        
    def atribuir_nota(self, bimestre, nota):
        self.notas[bimestre] = nota
        
def aluno_para_dict(aluno):
   return {
        "nome" : aluno.nome,
        "idade": aluno.idade,
        "notas": aluno.notas
    }
    
# Criando aluno
print(f"Controle de Turmas")

nome = "Isaac"
idade = 20

aluno = Aluno(nome, idade)
aluno.atribuir_nota("bimestre1", 7.5)
aluno.atribuir_nota("bimestre2", 8)

dados_aluno = aluno_para_dict(aluno)

# Salvar no Json
with open('Turma.json',"a") as arquivo:
    json.dump(dados_aluno, arquivo, indent=4)
