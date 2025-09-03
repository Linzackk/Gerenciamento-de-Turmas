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
        