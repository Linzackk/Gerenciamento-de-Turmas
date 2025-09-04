# Funções para verificação de dados
from . import arquivos as arq
from . import estrutura as est

@est.semiSeparacao
def verificacaoEscolha(opcoes):
    # Verifica se a Escolha esta dentro do range das opções
    limite = [0, (len(opcoes) -1)]
    escolha = -999
    
    # Mantém no loop até estar dentro do range
    while limite[0] > escolha and escolha < limite[1]:
        escolha = int(input("Insira sua escolha: "))
    return escolha

def verificacaoUsuarioExiste(usuario):
    # Verifica se o Usuário Existe
    nomeArquivo = {
        "al": "Alunos",
        "pr": "Professores",
        "ad": "Administrativo"
    }
    # As ultimas 2 letras representam a Função no sistema
    # Caso não exista, o usuário é inválido.
    
    # Tenta pegar a sigla
    try:
        sigla = nomeArquivo[usuario[-2:]]
    except KeyError:
        # Não existe o Usuário
        return False
    
    else:
        # Importa o arquivo que o usuário está presente (Alunos, Professores ou Administrativo)
        dicionario = arq.importarArquivo(sigla)
        
        # Verifica se ele existe dentro do arquivo
        if usuario not in dicionario:
            # O Usuário existe
            return False
        
        else:
            # O Usuário não existe
            return True
 