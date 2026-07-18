import utils as ut
import exercicio as ex
import datetime as dt

def adicionar_treino(treinos_adicionados,exercicios_adicionados):
    print("\n=== [ Adicionar Treino ] ===")
    while True:
        ex.listar_tipos_treino(exercicios_adicionados)
        tipo_treino = str(input("Digite a divisão/tipo de treino: "))
        if tipo_treino not in exercicios_adicionados.keys():
            print(f"\n[!] O tipo de treino '{tipo_treino}' não está cadastrado.")
            print(f"Digite um tipo de treino válido.")
        else:
            if tipo_treino not in treinos_adicionados:
                treinos_adicionados[tipo_treino] = {}
            break

    data_hoje = dt.datetime.now().strftime("%d-%m-%y")

    while True:
        ex.listar_exercicios_especifico(exercicios_adicionados, tipo_treino)
        nome_exercicio_adicionado = str(input("Digite o nome do exercício para ser adicionado: "))
        if nome_exercicio_adicionado not in exercicios_adicionados[tipo_treino]:
            print(f"\n[!] O exercício '{nome_exercicio_adicionado}' não está adicionado no tipo de treino '{tipo_treino}'.")
            print(f"Digite um exercício adicionado.")
            continue

        if nome_exercicio_adicionado not in treinos_adicionados[tipo_treino]:
            treinos_adicionados[tipo_treino][nome_exercicio_adicionado] = []

        treinos_adicionados[tipo_treino][nome_exercicio_adicionado].append({"data": data_hoje, "series": []})

        quantidade_series = int(input("Quantidade de séries: "))
        for i in range(quantidade_series):
            carga = float(input(f"Digite a carga da '{i+1}°' série: "))
            reps = int(input(f"Digite a quantidade de repetições com {carga} Kg na '{i+1}°' série: "))
            rpe = listar_rpe()
            obs = listar_observacao()
            treinos_adicionados[tipo_treino][nome_exercicio_adicionado][-1]["series"].append(
                {"serie": i+1, "carga": carga, "reps": reps, "rpe": rpe, "obs": obs}
            )

        pergunta = str(input(f"Deseja adicionar mais um exercício do treino de '{tipo_treino}'? (S/N): "))
        if pergunta.strip().upper() == "N":
            break

    return treinos_adicionados, exercicios_adicionados


def alterar_treino():
    pass
def listar_rpe():
    pass

def listar_observacao():
    pass
def listar_treino(treinos_adicionados,exercicios_adicionados): 
    pass


def remover_treino():
    pass

exercicios_adicionados = {}
exercicios_adicionados = ex.adicionar_exercicio(exercicios_adicionados)
treinos_adicionados = {}
treinos_adicionados,exercicios_adicionados =  adicionar_treino(treinos_adicionados,exercicios_adicionados)
print(treinos_adicionados)