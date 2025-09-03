# Controle de Turmas

# Criar Objeto Aluno, possui str Nome, int Idade, lista de float Notas.
# Criar Objeto Turma, possui str Nome, lista de objetos aluno.
# Metódos da Turma: Adicionar_aluno(aluno), media_turma(), aluno_maior_media()
import json
import funcoes.arquivos as arq
import funcoes.verificacao as ver
from classes.aluno import Aluno
from classes.professor import Professor 
from classes.adm import Adm

# Garante que os Arquivos estejam com alguma informação para ser lida
bancoDados = ["Alunos", "Professores", "Administrativo"]
for i in bancoDados:
    arq.garantirExistenciaArquivo(i)

# Refatorar para outro arquivo
def aluno_para_dict(aluno):
   return{
            "nome" : aluno.nome,
            "idade": aluno.idade,
            "notas": aluno.notas
            }

# Apresentação
# Fazer apresentável
print(f"Controle de Turmas")

while True:
    usuario = input("Insira o Usuario do Aluno: ")
    if ver.verificacaoUsuarioExiste(usuario):
        break
print("Logado com Sucesos")
print("IGNORAR O RESTO A PARTIR DAQUI POIS ESTÁ EM MANUTENÇÃO")

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
    