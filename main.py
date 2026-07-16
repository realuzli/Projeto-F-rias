import pandas as pd
import numpy as np
import matplotlib.pylab as mlb
import datetime as dt
import os
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
def registrar_treino():
    dicionario_registro_treino = {}
    tipos_treino = []
    print("\nBem-vindo, vamos registrar o seu treino!")
    print("\nPrecisamos que você responda algumas perguntas antes de registrarmos o seu treino!")

    while True:
        try:
            qtd_treinos_semana = int(input("Quantos dias você treina na semana? "))
            break
        except ValueError:
            print("\nPor favor, digite um numero inteiro.")


    for _ in range(qtd_treinos_semana):
        nome_tipo_treino = str(input((f"Diga o nome da sua divisão de treino do dia {_ + 1}: ")))
        tipos_treino.append(nome_tipo_treino)
        dicionario_registro_treino[nome_tipo_treino] = {}

    for _ in range(qtd_treinos_semana):
        print(f"Dia {_+1} -> {tipos_treino[_]}")

    for _ in range(len(tipos_treino)):
        quantidade = int (input(f"Quantos exercícios no dia de {tipos_treino[_]}? "))
        for i in range(quantidade):
            nome_exercicio = str(input("Nome do exercício: "))
            dicionario_registro_treino[tipos_treino[_]][nome_exercicio] = {"series":[],"carga":[],"reps":[]}
            print(f"Exercício {nome_exercicio} adicionado com sucesso no dia de {tipos_treino[_]}!")

    
  
    return dicionario_registro_treino,tipos_treino


def adicionar_treino(tipo_de_treino, dicionario_treino):
    while True:
        listar_treino(tipo_de_treino,dicionario_treino)
        exercicio_adicionado = str(input("Qual o exercício adicionado? "))
        if exercicio_adicionado in dicionario_treino[tipo_de_treino]:
            break
        else:
            print("Digite o nome de um exercício registrado.")

    quantidade_series = int(input("Quantidade de séries? "))

    for i in range(quantidade_series):
        carga = float(input((f"Carga da {i+1}° série: ")))
        reps = int(input((f"Repetições da {i+1}° série: ")))
        dicionario_treino[tipo_de_treino][exercicio_adicionado]["series"].append(i+1)
        dicionario_treino[tipo_de_treino][exercicio_adicionado]["carga"].append(carga)
        dicionario_treino[tipo_de_treino][exercicio_adicionado]["reps"].append(reps)
    listar_treino(tipo_de_treino,dicionario_treino)
    
def listar_treino(tipo_de_treino,dicionario_treino):
    limpar_tela()
    print("Escolha uma das opções de tipos de treino para listar: ")
        
    for i in range(len(tipo_de_treino)):
        print(f"Opção {i+1} - {tipo_de_treino[i]}")

    escolhido = int(input("Escolhido: "))
    
    
    for key,value in dicionario_treino.values():
        if key==tipo_de_treino[escolhido-1]:
            print(f"Treino {key} | Exercícios -> {value}")
            
def consultar_treino(tipo_de_treino,dicionario_treino):
    limpar_tela()
    try:
        for key, value in dicionario_treino[tipo_de_treino].items():
            print(f"Treino {key} | Exercícios -> {value}")
    except KeyError:
        print("O treino ainda não foi adicionado.")

def main():
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
            
            registro_do_treino,tipos_de_treino = registrar_treino()
            tipos_de_treino = list(registro_do_treino.keys())            
            print("Seu treino foi registrado com sucesso.")
        
        elif opcao == 2:
            if  not registro_do_treino:
                print("Nenhum treino registrado no momento.")
            
            else:
                print("\nVocê escolheu a opção de adicionar um treino!")
                for i in range(len(tipos_de_treino)):
                    print(f"Opção {i+1} - {tipos_de_treino[i]}")

                escolhido = int(input("Escolhido: "))
                adicionar_treino(tipos_de_treino[escolhido-1],registro_do_treino)
                
        
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
                consultar_treino(tipos_de_treino[escolhido-1],registro_do_treino)
        
        elif opcao== 4:
            if not registro_do_treino:
                print("Nenhum treino registrado no momento.")
            
            else:
                listar_treino(tipos_de_treino,registro_do_treino)
                
        elif opcao== 0:
            print("\nVocê escolheu a opção de encerrar o progama!")
            print("Até breve!")
            break
        
        else:
            print("Digite uma opção válida.")
        
if __name__ == "__main__":
    main()
