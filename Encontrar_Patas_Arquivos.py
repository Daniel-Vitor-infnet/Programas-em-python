import os
from tqdm import tqdm

def listar_arquivos_pastas(caminho_pasta, incluir_subpastas=False, apenas_arquivos=False, apenas_pastas=False, esconder_extensao=False):
    """Lista arquivos e pastas de acordo com as opções fornecidas."""
    resultados = []
    prefixo_arvore = ""

    if incluir_subpastas:
        for root, dirs, files in tqdm(os.walk(caminho_pasta), desc="Procurando arquivos e pastas", unit="iteração"):
            nivel = root.replace(caminho_pasta, "").count(os.sep)
            indent = " " * 4 * (nivel)
            prefixo_arvore = indent + "+---"
            subindent = " " * 4 * (nivel + 1)
            
            if not apenas_arquivos:
                for dir in dirs:
                    resultados.append(f"{prefixo_arvore}{dir}")
                    
            if not apenas_pastas:
                for file in files:
                    nome_arquivo = file if not esconder_extensao else os.path.splitext(file)[0]
                    resultados.append(f"{subindent}{nome_arquivo}")
    else:
        for item in tqdm(os.listdir(caminho_pasta), desc="Procurando arquivos e pastas", unit="arquivo"):
            caminho_completo = os.path.join(caminho_pasta, item)
            if os.path.isfile(caminho_completo):
                if apenas_pastas:
                    continue
                nome_arquivo = item if not esconder_extensao else os.path.splitext(item)[0]
                resultados.append(nome_arquivo)
            elif os.path.isdir(caminho_completo):
                if apenas_arquivos:
                    continue
                resultados.append(item)
    return resultados

def main():
    while True:
        print("Deseja listar:")
        print("1. Apenas arquivos")
        print("2. Apenas pastas")
        print("3. Todos")

        escolha_tipo = input("Digite o número da sua escolha: ").strip()

        if escolha_tipo not in {'1', '2', '3'}:
            print("Opção inválida. Tente novamente.")
            continue

        print("Deseja listar arquivos com extensão?")
        print("1. Sim (mostrar extensão)")
        print("2. Não (não mostrar extensão)")

        escolha_extensao = input("Digite o número da sua escolha: ").strip()

        esconder_extensao = escolha_extensao == '2'

        print("Deseja listar todos os arquivos, pastas e subpastas até o final?")
        print("1. Sim")
        print("2. Não")

        escolha_subpastas = input("Digite o número da sua escolha: ").strip()

        incluir_subpastas = escolha_subpastas == '1'

        caminho_pasta = input("Informe o caminho da pasta (ex: C:\\Program Files (x86)\\Steam): ").strip()

        if not os.path.exists(caminho_pasta):
            print("Caminho inválido. Verifique o caminho informado e tente novamente.")
            continue

        apenas_arquivos = escolha_tipo == '1'
        apenas_pastas = escolha_tipo == '2'

        resultados = listar_arquivos_pastas(caminho_pasta, incluir_subpastas, apenas_arquivos, apenas_pastas, esconder_extensao)

        if resultados:
            print("\nResultados encontrados:")
            for resultado in resultados:
                print(resultado)
        else:
            print("Nenhum resultado encontrado.")

        # Perguntar se deseja finalizar o programa
        deseja_finalizar = input("Deseja finalizar o programa? (sim/não): ").strip().lower()
        if deseja_finalizar in {'sim', 's'}:
            print("Finalizando o programa...")
            break
        else:
            print("Continuando a execução...\n")

if __name__ == "__main__":
    main()
