# Funções para verificação de dados
import funcoes.arquivos as arq

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
    
    dicionario = arq.importarArquivo()
    if usuario not in dicionario:
        print(f"O USUARIO NAO TA NO DICIONARIO")
        return False
    else:
        print(f"O USUARIO TA NO DICIONARIO")
        return True
 