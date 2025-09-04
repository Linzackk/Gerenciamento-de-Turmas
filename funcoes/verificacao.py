# Funções para verificação de dados
from . import arquivos as arq
from . import estrutura as est

@est.semiSeparacao
def verificacaoEscolha(opcoes):
    limite = [0, (len(opcoes) -1)]
    escolha = -999
    # Limite [0,3]
    while limite[0] > escolha and escolha < limite[1]:
        escolha = int(input("Insira sua escolha: "))
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
 