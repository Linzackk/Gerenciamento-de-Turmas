from funcoes import arquivos as arq
from funcoes import verificacao as ver
from funcoes import estrutura as est
from classes.aluno import Aluno
from classes.professor import Professor

class Adm:
    def __init__ (self, usuario, nome, idade):
        self.usuario = usuario
        self.nome = nome
        self.idade = idade
        
    @est.separacao
    def mostrarMenu(self):
        opcoes = ["Adicionar Aluno", "Deletar Aluno", "Adicionar Professor", "Deletar Professor"]
        est.mostrarMenu(opcoes, "MENU DO PROFESSOR")
        escolha = ver.verificacaoEscolha(opcoes)
        return escolha
    
    @est.semiSeparacao
    def addAluno(self):
        @est.semiSeparacao
        def confirmacao():
            certeza = input("[S/N]\n").upper()
            return certeza
        
        correto = ""
        while correto != "S":
            nome = input("Nome completo: ").lower().title()
            idade = int(input("Idade: "))
            print('-' * 50)
            print(f"Informações inseridas: \nNome: {nome}\nIdade: {idade}")
            correto = confirmacao()
        
        alunos = arq.importarArquivo("Alunos")
        usuario = arq.adicionarUsuario(nome, "Aluno")
        aluno = Aluno(usuario, nome, idade)
        arq.salvarArquivo(arq.salvarAluno(aluno, alunos), "Alunos") 
        
    @est.semiSeparacao   
    def addProf(self):  
        @est.semiSeparacao
        def confirmacao():
            certeza = input("[S/N]\n").upper()
            return certeza
                  
        correto = ""
        while correto != "S":
            nome = input("Nome completo: ").lower().title()
            idade = int(input("Idade: "))
            materia = input("Materia de Ensino: ")
            print('-' * 50)
            print(f"Informações inseridas: \nNome: {nome}\nIdade: {idade}\nMatéria: {materia}")
            correto = confirmacao()
        
        profs = arq.importarArquivo("Professores")
        usuario = arq.adicionarUsuario(nome, "Professor") 
        professor = Professor(usuario, nome, idade, materia)
        arq.salvarArquivo(arq.salvarProfessor(professor, profs), "Professores")
    
    @est.semiSeparacao
    def deletarAluno(self):
        @est.semiSeparacao
        def confirmacao():
            certeza = input("Confirme o pedido de Remoção do Aluno [S/N]\n").upper()
            return certeza
        usuario = ''
        while not ver.verificacaoUsuarioExiste(usuario):
            usuario = input("Insira o Usuário do Aluno: ")
        alunos = arq.importarArquivo("Alunos")
        
        certeza = confirmacao()
        if certeza == "S":
            alunos.pop(usuario)
            print(f"Aluno deletado com sucesso.")
            arq.salvarArquivo(alunos,"Alunos")
        else:
            print(f"Aluno não foi deletado.")
        
    
    @est.semiSeparacao    
    def deletarProf(self):
        @est.semiSeparacao
        def confirmacao():
            certeza = input("Confirme o pedido de Remoção do Professor [S/N]\n").upper()
            return certeza
        
        
        usuario = ''
        while not ver.verificacaoUsuarioExiste(usuario):
            usuario = input("Insira o Usuário do Professor: ")
        professores = arq.importarArquivo("Professores")
        
        certeza = confirmacao()
        if certeza == "S":
            professores.pop(usuario)
            print(f"Professor deletado com sucesso.")
            arq.salvarArquivo(professores,"Professores")
        else:
            print(f"Professor não foi deletado.")
            