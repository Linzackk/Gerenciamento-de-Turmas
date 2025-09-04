from funcoes import arquivos as arq
from funcoes import verificacao as ver
from funcoes import estrutura as est

class Aluno:
    def __init__ (self, usuario, nome, idade, notas = {"semestre1": 0, "semestre2": 0}):
        self.usuario = usuario
        self.nome = nome
        self.idade = idade
        self.notas = notas
    
    @est.semiSeparacao  
    def ver_informacoes(self):
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
     
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
        
    @est.separacao  
    def mostrarMenu(self):
        opcoes = ["Ver Notas", "Atualizar Dados", "Verificar Informações"]
        est.mostrarMenu(opcoes, "MENU DO ALUNO")
        escolha = ver.verificacaoEscolha(opcoes)
        return escolha
    
    @est.semiSeparacao       
    def verNotas(self):
        notas = ["Semestre 1", "Semestre 2"]
        est.mostrarMenu(notas, "NOTAS DISPONÍVEIS")
        escolha = ver.verificacaoEscolha(notas)
        if escolha != 0:
            print(f"Nota do {escolha}° Semestre: {self.notas[f"Semestre{escolha}"]}")