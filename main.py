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

# Tela de Login
while True:
    user = est.respostas("Insira o Usuário para Login").lower()
    if ver.verificacaoUsuarioExiste(user):
        # Laço é quebrado após verificar existência do Usuário
        break
print("Logado com Sucesso")

# Define a sigla a partir dos dois ultimos caracteres.
sigla = user[-2:]

# Caso da sigla para Aluno
if sigla == "al":
    
    # Importa o Arquivo de Alunos
    alunos = arq.importarArquivo("Alunos")
    
    # Cria o Objeto do Aluno que esta utilizando o sistema
    aluno = Aluno(user, alunos[user]["nome"], alunos[user]["idade"], alunos[user]["notas"])
    
    # Mostra o Menu do Aluno em loop até a opção ser "0"
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

# Caso da sigla para Professor 
elif sigla == "pr":
    
    # Importa o Arquivo de Professores
    professores = arq.importarArquivo("Professores")
    
    # Cria o Objeto do Professor que esta utilizando o sistema
    professor = Professor(user, professores[user]["nome"], professores[user]["idade"], professores[user]["materia"])
    
    # Mostra o Menu do Professor em loop até a opção ser "0"
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

# Caso da sigla para Administrativo        
elif sigla == "ad":
    
    # Importa o Arquivo de Administrativos
    adms = arq.importarArquivo("Administrativo")
    
    # Cria o Objeto do Adm que esta utilizando o sistema
    adm = Adm(user, adms[user]["nome"], adms[user]["idade"])
    
    # Mostra o Menu do Administrativo em loop até a opção ser "0"
    escolha = -1
    while escolha != 0:
        escolha = adm.mostrarMenu()
        if escolha == 1:
            adm.addAluno()
        elif escolha == 2:
            adm.deletarAluno()
        elif escolha == 3:
            adm.addProf()
        elif escolha == 4:
            adm.deletarProf()
              
print("Saindo")