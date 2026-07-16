import pandas as pd
import numpy as np
import matplotlib.pylab as mlb
import datetime as dt
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
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
    dicionarioExercicio = {}

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
        dicionarioExercicio[tiposTreino[i]] = []

        for _ in range(qtdExerciciosTreino):
            exercicio = str(input((f"Exercício {_ +1}: ")))
            
            dicionarioRegistroTreino[tiposTreino[i]][exercicio] = {"series":[],"reps":[],"carga":[]}        
            dicionarioExercicio[tiposTreino[i]].append(exercicio)
           
    
  
    return dicionarioRegistroTreino,dicionarioExercicio,tiposTreino


def adicionar_treino(tipo_de_treino, dicionario_treino,exercicios_treino):
    while True:
        listar_Treino(tipo_de_treino,exercicios_treino)
        exercicio_adicionado = str(input("Qual o exercício adicionado? "))
        if exercicio_adicionado in dicionario_treino[tipo_de_treino]:
            break
        else:
            print("Digite o nome de um exercício registrado.")

    quantidade_series = int(input("Quantidade de séries? "))

    for i in range(quantidade_series):
        carga = float(input((f"Carga da {i+1}° série: ")))
        reps = int(input((f"Repetições da {i+1}° série: ")))
        dicionario_treino[tipo_de_treino][exercicio_adicionado]["series"].append(i)
        dicionario_treino[tipo_de_treino][exercicio_adicionado]["carga"].append(carga)
        dicionario_treino[tipo_de_treino][exercicio_adicionado]["reps"].append(reps)
    listar_Treino(tipo_de_treino,dicionario_treino)





    
def listar_Treino(tipo_de_treino,exercicios_treino):
    limpar_tela()
    print("Escolha uma das opções de tipos de treino para listar: ")
        
    for i in range(len(tipo_de_treino)):
        print(f"Opção {i+1} - {tipo_de_treino[i]}")

    escolhido = int(input("Escolhido: "))
    
    
    for key,value in exercicios_treino.items():
        if key==tipo_de_treino[escolhido-1]:
            print(f"Treino {key} | Exercícios -> {value}")
            


def consultar_Treino(tipo_de_treino,dicionario_treino):
    limpar_tela()
    if KeyError:
        print(f"O treino ainda não foi adicionado.")
        print(f"Tente adicionar um treino para poder consultar.")
    else:
        for key,value in dicionario_treino[tipo_de_treino].items():
            print(f"Treino {key} | Exercícios -> {value}")

def main():
    registro_exercicios_do_treino ={}
    registro_do_treino = {}
    tipos_de_treino = []
    while True:
        limpar_tela()  
        print("Escolha o modo de funcionamento do aplicativo:")
        print("\nOpções de funcionamento do aplicativo disponíveis:\n",
        "[1] - Registrar um treino\n",
        "[2] - Adicionar um treino\n",
        "[3] - Consultar os dados de treino\n",
        "[4] - Listar treino\n",
        "[0] - Sair do progama")

        opcao = int(input("\nOpção de funcionamento escolhida: "))

        if opcao == 1:
            print("\nVocê escolheu a opção de registrar um treino!")
            print("\nVamos começar!")
            
            registro_do_treino,registro_exercicios_do_treino,tipos_de_treino = registrar_treino()
            tipos_de_treino = list(registro_exercicios_do_treino.keys())            
            print("Seu treino foi registrado com sucesso.")
        
        elif opcao == 2:
            if  not registro_do_treino:
                print("Nenhum treino registrado no momento.")
            
            else:
                print("\nVocê escolheu a opção de adicionar um treino!")
                for i in range(len(tipos_de_treino)):
                    print(f"Opção {i+1} - {tipos_de_treino[i]}")

                    escolhido = int(input("Escolhido: "))
                adicionar_treino(tipos_de_treino[escolhido-1],registro_do_treino,registro_exercicios_do_treino)
                
        
        elif opcao== 3: 
            if not registro_do_treino:
                print(f"Nenhum exercício registrado no momento.")
                print(f"Tente registrar primeiro.")
            
            else:       
                print("\nVocê escolheu a opção de consultar os dados de treino!")
                print("Digite o numero de um dos tipos de treino: ")
        
                for i in range(len(tipos_de_treino)):
                    print(f"{i+1} - {tipos_de_treino[i]}")

                escolhido = int(input("Escolhido: "))
                consultar_Treino(tipos_de_treino[escolhido-1],registro_do_treino)
        
        elif opcao== 4:
            if not registro_do_treino:
                print("Nenhum treino registrado no momento.")
            
            else:
                listar_Treino(tipos_de_treino,registro_exercicios_do_treino)
                
        elif opcao== 0:
            print("\nVocê escolheu a opção de encerrar o progama!")
            print("Até breve!")
            break
        
        else:
            print("Digite uma opção válida.")
        
if __name__ == "__main__":
    main()
