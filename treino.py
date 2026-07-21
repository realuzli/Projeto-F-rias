import utils as ut
import exercicio as ex
import datetime as dt

def adicionar_treino(treinos_adicionados,exercicios_adicionados): # Adicionar a validação de não permitir adicionar mais de um treino por exercício no dia. Exemplo: adicionar dois treinos de supino no mesmo dia
    print("\n=== [ Adicionar Treino ] ===")
    while True:
        ex.listar_tipos_treino(exercicios_adicionados)
        tipo_treino = str(input("Digite a divisão/tipo de treino: "))
        if tipo_treino not in exercicios_adicionados.keys():
            print(f"\n[!] O tipo de treino '{tipo_treino}' não está cadastrado.")
            print(f"[!] Digite um tipo de treino válido.")
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
            print(f"[!] Digite um exercício adicionado.")
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

        print(f"\n[✔] Treino de '{nome_exercicio_adicionado}' adicionado com sucesso!")
        while True:
            pergunta = str(input(f"Deseja adicionar mais um exercício do treino de '{tipo_treino}'? (S/N): "))
            if pergunta.strip().upper() == "N":
                return treinos_adicionados, exercicios_adicionados
            else:
                break

def alterar_treino(treinos_adicionados,exercicios_adicionados):
    print("\n=== [ Alterar Treino ] ===")
    while True: # Procura um tipo de treino válido
        ex.listar_tipos_treino(exercicios_adicionados)
        tipo_treino = str(input("Digite a divisão/tipo de treino: "))
        if tipo_treino not in exercicios_adicionados:
            print(f"\n[!] O tipo de treino '{tipo_treino}' não está cadastrado.")
            print(f"[!] Digite um tipo de treino válido.")
        else:
            break
    
    while True: # Procura um exercício válido no tipo de treino escolhido
        ex.listar_exercicios_especifico(exercicios_adicionados,tipo_treino)
        exercicio_escolhido = str(input("Digite o nome do exercício: "))
        if exercicio_escolhido not in exercicios_adicionados[tipo_treino]:
            print(f"\n[!] O exercício '{exercicio_escolhido}' não está adicionado no tipo de treino '{tipo_treino}'.")
            print(f"[!] Digite um exercício adicionado.")
        else:
            if exercicio_escolhido not in treinos_adicionados[tipo_treino]:
                print(f"\n[!] O exercício '{exercicio_escolhido}' não tem nenhum treino adicionado!")
                print(f"[!] Digite um exercício que tenha um treino adicionado.")
            else:
                break

    lista_opcoes = ["carga","reps"]
    while True: # Valida a data de entrada e procura se tem algum treino adicionado com essa data
        flag_achou_treino = False
        data_input = str(input("Digite a data do treino (dd-mm-aa): "))
        try:
            data_validada = dt.datetime.strptime(data_input, "%d-%m-%y").strftime("%d-%m-%y")
            for i in range(len(treinos_adicionados[tipo_treino][exercicio_escolhido])):
                if treinos_adicionados[tipo_treino][exercicio_escolhido][i]["data"] == data_validada:
                    posicao_data_treino = i
                    flag_achou_treino = True
                    break

            if not flag_achou_treino:
                print(f"\n[!] Nenhum treino adicionado na data '{data_validada}'!")
                listar_treino_especifico(treinos_adicionados,tipo_treino,exercicio_escolhido)
            else:
                break
        except ValueError:
            print("\n[!] Data inválida. Use o formato dd-mm-aa.")

    while True: # Valida qual campo será alterado
        alteracao = str(input("O que você deseja alterar [carga,reps]? "))
        if alteracao not in lista_opcoes:
            print(f"\n[!] Digite uma opção de alteração válida [carga/reps]!")
        else:
            break

    lista_series = treinos_adicionados[tipo_treino][exercicio_escolhido][posicao_data_treino]["series"]
    while True: # Valida qual série será alterada
        alteracao_em_serie = int(input("Qual série você deseja realizar essa alteração? "))
        if alteracao_em_serie < 1 or alteracao_em_serie > len(lista_series):
            print(f"\n[!] Digite uma série válida. Foram registradas {len(lista_series)} série(s) nesse treino.")
        else:
            break

    if alteracao == "carga":
        novo_valor = float(input("Digite a nova carga (Kg): "))
    else:
        novo_valor = int(input("Digite a nova quantidade de repetições: "))

    lista_series[alteracao_em_serie-1][alteracao] = novo_valor
    print(f"\n[✔] Série {alteracao_em_serie} do exercício '{exercicio_escolhido}' alterada com sucesso!")

    return treinos_adicionados

