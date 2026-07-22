import exercicio as ex
import utils as ut
import treino as tr
import json
from pathlib import Path
import csv

def salvar_csv(lista_dados):
    path_atual = Path.cwd()
    diretorio_arquivos = Path("arquivos")
    path_final_arquivo = path_atual.joinpath(diretorio_arquivos,"treinos.csv")

    with open(path_final_arquivo,"w",newline='') as arquivo:
        fieldnames = ["tipo_treino","nome_exercicio","data","series_totais","serie","carga","peso","rpe","obs"]
        writer = csv.writer(arquivo)
        writer.writerow(fieldnames)
        writer.writerows(lista_dados)
    print(f"\n[✔] Arquivo 'treinos.csv' salvo com sucesso.")

def salvar_json(path,conteudo_json,nome_arquivo):
    with open(path,"w") as arquivo:
        json.dump(conteudo_json,arquivo,ensure_ascii=False,indent=4)
    
    print(f"\n[✔] Arquivo '{nome_arquivo}' salvo com sucesso.")

def salvar_dados(treinos_adicionados,exercicios_adicionados):
    print("\n=== [ Salvando Dados ] ===")
    diretorio_arquivos = Path("arquivos")    
    if not diretorio_arquivos.exists():
        print(f"\n[!] A pasta de dados não existe.")
        print(f"[!] Criando a pasta agora...")
        diretorio_arquivos.mkdir()
    
    lista_arquivos = ["exercicios.json","treinos.json","treinos.csv"]
    
    path_atual = Path.cwd()
    path_final_arquivo = path_atual.joinpath(diretorio_arquivos,lista_arquivos[0])
    salvar_json(path_final_arquivo,exercicios_adicionados,lista_arquivos[0])
    
    path_final_arquivo = path_atual.joinpath(diretorio_arquivos,lista_arquivos[1])
    salvar_json(path_final_arquivo,treinos_adicionados,lista_arquivos[1])
    leitura_treinos_adicionados(treinos_adicionados)

 
def leitura_treinos_adicionados(treinos_adicionados):
    lista_final = []
    for tipos_treino in treinos_adicionados.keys(): # Pegando cada tipo de treino diferente
        for exercicios in treinos_adicionados[tipos_treino].keys(): # Pegando cada exercicio diferente com base no tipo de treino da vez
            for registros_treino in treinos_adicionados[tipos_treino][exercicios]: # Pega cada registro de treino adicionado desse exercicio
                for i in range(len(registros_treino['series'])):
                    lista = []
                    data = (registros_treino['data'])
                    lista.append(tipos_treino)
                    lista.append(exercicios)
                    lista.append(data)
                    lista.append(len(registros_treino['series']))
                    lista.append(i+1)
                    for key,values in  registros_treino['series'][i].items():
                        lista.append(values)
                    lista_final.append(lista)
    salvar_csv(lista_final)
                
def carregar_dados(nome_arquivo):
    diretorio_atual = Path.cwd()
    diretorio_arquivos = Path("arquivos")
    path_arquivo = diretorio_atual.joinpath(diretorio_arquivos,nome_arquivo)
    try:
        with open(path_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except json.decoder.JSONDecodeError:
        print(f"\n[!] Erro ao ler '{nome_arquivo}': sem dados para carregar.")
        return {}
    except FileNotFoundError:
        print(f"\n[!] Arquivo '{nome_arquivo}' ainda não existe. Começando do zero.")
        return {}

