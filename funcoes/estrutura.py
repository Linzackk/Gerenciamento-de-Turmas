from . import verificacao as ver
from . import arquivos as arq

def separacao(func):
    # Função para deixar mais bonito usando Wrapper antes e depois da função
    def wrapper(*args, **kwargs):
        print("-" * 50)
        resultado = func(*args, **kwargs)
        print("-" * 50)
        return resultado
    return wrapper

def semiSeparacao(func):
    # Outro wrapper mas apenas para antes da função
    def wrapper(*args, **kwargs):
        print("-" * 50)
        resultado = func(*args, **kwargs)
        return resultado
    return wrapper
    
@separacao
def titulo(texto=""):
    # Mostra uma Mensagem centralizada junto com os wrappers separadores
    print(texto.center(50))

@semiSeparacao 
def respostas(texto=""):
    # Pega as respostas dos menus
    print(texto)
    r = input()
    return r

@separacao
def mostrarMenu(opcoes, mensagem):
    # Mostra o menu com as opções, insere a opção "Sair"
    # Vincula um numero a cada uma delas
    print(f"{mensagem}".center(50))
    opcoes.insert(0, "Sair")
    for c, i in enumerate(opcoes):
        print(f"[ {c} ] - {i}")
    
    