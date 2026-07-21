import exercicio as ex
import utils as ut
import treino as tr
import json
from pathlib import Path
import csv

def salvar_csv(lista_dados):
    path = Path.cwd()
    path = Path.joinpath("Arquivos","treinos.csv")
    with open(path,"w",newline='') as arquivo:
        fieldnames = ["tipo_treino","nome_exercicio","data","serie","carga","peso","rpe","obs"]
        escritor_csv = csv.writer(arquivo,delimiter=";",fieldnames=fieldnames)
        escritor_csv = escritor_csv.writeroww(lista_dados)        

def salvar_json(path,conteudo_json,nome_arquivo):
    with open(path,"w") as arquivo:
        json.dump(conteudo_json,arquivo,ensure_ascii=False,indent=4)
    
    print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")

def salvar_dados(treinos_adicionados,exercicios_adicionados):
    diretorio_atual = Path.cwd()    
    diretorio_arquivos = Path("Arquivos")
    
    if not diretorio_arquivos.exists():
        print(f"Confirmação: a pasta não existe")
        print(f"Pasta sendo criada agora!")
        diretorio_arquivos.mkdir()
    
    lista_arquivos = ["exercicios.json","treinos.json","treinos.csv"]
    
    path_atual = Path.cwd()
    path_final_arquivo = path_atual.joinpath(diretorio_arquivos,lista_arquivos[0])
    salvar_json(path_final_arquivo,exercicios_adicionados,lista_arquivos[0])
    
    path_final_arquivo = path_atual.joinpath(diretorio_arquivos,lista_arquivos[1])
    salvar_json(path_final_arquivo,treinos_adicionados,lista_arquivos[1])

 
def leitura_treinos_adicionados(treinos_adicionados):
    for tipos_treino in treinos_adicionados.keys(): # Pegando cada tipo de treino diferente
        print(tipos_treino)
        for exercicios in treinos_adicionados[tipos_treino].keys(): # Pegando cada exercicio diferente com base no tipo de treino da vez
            print(exercicios)
            #print(treinos_adicionados[tipos_treino][exercicios])
            for registros_treino in treinos_adicionados[tipos_treino][exercicios]: # Pega cada registro de treino adicionado desse exercicio
                for i in range(len(registros_treino['series'])):
                    lista_final = []
                    data = (registros_treino['data'])
                    lista_final.append(tipos_treino)
                    lista_final.append(exercicios)
                    lista_final.append(data)
                    for key,values in  registros_treino['series'][i].items():
                        lista_final.append(values)
                    salvar_csv(lista_final)
                
def carregar_dados():
    pass


def main():
    treinos_adicionados = {}
    exercicios_adicionados = {}

    exercicios_adicionados = ex.adicionar_exercicio(exercicios_adicionados)
    treinos_adicionados,exercicios_adicionados = tr.adicionar_treino(treinos_adicionados,exercicios_adicionados)

    salvar_dados(treinos_adicionados,exercicios_adicionados)
    leitura_treinos_adicionados(treinos_adicionados)
   


main()
