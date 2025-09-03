def separacao(func):
    def wrapper(*args, **kwargs):
        print("-" * 50)
        resultado = func(*args, **kwargs)
        print("-" * 50)
        return resultado
    return wrapper

def semiSeparacao(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print("-" * 50)
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
    