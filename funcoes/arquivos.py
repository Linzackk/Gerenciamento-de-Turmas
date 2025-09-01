# Funções para Lidar com arquivos no geral

import json

def importarArquivo():  
    with open(f"Alunos.json", "r") as arquivo:
        turma_salva = json.loads("\n".join(arquivo.readlines()))
    return turma_salva

def salvarArquivo(informacao):
    with open('Alunos.json',"w") as arquivo:
        json.dump(informacao, arquivo, indent=4)