# Controle de Turmas

# Criar Objeto Aluno, possui str Nome, int Idade, lista de float Notas.
# Criar Objeto Turma, possui str Nome, lista de objetos aluno.
# Metódos da Turma: Adicionar_aluno(aluno), media_turma(), aluno_maior_media()
import json
import funcoes.arquivos as arq
import funcoes.verificacao as ver

# Garante que o Arquivo "Alunos" sempre existirá com informação.
try: 
    with open(f"Alunos.json", "r") as arquivo:
        teste = json.loads("\n".join(arquivo.readlines()))
except json.decoder.JSONDecodeError:
    with open(f"Alunos.json", "w") as arquivo:
        dictVazio = {}
        json.dump(dictVazio, arquivo, indent=4)

class Aluno:
    def __init__ (self, usuario, nome, idade, notas = {"bimestre1": 0, "bimestre2": 0}):
        self.usuario = usuario
        self.nome = nome
        self.idade = idade
        self.notas = notas
        
    def atribuir_nota(self, bimestre, nota):
        self.notas[bimestre] = nota
        
    def ver_informacoes(self):
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Notas: \nBimestre 1: {self.notas["bimestre1"]}\nBimestre 2: {self.notas["bimestre2"]}")
        
    def trocar_nome(self, novoNome):
        self.nome = novoNome
    
    def trocar_idade(self, novaIdade):
        self.idade = novaIdade
        
def aluno_para_dict(aluno):
   return{
            "nome" : aluno.nome,
            "idade": aluno.idade,
            "notas": aluno.notas
            }


# Variavel para habilitar o salvamento no arquivo 
alteracaoUsuarioExistente = False
alteracaoNovoUsuario = False

print(f"Controle de Turmas")

# CRUD do aluno
while True:
    usuario = input("Insira o Usuario do Aluno: ")
    if ver.verificacaoUsuarioExiste(usuario):
        break
print("Usuário Existente.")

# Importa a turma salva no arquivo
turma_salva = arq.importarArquivo()

# Carrega aluno logado
#aluno = Aluno(usuario, turma_salva[usuario]["nome"], turma_salva[usuario]["idade"], turma_salva[usuario]["notas"])
    
opcoes = ["Adicionar Aluno: ", "Verificar Aluno", "Atualizar Aluno", "Deletar Aluno"]
escolha = ver.verificacaoEscolha(opcoes)
# If para cada escolha

# Fazer só possível caso seja Administrador a conta
if escolha == 0:
    print("Nenhuma opção foi escolhida.")
    
if escolha == 1:
    # Função da Classe Administrador. Continua aqui temporariamente
    nome = input("Nome Completo do Aluno: ")
    idade = input("Idade do Aluno: ")
    infos = arq.adicionarAluno(nome, idade, "aluno")
    novoAluno = Aluno(infos[0],infos[1],infos[2])
    novoUsuario = novoAluno.usuario
    alteracaoNovoUsuario = True
    
    # Adicionar mais informações, sexo, data de nascimento, etc etc.
    
    
if escolha == 2:
    aluno.ver_informacoes()
    
if escolha == 3:
    opcoesAlteracao = ["Nome", "Idade"]
    escolhaAlteracao = ver.verificacaoEscolha(opcoesAlteracao)
    
    if escolhaAlteracao == 0:
        print("Nenhuma opção foi escolhida;")
    if escolhaAlteracao == 1:
        # Atualiza o Nome
        aluno.trocar_nome(input("Insira o novo nome do Aluno: "))
        alteracaoUsuarioExistente = True
    if escolhaAlteracao == 2:
        # Atualiza a Idade
        aluno.trocar_idade(input("Insira a nova idade do Aluno: "))
        alteracaoUsuarioExistente = True

# Apenas o Administrador.
if escolha == 4:
    print("Deletar aluno: ") # Place Holder
    
if alteracaoUsuarioExistente:
    turma_salva[usuario] = aluno_para_dict(aluno)
    arq.salvarArquivo(turma_salva)
    
if alteracaoNovoUsuario:
    turma_salva[novoUsuario] = aluno_para_dict(novoAluno)
    arq.salvarArquivo(turma_salva)
    