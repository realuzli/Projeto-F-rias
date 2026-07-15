import pandas as pd
import numpy as np
import matplotlib.pylab as mlb


def registrar_treino():
    dicionarioRegistroTreino = {}

    print("\nBem-vindo, vamos registrar o seu treino!")
    print("\nPrecisamos que você responda algumas perguntas antes de registrarmos o seu treino!")

    while True:
        try:
            qtdTreinosSemana = int(input("Quantos dias você treina na semana? "))
            break
        except ValueError:
            print("\nPor favor, digite um numero inteiro.")

    tiposTreino = []

    for _ in range(qtdTreinosSemana):
        nomeTipoTreino = str(input((f"Diga o nome da sua divisão de treino do dia {_ + 1}: ")))
        tiposTreino.append(nomeTipoTreino)
        dicionarioRegistroTreino[nomeTipoTreino] = {}

    for _ in range(qtdTreinosSemana):
        print(f"Dia {_+1} -> {tiposTreino[_]}")



    while True:
        try:
            qtdExerciciosTreino = int(input("Quantos exercícios em média por tipo de treino? "))
            break
        except ValueError:
             print("\nPor favor, digite um numero inteiro.")

    for i in range(qtdTreinosSemana):
        print(f"\nVamos adicionar os exercícios do dia {tiposTreino[i]}")
        for _ in range(qtdExerciciosTreino):
            exercicio = str(input((f"Exercício {_ +1}: ")))
            dicionarioRegistroTreino[tiposTreino[i]][exercicio] = {"series":[],"reps":[],"carga":[]}
    
#    print(dicionarioRegistroTreino)
    return dicionarioRegistroTreino
def adicionartreino():
    pass

def main():
    while True:
        try:
            print("Escolha o modo de funcionamento do aplicativo:")
            print("\nOpções de funcionamento do aplicativo disponíveis:\n",
            "[1] - Registrar um treino\n",
            "[2] - Adicionar um treino\n",
            "[3] - Consultar os dados de treino\n", 
            "[0] - Sair do progama")

            opcao = int(input("\nOpção de funcionamento escolhida: "))
            break
            
        except ValueError:
            print("\nDigite uma opção válida!")
        
        
    match opcao:
        case 1:
            print("\nVocê escolheu a opção de registrar um treino!")
            print("\nVamos começar!")
            treino = registrar_treino()
            print("Seu treino foi registrado com sucesso.")
            pergunta = str(input("Deseja adicionar um treino?"))

            if pergunta == "S":
                treino = adicionartreino(treino)
            if pergunta == "N":
                pass
        case 2:
            print("\nVocê escolheu a opção de adicionar um treino!")
            print("Vamos começar!")

        case 3:
            print("\nVocê escolheu a opção de consultar os dados de treino!")
            print("\nVamos começar!")
            
        case 0:
            print("\nVocê escolheu a opção de encerrar o progama!")
            print("\nAté breve!")
           
            
        
       





 




if __name__ == "__main__":
    main()






