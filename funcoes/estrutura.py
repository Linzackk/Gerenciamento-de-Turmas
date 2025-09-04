from . import verificacao as ver
from . import arquivos as arq

def separacao(func):
    def wrapper(*args, **kwargs):
        print("-" * 50)
        resultado = func(*args, **kwargs)
        print("-" * 50)
        return resultado
    return wrapper

def semiSeparacao(func):
    def wrapper(*args, **kwargs):
        print("-" * 50)
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper
    
@separacao
def titulo(texto=""):
    print(texto.center(50))

@semiSeparacao 
def respostas(texto=""):
    print(texto)
    r = input()
    return r

@separacao
def mostrarMenu(opcoes, mensagem):
    print(f"{mensagem}".center(50))
    opcoes.insert(0, "Sair")
    for c, i in enumerate(opcoes):
        print(f"[ {c} ] - {i}")
    
    