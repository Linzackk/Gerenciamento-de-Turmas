# Funções para Lidar com arquivos no geral

import json
import os
from . import verificacao as ver

def adicionarExtensaoJson(nomeArquivo):
    # Garante que o parametro vai ter um .json ao final
    if not nomeArquivo.endswith(".json"):
        nomeArquivo += ".json"
    return nomeArquivo
      

def redirecionarCaminho(arquivo):
    caminho_base = os.path.join(os.path.dirname(__file__), "..", "arquivosJson")
      
    # Direciona o caminho
    caminhoArquivo = os.path.join(caminho_base, arquivo)
    return caminhoArquivo

def garantirExistenciaArquivo(nomeArquivo):
    # Garante que os Arquivos JSON (Alunos, Professores e Administrativo) tenham conteúdo e possam ser lidos
    arquivo = redirecionarCaminho(adicionarExtensaoJson(nomeArquivo))
    
    # Garante que há um texto sempre no arquivo
    try: 
        # Tenta ler o arquivo
        with open(arquivo, "r") as arquivo:
            teste = json.loads("\n".join(arquivo.readlines()))
            
    # Erro sem informação no arquivo
    except json.decoder.JSONDecodeError:
        
        # Escreve um dicionario vazio no arquivo
        with open(arquivo, "w") as arquivo:
            dictVazio = {}
            json.dump(dictVazio, arquivo, indent=4)

def importarArquivo(nomeArquivo):
    # Importa o Arquivo
    arquivo = redirecionarCaminho(adicionarExtensaoJson(nomeArquivo))
    
    # Abre o Arquivo
    with open(arquivo, "r") as arquivo:
        
        # Carrega os Dados
        dicionarioBanco = json.loads("\n".join(arquivo.readlines()))
        
    # Retorna o Dicionario
    return dicionarioBanco

def salvarArquivo(informacao, nomeArquivo):
    # Salva os dados no Arquivo
    arquivo = redirecionarCaminho(adicionarExtensaoJson(nomeArquivo))
    
    # Abre o arquivo
    with open(arquivo,"w") as arquivo:
        
        # Salva os dados no arquivo
        json.dump(informacao, arquivo, indent=4)
        
def salvarAluno(aluno, arquivo):
    # Transforma o Aluno (Objeto) em informações de dicionario
    def aluno_para_dict(aluno):
        return{
            "nome" : aluno.nome,
            "idade": aluno.idade,
            "notas": aluno.notas
            }
    
    # Pega o arquivo (dict) e passa as informações do aluno
    arquivo[aluno.usuario] = aluno_para_dict(aluno)
    
    # Retorna o Dict modificado
    return arquivo

def salvarProfessor(prof, arquivo):
    # Transforma o Professor (Objeto) em informações de dicionario
    def prof_para_dict(prof):
        return {
            "nome" : prof.nome,
            "idade": prof.idade,
            "materia": prof.materia
        }
     
    # Pega o arquivo (dict) e passa as informações do Professor   
    arquivo[prof.usuario] = prof_para_dict(prof)
    
    # Retorna o Dict modificado
    return arquivo
        
def adicionarUsuario(nomeCompleto="", cargo=""):
    # Adiciona um Novo usuário para criação de uma nova pessoa no sistema
    
    def criacaoUsuario(nomeCompleto, cargo):
        # Cria um usuário novo
        user = f"{nomeCompleto.split()[0]}{nomeCompleto.split()[-1]}{cargo[:2]}".lower()
        cont = 0
        
        # Garante que o Usuário é completamente único
        userExist = ver.verificacaoUsuarioExiste(user)
        
        # Só sai do Laço quando o Usuário é Unico
        while userExist:
            cont += 1
            user = user = f"{nomeCompleto.split()[0]}{nomeCompleto.split()[-1]}{cont:02}{cargo[:2]}".lower()
            userExist = ver.verificacaoUsuarioExiste(user)
            
        return user.lower()
    
    # Cria o usuário a partir do nome completo e o cargo no sistema
    user = criacaoUsuario(nomeCompleto, cargo)
    return user