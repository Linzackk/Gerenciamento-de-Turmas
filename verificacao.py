# Funções para verificação de dados

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

def verificacaoUsuario(usuario, dicionario):
    if usuario not in dicionario:
        return False
    else:
        return True
    