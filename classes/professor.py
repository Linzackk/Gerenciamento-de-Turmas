from funcoes import arquivos as arq
from funcoes import verificacao as ver
from funcoes import estrutura as est

class Professor:
    def __init__ (self, usuario, nome, idade, materia):
        self.usuario = usuario
        self.nome = nome
        self.idade = idade
        self.materia = materia
    
    @est.separacao
    def mostrarMenu(self):
        # Mostra o Menu principal do Professor
        opcoes = ["Atribuir Notas", "Atualizar Dados", "Verificar Informações", "Maior Média", "Menor Média", "Média da Turma"]
        est.mostrarMenu(opcoes, "MENU DO PROFESSOR")
        escolha = ver.verificacaoEscolha(opcoes)
        return escolha
    
    @est.semiSeparacao 
    def verInformacoes(self):
        # Mostra as Informações do Professor
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Materia: {self.materia}")
     
    @est.semiSeparacao    
    def atualizarInformacoes(self):
        # Atualiza as Informações do Professor
        
        def trocar_nome(novoNome):
            # Atualiza Nome
            self.nome = novoNome
    
        def trocar_idade(novaIdade):
            # Atualiza Idade
            self.idade = novaIdade
        
        # Mostra as opções e os numeros correspondentes
        opcoes = ["Alterar Nome", "Alterar Idade"]
        est.mostrarMenu(opcoes, "DADOS ALTERÁVEIS")
        escolha = ver.verificacaoEscolha(opcoes)
        
        # Pega o Novo nome e Atualiza com o método trocar_nome
        if escolha == 1:    
            novoNome = input("Insira seu Novo Nome: ")
            trocar_nome(novoNome)
        
        # Pega o Nova idade e Atualiza com o método trocar_idade  
        elif escolha == 2:
            novaIdade = int(input("Insira sua Nova idade: "))
            trocar_idade(novaIdade)
            
    @est.semiSeparacao         
    def atribuirNotas(self):
        # Atribui notas aos alunos
        usuario = ''
        while not ver.verificacaoUsuarioExiste(usuario):
            # Verifica a Existência do Aluno
            usuario = input("Insira o Usuário do Aluno: ")
        
        # Importa todos alunos
        alunos = arq.importarArquivo("Alunos")
        
        # Seleção da Nota a ser trocada
        opcoes = ["Semestre 1", "Semestre 2"]
        est.mostrarMenu(opcoes, "NOTAS ALTERÁVEIS")
        escolha = ver.verificacaoEscolha(opcoes)
          
        if escolha != 0:    
            nota = -1
            # Atualiza a nota caso for válida
            while nota < 0 or nota > 10:
                nota = float(input("Insira a Nota: "))
            alunos[usuario]["notas"][f"semestre{escolha}"] = nota
            arq.salvarArquivo(alunos, "Alunos")
    
    def mostrarMaiorMedia(self):
        maiorMedia = [0, "nome"]
        alunos = arq.importarArquivo("Alunos")
        for aluno in alunos:
            media = (alunos[aluno]["notas"]["semestre1"] + alunos[aluno]["notas"]["semestre2"]) / 2
            if media > maiorMedia[0]:
                maiorMedia[0], maiorMedia[1] = media, aluno
        print(f"O Aluno(a) com maior media é {alunos[maiorMedia[1]]["nome"]} com uma média de {maiorMedia[0]}")
        
    def mostrarMenorMedia(self):
        menorMedia = [11, "nome"]
        alunos = arq.importarArquivo("Alunos")
        for aluno in alunos:
            media = (alunos[aluno]["notas"]["semestre1"] + alunos[aluno]["notas"]["semestre2"]) / 2
            if media < menorMedia[0]:
                menorMedia[0], menorMedia[1] = media, aluno
        print(f"O Aluno(a) com menor media é {alunos[menorMedia[1]]["nome"]} com uma média de {menorMedia[0]}")
    
    def mediaTurma(self):
        somaTotal = 0
        contador = 0
        alunos = arq.importarArquivo("Alunos")
        for aluno in alunos:
            somaTotal += (alunos[aluno]["notas"]["semestre1"] + alunos[aluno]["notas"]["semestre2"]) / 2
            contador += 1
        print(f"A Média da turma é de {(somaTotal / contador):.1f} com {contador} Alunos na Turma!")