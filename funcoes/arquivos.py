# Funções para Lidar com arquivos no geral

import json
import os
from . import verificacao as ver

def garantirExistenciaArquivo(nomeArquivo):
    # Redireciona o Caminho para a Pasta "arquivosJson" para ficar organizado
    caminho_base = os.path.join(os.path.dirname(__file__), "..", "arquivosJson")
    
    # Garante que o parametro vai ter um .json ao final
    if not nomeArquivo.endswith(".json"):
        nomeArquivo += ".json"
        
    # Direciona o caminho
    caminhoArquivo = os.path.join(caminho_base, nomeArquivo)
    
    # Garante que há um texto sempre no arquivo
    try: 
        with open(caminhoArquivo, "r") as arquivo:
            teste = json.loads("\n".join(arquivo.readlines()))
    except json.decoder.JSONDecodeError:
        with open(caminhoArquivo, "w") as arquivo:
            dictVazio = {}
            json.dump(dictVazio, arquivo, indent=4)


def importarArquivo(nomeArquivo):
    # Redireciona o Caminho para a Pasta "arquivosJson"
    caminho_base = os.path.join(os.path.dirname(__file__), "..", "arquivosJson")
    
    # Garante que o parametro vai ter um .json ao final
    if not nomeArquivo.endswith(".json"):
        nomeArquivo += ".json"
        
    # Direciona o caminho
    caminhoArquivo = os.path.join(caminho_base, nomeArquivo)
    
    with open(caminhoArquivo, "r") as arquivo:
        dicionarioBanco = json.loads("\n".join(arquivo.readlines()))
    return dicionarioBanco

def salvarArquivo(informacao, nomeArquivo):
    # Redireciona o Caminho para a Pasta "arquivosJson"
    caminho_base = os.path.join(os.path.dirname(__file__), "..", "arquivosJson")
    
    # Garante que o parametro vai ter um .json ao final
    if not nomeArquivo.endswith(".json"):
        nomeArquivo += ".json"
        
    # Direciona o caminho
    caminhoArquivo = os.path.join(caminho_base, nomeArquivo)
    
    with open(caminhoArquivo,"w") as arquivo:
        json.dump(informacao, arquivo, indent=4)
        
def salvarAluno(aluno, arquivo):
    def aluno_para_dict(aluno):
        return{
            "nome" : aluno.nome,
            "idade": aluno.idade,
            "notas": aluno.notas
            }
    
    arquivo[aluno.usuario] = aluno_para_dict(aluno)
    return arquivo

def salvarProfessor(prof, arquivo):
    def prof_para_dict(prof):
        return {
            "nome" : prof.nome,
            "idade": prof.idade,
            "materia": prof.materia
        }
        
    arquivo[prof.usuario] = prof_para_dict(prof)
    return arquivo
        
def adicionarUsuario(nomeCompleto="", cargo=""):
    def criacaoUsuario(nomeCompleto, cargo):
        user = f"{nomeCompleto.split()[0]}{nomeCompleto.split()[-1]}{cargo[:2]}".lower()
        cont = 0
        userExist = ver.verificacaoUsuarioExiste(user)
        while userExist:
            cont += 1
            user = user = f"{nomeCompleto.split()[0]}{nomeCompleto.split()[-1]}{cont:02}{cargo[:2]}".lower()
            userExist = ver.verificacaoUsuarioExiste(user)
        return user.lower()
    user = criacaoUsuario(nomeCompleto, cargo)
    return user