from funcoes import arquivos as arq
from funcoes import verificacao as ver
from funcoes import estrutura as est

class Aluno:
    def __init__ (self, usuario, nome, idade, notas = {"semestre1": 0.0, "semestre2": 0.0}):
        self.usuario = usuario
        self.nome = nome
        self.idade = idade
        self.notas = notas
    
    @est.semiSeparacao  
    def ver_informacoes(self):
        # Mostra o Nome e a Idade do Aluno
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
     
    @est.semiSeparacao  
    def atualizarInformacoes(self):
        # Troca as Informações do Aluno
        def trocar_nome(novoNome):
            # Troca de Nome
            self.nome = novoNome
    
        def trocar_idade(novaIdade):
            # Troca de Idade
            self.idade = novaIdade
        
        # Mostra as opções e os numeros correspondentes
        opcoes = ["Alterar Nome", "Alterar Idade"]
        est.mostrarMenu(opcoes, "DADOS ALTERÁVEIS")
        escolha = ver.verificacaoEscolha(opcoes)
        
        # Pega o Novo nome e Atualiza com o método trocar_nome
        if escolha == 1:
            novoNome = input("Insira seu Novo Nome: ")
            trocar_nome(novoNome)
        
        # Pega a Nova idade e Atualiza com o método trocar_idade    
        elif escolha == 2:
            novaIdade = int(input("Insira sua Nova idade: "))
            trocar_idade(novaIdade)
        
    @est.separacao  
    def mostrarMenu(self):
        # Mostra o Menu principal do Aluno
        opcoes = ["Ver Notas", "Atualizar Dados", "Verificar Informações"]
        est.mostrarMenu(opcoes, "MENU DO ALUNO")
        escolha = ver.verificacaoEscolha(opcoes)
        return escolha
    
    @est.semiSeparacao    
        # Mostra as Notas do Aluno   
    def verNotas(self):
        notas = ["Semestre 1", "Semestre 2"]
        est.mostrarMenu(notas, "NOTAS DISPONÍVEIS")
        escolha = ver.verificacaoEscolha(notas)
        if escolha != 0:
            print(f"Nota do {escolha}° Semestre: {self.notas[f"semestre{escolha}"]}")