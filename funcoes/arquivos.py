# Funções para Lidar com arquivos no geral

import json
import funcoes.verificacao as ver

def importarArquivo():  
    with open(f"Alunos.json", "r") as arquivo:
        turma_salva = json.loads("\n".join(arquivo.readlines()))
    return turma_salva

def salvarArquivo(informacao):
    with open('Alunos.json',"w") as arquivo:
        json.dump(informacao, arquivo, indent=4)
        
def adicionarAluno(nomeCompleto="", idade=0, cargo=""):
    def criacaoUsuario(nomeCompleto, cargo):
        user = f"{nomeCompleto.split()[0]}{nomeCompleto.split()[-1]}{cargo[:2]}".lower()
        cont = 0
        userExist = ver.verificacaoUsuarioExiste(user)
        while userExist:
            cont += 1
            user = user = f"{nomeCompleto.split()[0]}{nomeCompleto.split()[-1]}{cont:02}{cargo[:2]}".lower()
            userExist = ver.verificacaoUsuarioExiste(user)
        return user.lower()
    nomeCompleto.capitalize()
    user = criacaoUsuario(nomeCompleto, cargo)
    return user, nomeCompleto, idade
