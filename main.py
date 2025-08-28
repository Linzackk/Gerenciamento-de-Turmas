# Controle de Turmas

# Criar Objeto Aluno, possui str Nome, int Idade, lista de float Notas.
# Criar Objeto Turma, possui str Nome, lista de objetos aluno.
# Metódos da Turma: Adicionar_aluno(aluno), media_turma(), aluno_maior_media()
import json

# Garante que a lista da Turma é sempre criada
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
   
# Importa a turma salva no arquivo
with open("Turma.json", "r") as arquivo:
     turma_salva = json.loads("\n".join(arquivo.readlines()))
    
print(f"Controle de Turmas")

# Informações Básicas do Aluno
nome = input("Nome do Aluno: ")
idade = int(input("Idade do Aluno: "))
usuario = nome.split()[0] + str(idade)

# Criando aluno
aluno = Aluno(nome, idade)

# Atribuindo notas do aluno
atribuicao = input("Deseja atribuir notas para o aluno? [s/n]").lower().strip()
if atribuicao == "s":
    print(f"Insira '-1' caso não queira atribuir uma nota.")
    bim1 = float(input("Nota para o Bimestre 1: "))
    bim2 = float(input("Nota para o Bimestre 2: "))
    
    # Verifica se a nota é válida (entre 0 e 10) e atribui ao aluno adicionado.
    if 0 <= bim2 and bim2 <= 10:
        aluno.atribuir_nota("bimestre1", bim1)
    if 0 <= bim2 and bim2 <= 10:
        aluno.atribuir_nota("bimestre2", bim2)
        
    print(f"Notas atualizadas com sucesso.")    
    
turma_salva[usuario] = aluno_para_dict(aluno)


# Salvar no Json
with open('Turma.json',"w") as arquivo:
    json.dump(turma_salva, arquivo, indent=4)
