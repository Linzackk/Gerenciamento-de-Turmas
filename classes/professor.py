from funcoes import arquivos as arq
from funcoes import verificacao as ver
from funcoes import estrutura as est

class Professor:
    def __init__ (self, usuario, nome, idade, materia):
        self.usuario = usuario
        self.nome = nome
        self.idade = idade
        self.materia = materia
    
    @est.separacao
    def mostrarMenu(self):
        opcoes = ["Atribuir Notas", "Atualizar Dados", "Verificar Informações"]
        est.mostrarMenu(opcoes, "MENU DO PROFESSOR")
        escolha = ver.verificacaoEscolha(opcoes)
        return escolha
    
    @est.semiSeparacao 
    def verInformacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Materia: {self.materia}")
     
    @est.semiSeparacao    
    def atualizarInformacoes(self):
        def trocar_nome(novoNome):
            self.nome = novoNome
    
        def trocar_idade(novaIdade):
            self.idade = novaIdade
            
        opcoes = ["Alterar Nome", "Alterar Idade"]
        est.mostrarMenu(opcoes, "DADOS ALTERÁVEIS")
        escolha = ver.verificacaoEscolha(opcoes)
        
        if escolha == 1:
            novoNome = input("Insira seu Novo Nome: ")
            trocar_nome(novoNome)
            
        elif escolha == 2:
            novaIdade = int(input("Insira sua Nova idade: "))
            trocar_idade(novaIdade)
            
    @est.semiSeparacao         
    def atribuirNotas(self):
        usuario = ''
        while not ver.verificacaoUsuarioExiste(usuario):
            usuario = input("Insira o Usuário do Aluno: ")
        alunos = arq.importarArquivo("Alunos")
        
        opcoes = ["Bimestre 1", "Bimestre 2"]
        est.mostrarMenu(opcoes, "NOTAS ALTERÁVEIS")
        escolha = ver.verificacaoEscolha(opcoes)
        
        if escolha == 1:
            bimestre = "bimestre1"
        elif escolha == 2:
            bimestre = "bimestre2"
            
        if escolha != 0:    
            nota = -1
            while nota < 0 or nota > 10:
                nota = float(input("Insira a Nota: "))
            alunos[usuario]["notas"][bimestre] = nota
            arq.salvarArquivo(alunos, "Alunos")
        
        