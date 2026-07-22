import exercicio as ex
import treino as tr
import arquivo
import utils as ut

def exibir_menu():
    print("\n=== [ Menu Principal - Diário de Treino ] ===")
    print("[1] - Adicionar exercício")
    print("[2] - Adicionar treino")
    print("[3] - Alterar exercício")
    print("[4] - Alterar treino")
    print("[5] - Remover exercício")
    print("[6] - Remover treino")
    print("[7] - Listar tipos de treino")
    print("[8] - Listar exercícios (específico)")
    print("[9] - Listar exercícios (completo)")
    print("[10] - Listar treino (específico)")
    print("[11] - Listar treino (completo)")
    print("[0] - Sair")

def main():
    exercicios_adicionados = arquivo.carregar_dados("exercicios.json")
    treinos_adicionados = arquivo.carregar_dados("treinos.json")

    try:
        continuar = True
        while continuar:
            ut.limpar_tela()
            exibir_menu()
            opcao = input("\nEscolha uma opção: ").strip()

            try:
                match opcao:
                    case "1":
                        ut.limpar_tela()
                        exercicios_adicionados = ex.adicionar_exercicio(exercicios_adicionados)
                        ut.pausar_execucao()

                    case "2":
                        ut.limpar_tela()
                        treinos_adicionados, exercicios_adicionados = tr.adicionar_treino(treinos_adicionados, exercicios_adicionados)
                        ut.pausar_execucao()

                    case "3":
                        ut.limpar_tela()
                        exercicios_adicionados = ex.alterar_exercicio(exercicios_adicionados)
                        ut.pausar_execucao()

                    case "4":
                        ut.limpar_tela()
                        treinos_adicionados = tr.alterar_treino(treinos_adicionados, exercicios_adicionados)
                        ut.pausar_execucao()

                    case "5":
                        ut.limpar_tela()
                        exercicios_adicionados = ex.remover_exercicio(exercicios_adicionados)
                        ut.pausar_execucao()

                    case "6":
                        ut.limpar_tela()
                        treinos_adicionados = tr.remover_treino_completo(treinos_adicionados, exercicios_adicionados)
                        ut.pausar_execucao()

                    case "7":
                        ut.limpar_tela()
                        ex.listar_tipos_treino(exercicios_adicionados)
                        ut.pausar_execucao()

                    case "8":
                        ut.limpar_tela()
                        ex.listar_tipos_treino(exercicios_adicionados)
                        tipo_treino = input("\nDigite o tipo de treino para listar os exercícios: ")
                        if tipo_treino not in exercicios_adicionados:
                            print(f"\n[!] O tipo de treino '{tipo_treino}' não está cadastrado.")
                        else:
                            ex.listar_exercicios_especifico(exercicios_adicionados, tipo_treino)
                        ut.pausar_execucao()

                    case "9":
                        ut.limpar_tela()
                        ex.listar_exercicios_completo(exercicios_adicionados)
                        ut.pausar_execucao()

                    case "10":
                        ut.limpar_tela()
                        ex.listar_tipos_treino(exercicios_adicionados)
                        tipo_treino = input("\nDigite o tipo de treino: ")
                        if tipo_treino not in exercicios_adicionados:
                            print(f"\n[!] O tipo de treino '{tipo_treino}' não está cadastrado.")
                        else:
                            ex.listar_exercicios_especifico(exercicios_adicionados, tipo_treino)
                            nome_exercicio = input("\nDigite o nome do exercício: ")
                            if nome_exercicio not in exercicios_adicionados[tipo_treino] or tipo_treino not in treinos_adicionados or nome_exercicio not in treinos_adicionados[tipo_treino]:
                                print(f"\n[!] Não há treinos registrados para '{nome_exercicio}'.")
                            else:
                                tr.listar_treino_especifico(treinos_adicionados, tipo_treino, nome_exercicio)
                        ut.pausar_execucao()

                    case "11":
                        ut.limpar_tela()
                        tr.listar_treino_completo(treinos_adicionados)
                        ut.pausar_execucao()

                    case "0":
                        print("\n[✔] Saindo do programa...")
                        continuar = False

                    case _:
                        print(f"\n[!] Opção '{opcao}' inválida. Escolha uma opção do menu.")
                        ut.pausar_execucao()

            except ValueError:
                print("\n[!] Entrada inválida. Digite um número onde for solicitado.")
                ut.pausar_execucao()
            except KeyError:
                print("\n[!] Não foi possível encontrar o dado solicitado.")
                ut.pausar_execucao()

    finally:
        arquivo.salvar_dados(treinos_adicionados, exercicios_adicionados)

main()