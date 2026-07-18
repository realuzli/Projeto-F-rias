import os 
def limpar_tela():
    os.system('cls' if os.name== 'nt' else 'clear')

def pausar_execucao():
    input(f"Pressione 'Enter' para continuar.")