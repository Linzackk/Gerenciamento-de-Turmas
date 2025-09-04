from funcoes import arquivos as arq
from funcoes import verificacao as ver
from funcoes import estrutura as est

class Professor:
    def __init__ (self, usuario, nome, idade, materia):
        self.usuario = usuario
        self.nome = nome
        self.idade = idade
        self.materia = materia
        