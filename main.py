import os
def limpar_tela():
    os.system('cls' if os.name== 'nt' else 'clear')

def registrar_treino():
    registro_de_treino = {}
    exercicios_registrados = {}
    tipos_treino = []

    print(f"Vamos começar o registro do seu treino!")
    print(f"Precisamos que você responda algumas perguntas antes de começarmos!")

    while True:
        try:
            quantidade_de_tipos_de_treino_diferentes = int(input("Quantos dias possui a sua divisão de treino? "))
            break
        except ValueError:
            print("Por favor, digite um numero inteiro.")
    limpar_tela()

    for dia in range(quantidade_de_tipos_de_treino_diferentes):
        nome_tipo_treino = str(input(f"Diga o {dia+1}° nome da sua divisão de treino: ")).upper()
        tipos_treino.append(nome_tipo_treino)
        registro_de_treino[nome_tipo_treino] = {}

    for diaS in range(quantidade_de_tipos_de_treino_diferentes):
        while True:
            try:
                limpar_tela()
                quantidade_exercicios = int(input(f"Quantos exercícios no dia de {tipos_treino[diaS]}? "))
                exercicios_registrados[tipos_treino[diaS]] = []
                break
            except ValueError:
                print("Digite um numero inteiro.")
        for nomes in range(quantidade_exercicios):
            nome_exercicio = str(input("Nome do exercício: ")).upper()
            registro_de_treino[tipos_treino[diaS]][nome_exercicio] = []
            exercicios_registrados[tipos_treino[diaS]].append(nome_exercicio)
            print(f"Exercício {nome_exercicio} adicionado com sucesso no dia de {tipos_treino[diaS]}!")

    pausar_execucao()
    return registro_de_treino,exercicios_registrados,tipos_treino
  
def adicionar_treino(registro_de_treino,tipos_de_treino,exercicios_registrados):
    tipo_de_treino_escolhido = escolher_tipo_de_treino(tipos_de_treino)
    exercicio_escolhido = escolher_exercicio(tipo_de_treino_escolhido,exercicios_registrados)
    print(f"Exercício escolhido -> {exercicio_escolhido} | Tipo de treino do exercício escolhido -> {tipo_de_treino_escolhido}")

    quantidade_series = int(input("Quantidade de séries desse exercício?"))

    for quantidade in range(quantidade_series):
        carga = float(input(f"Carga da {quantidade+1}° série: "))
        reps = int(input(f"Repetições da {quantidade+1}° série: "))
        registro_de_treino[tipo_de_treino_escolhido][exercicio_escolhido].append({"série":quantidade+1,"carga":carga,"reps":reps})

    print(f"Treino de {exercicio_escolhido} salvo com sucesso: {registro_de_treino[tipo_de_treino_escolhido][exercicio_escolhido]}")
    pausar_execucao()

def pausar_execucao():
    input("Pressione 'Enter' para continuar: ")

def mostrar_tipos_de_treino(tipos_de_treino):
    for posicao,nome_do_tipo in enumerate(tipos_de_treino):
        print(f"{posicao} -> {nome_do_tipo}")

def escolher_tipo_de_treino(tipos_de_treino):
    while True:
        limpar_tela()
        mostrar_tipos_de_treino(tipos_de_treino)
        tipo_de_treino_escolhido = str(input("Digite o nome do tipo de treino escolhido: ")).upper()
        if tipo_de_treino_escolhido not in tipos_de_treino:
            print("Digite um tipo de treino existente.")
       
        else:
            print(f"Você escolheu [{tipo_de_treino_escolhido}]")
            return tipo_de_treino_escolhido

def mostrar_exercicios_registrados(tipo_de_treino_escolhido,exercicios_registrados):
    for key,value in exercicios_registrados.items():
        if key == tipo_de_treino_escolhido:
            print(f"Tipo de treino [{key}] | Exercícios -> [{value}]")
def escolher_exercicio(tipo_de_treino_escolhido,exercicios_registrados):
    mostrar_exercicios_registrados(tipo_de_treino_escolhido,exercicios_registrados)
    exercicio_escolhido = str(input("Exercício escolhido: ")).upper()
    return exercicio_escolhido
def mostrar_treinos_registrados(registro_de_treino):
    for key,value in registro_de_treino.items():
        print(f"Treino de {key} | Registro -> {value}")    
    pausar_execucao()
def main():
    exercicios_registrados = {}
    tipos_de_treino = []
    registro_de_treino = {}

    while True:
        limpar_tela()
        print("Escolha o modo de funcionamento do terminal: ")
        print("\nOpções de funcionamento do aplicativo disponíveis:\n",
        "[1] - Registrar um treino (criar a divisão dos treinos)\n",
        "[2] - Adicionar um treino (lançar séries,cargas e repetições)\n",
        "[3] - Consultar os dados de treino\n",
        "[4] - Listar exercícios registrados\n",
        "[0] - Sair do progama")

        try:
            opcao_escolhida = int(input("\nOpção escolhida: "))
        except ValueError:
            print("Digite uma opção válida.")
            pausar_execucao()
            continue
        
        match opcao_escolhida:
            
            case 0:
                limpar_tela()
                print("Você escolheu a opção de encerrar o progama!")
                print("Até breve!")
                break
            case 1:
                registro_de_treino,exercicios_registrados,tipos_de_treino = registrar_treino()
            
            case 2:
                if not registro_de_treino:
                    print(f"Nenhum treino registrado.")
                    print(f"Tente registrar um treino primeiro.")
                else:
                    adicionar_treino(registro_de_treino,tipos_de_treino,exercicios_registrados)
            
            case 3:
                if not registro_de_treino:
                    print(f"Nenhum treino registrado.")
                    print(f"Tente registrar um treino primeiro.")
                else:
                    mostrar_treinos_registrados(registro_de_treino)
            
            case 4:
                if not registro_de_treino:
                    print(f"Nenhum treino registrado.")
                    print(f"Tente registrar um treino primeiro.")
                else:
                    tipo_de_treino_escolhido =escolher_tipo_de_treino(tipos_de_treino)
                    mostrar_exercicios_registrados(tipo_de_treino_escolhido,exercicios_registrados)
            
          

if __name__ == "__main__":
    main()