def listar_rpe():
    print("\n=== [ Adicionar RPE ] ===")
    while True:
        lista_nomes_rpe = ["Peso/Aquecimento","Moderado/Pesado","Dificil","Muito Difícil","Esforço máximo/Falha"]
        print(
            "\n[1] - Peso/Aquecimento",
            "\n[2] - Moderado/Pesado - 3 repetições",
            "\n[3] - Difícil - 2 repetições",
            "\n[4] - Muito Difícil - 1 repetição",
            "\n[5] - Esforço máximo - Falha"
        )
        escolha_rpe = int(input("Digite o RPE da sua série: "))
        if 0 < escolha_rpe <= len(lista_nomes_rpe):
            return lista_nomes_rpe[escolha_rpe-1]
        else:
            print(f"\n[!] Digite uma opção válida.")


def listar_observacao():
    print("\n=== [ Adicionar Observação ] ===")
    while True:
        lista_nomes_obs = ["Aquecimento","Normal","Falha","RestPause","Roubado"]
        print(
            "\n[1] - Aquecimento",
            "\n[2] - Normal",
            "\n[3] - Falha",
            "\n[4] - RestPause",
            "\n[5] - Roubado"
        )
        escolha_obs = int(input("Digite a observação da sua série: "))
        if 0 < escolha_obs <= len(lista_nomes_obs):
            return lista_nomes_obs[escolha_obs-1]
        else:
            print(f"\n[!] Digite uma opção válida.")


def listar_treino_especifico(treinos_adicionados, tipos_treino, nome_exercicio):
    print(f"\n=== [ Treinos de '{nome_exercicio}' ] ===")
    for sessao in treinos_adicionados[tipos_treino][nome_exercicio]:
        print(f"\nData do treino: '{sessao['data']}'")
        for serie in sessao["series"]:
            for key, value in serie.items():
                print(f" '{key}' -> '{value}' ", end=" ")
            print()

def listar_treino_completo(treinos_adicionados):
    print("\n=== [ Todos os Treinos Registrados ] ===")
    for tipo_treino in treinos_adicionados:
        for nome_exercicio in treinos_adicionados[tipo_treino]:
            for sessao in treinos_adicionados[tipo_treino][nome_exercicio]:
                print(f"\nData do treino: '{sessao['data']}'")
                for serie in sessao["series"]:
                    for key,value in serie.items():
                        print(f" '{key}' -> '{value}' ",end=" ")
                    print()

def remover_treino_completo(treinos_adicionados,exercicios_adicionados):
    print("\n=== [ Remover Treino ] ===")
    while True: # Procura um tipo de treino válido
        ex.listar_tipos_treino(exercicios_adicionados)
        tipo_treino = str(input("Digite a divisão/tipo de treino: "))
        if tipo_treino not in exercicios_adicionados:
            print(f"\n[!] O tipo de treino '{tipo_treino}' não está cadastrado.")
            print(f"[!] Digite um tipo de treino válido.")
        else:
            break
    
    while True: # Procura um exercício válido no tipo de treino escolhido
        ex.listar_exercicios_especifico(exercicios_adicionados,tipo_treino)
        exercicio_escolhido = str(input("Digite o nome do exercício: "))
        if exercicio_escolhido not in exercicios_adicionados[tipo_treino]:
            print(f"\n[!] O exercício '{exercicio_escolhido}' não está adicionado no tipo de treino '{tipo_treino}'.")
            print(f"[!] Digite um exercício adicionado.")
        else:
            if exercicio_escolhido not in treinos_adicionados[tipo_treino]:
                print(f"\n[!] O exercício '{exercicio_escolhido}' não tem nenhum treino adicionado!")
                print(f"[!] Digite um exercício que tenha um treino adicionado.")
            else:
                break
    
    while True: # Valida a data de entrada e procura se tem algum treino adicionado com essa data
        flag_achou_treino = False
        data_input = str(input("Digite a data do treino (dd-mm-aa): "))
        try:
            data_validada = dt.datetime.strptime(data_input, "%d-%m-%y").strftime("%d-%m-%y")
            for i in range(len(treinos_adicionados[tipo_treino][exercicio_escolhido])):
                if treinos_adicionados[tipo_treino][exercicio_escolhido][i]["data"] == data_validada:
                    posicao_data_treino = i
                    flag_achou_treino = True
                    break

            if not flag_achou_treino:
                print(f"\n[!] Nenhum treino adicionado na data '{data_validada}'!")
                listar_treino_especifico(treinos_adicionados,tipo_treino,exercicio_escolhido)
            else:
                treinos_adicionados[tipo_treino][exercicio_escolhido].pop(posicao_data_treino)
                if not treinos_adicionados[tipo_treino][exercicio_escolhido]:
                    del treinos_adicionados[tipo_treino][exercicio_escolhido]
                print(f"\n[✔] Treino removido com sucesso!")
                return treinos_adicionados
        except ValueError:
            print("\n[!] Data inválida. Use o formato dd-mm-aa.")
