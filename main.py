# Controle de Turmas

# TODO: Metódos da Turma: Adicionar_aluno(aluno), media_turma(), aluno_maior_media()
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
    alunos = arq.importarArquivo("Alunos")
    aluno = Aluno(user, alunos[user]["nome"], alunos[user]["idade"], alunos[user]["notas"])
    
    # Menu do Aluno
    # Loop para Manter no Menu
    escolha = -1
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
    
    # Menu do Professor
    escolha = -1
    while escolha != 0:
        escolha = professor.mostrarMenu()
        if escolha == 1:
            professor.atribuirNotas()
        elif escolha == 2:
            professor.atualizarInformacoes()
            arq.salvarArquivo(arq.salvarProfessor(professor, professores), "Professores")
        elif escolha == 3:
            professor.verInformacoes()
        
elif sigla == "ad":
    # Menu do Administrativo
    adms = arq.importarArquivo("Administrativo")
    adm = Adm(user, adms[user]["nome"], adms[user]["idade"])
    
print("Saindo")