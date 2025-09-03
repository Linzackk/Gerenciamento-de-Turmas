# Controle de Turmas

# Criar Objeto Aluno, possui str Nome, int Idade, lista de float Notas.
# Criar Objeto Turma, possui str Nome, lista de objetos aluno.
# Metódos da Turma: Adicionar_aluno(aluno), media_turma(), aluno_maior_media()
import json

import funcoes.arquivos as arq
import funcoes.verificacao as ver
import funcoes.estrutura as est

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

est.titulo("Controle de Turmas")

while True:
    usuario = est.respostas("Insira o Usuário para Login").lower()
    if ver.verificacaoUsuarioExiste(usuario):
        break
print("Logado com Sucesso")
print("IGNORAR O RESTO A PARTIR DAQUI POIS ESTÁ EM MANUTENÇÃO")

# Importa a turma salva no arquivo
turma_salva = arq.importarArquivo()

# Carrega aluno logado
#aluno = Aluno(usuario, turma_salva[usuario]["nome"], turma_salva[usuario]["idade"], turma_salva[usuario]["notas"])
    
opcoes = ["Adicionar Aluno: ", "Verificar Aluno", "Atualizar Aluno", "Deletar Aluno"]
escolha = ver.verificacaoEscolha(opcoes)

    