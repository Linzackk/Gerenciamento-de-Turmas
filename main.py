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

# Apresentação
est.titulo("Controle de Turmas")

while True:
    user = est.respostas("Insira o Usuário para Login").lower()
    if ver.verificacaoUsuarioExiste(user):
        break
print("Logado com Sucesso")

sigla = user[-2:]
if sigla == "al":
    # Menu do Aluno
    alunos = arq.importarArquivo("Alunos")
    aluno = Aluno(user, alunos[user]["nome"], alunos[user]["idade"], alunos[user]["notas"])
    escolha = -1
    
    # Loop para Manter no Menu
    while escolha != 0:
        escolha = aluno.mostrarMenu()
        if escolha == 1:
            aluno.verNotas()
        elif escolha == 2:
            aluno.atualizarInformacoes()
            arq.salvarArquivo(arq.salvarAluno(aluno, alunos), "Alunos")
        elif escolha == 3:
            aluno.ver_informacoes()
            
elif sigla == "pr":
    professores = arq.importarArquivo("Professores")
    professor = Professor(user, professores[user]["nome"], professores[user]["idade"], professores[user]["materia"])
    
elif sigla == "ad":
    # Menu do Administrativo
    adms = arq.importarArquivo("Administrativo")
    adm = Adm(user, adms[user]["nome"], adms[user]["idade"])
    
print("Saindo")