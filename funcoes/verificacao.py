# Funções para verificação de dados
from . import arquivos as arq

def verificacaoEscolha(opcoes):
    limite = [0, (len(opcoes) -1)]
    opcoes.insert(0, "Sair")
    print()
    for c, i in enumerate(opcoes):
        print(f"[ {c} ] - {i}")
    escolha = -1
    print()
    while escolha < limite[0] or escolha > limite[1] :
        escolha = int(input("Insira sua escolha: "))
        continue
    return escolha

def verificacaoUsuarioExiste(usuario):
    nomeArquivo = {
        "al": "Alunos",
        "pr": "Professores",
        "ad": "Administrativo"
    }
    try:
        sigla = nomeArquivo[usuario[-2:]]
    except KeyError:
        return False
    else:
        dicionario = arq.importarArquivo(sigla)
        if usuario not in dicionario:
            return False
        else:
            return True
 