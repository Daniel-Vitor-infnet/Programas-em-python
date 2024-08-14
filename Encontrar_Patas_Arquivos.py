import os

def listar_arquivos_com_extensao(caminho_pasta, extensao, incluir_subpastas=False):
    """Lista arquivos e pastas com uma extensão específica."""
    resultados = []
    if incluir_subpastas:
        for root, dirs, files in os.walk(caminho_pasta):
            for file in files:
                if file.endswith(extensao):
                    resultados.append(os.path.join(root, file))
    else:
        for item in os.listdir(caminho_pasta):
            caminho_completo = os.path.join(caminho_pasta, item)
            if os.path.isfile(caminho_completo) and item.endswith(extensao):
                resultados.append(caminho_completo)
            elif os.path.isdir(caminho_completo):
                resultados.append(caminho_completo)
    return resultados

def listar_arquivos_sem_extensao(caminho_pasta, incluir_subpastas=False):
    """Lista todos os arquivos e pastas sem se preocupar com a extensão."""
    resultados = []
    if incluir_subpastas:
        for root, dirs, files in os.walk(caminho_pasta):
            for file in files:
                resultados.append(os.path.join(root, file))
            for dir in dirs:
                resultados.append(os.path.join(root, dir))
    else:
        for item in os.listdir(caminho_pasta):
            caminho_completo = os.path.join(caminho_pasta, item)
            if os.path.isfile(caminho_completo) or os.path.isdir(caminho_completo):
                resultados.append(caminho_completo)
    return resultados

def main():
    print("Escolha uma das opções abaixo:")
    print("1. Listar todos arquivos e pastas com extensão específica da pasta informada")
    print("2. Listar todos arquivos e pastas sem se preocupar com a extensão da pasta informada")
    print("3. Listar todos arquivos e subpastas com extensão específica até o fim da pasta informada")
    print("4. Listar todos arquivos e subpastas sem se preocupar com a extensão até o fim da pasta informada")

    escolha = input("Digite o número da sua escolha: ").strip()

    if escolha not in {'1', '2', '3', '4'}:
        print("Opção inválida. Encerrando o programa.")
        return

    caminho_pasta = input("Informe o caminho da pasta (ex: C:\\Program Files (x86)\\Steam): ").strip()

    if not os.path.exists(caminho_pasta):
        print("Caminho inválido. Verifique o caminho informado e tente novamente.")
        return

    if escolha in {'1', '3'}:
        extensao = input("Informe a extensão desejada (ex: .txt): ").strip()
        if not extensao.startswith('.'):
            extensao = '.' + extensao

    if escolha == '1':
        resultados = listar_arquivos_com_extensao(caminho_pasta, extensao, incluir_subpastas=False)
    elif escolha == '2':
        resultados = listar_arquivos_sem_extensao(caminho_pasta, incluir_subpastas=False)
    elif escolha == '3':
        resultados = listar_arquivos_com_extensao(caminho_pasta, extensao, incluir_subpastas=True)
    elif escolha == '4':
        resultados = listar_arquivos_sem_extensao(caminho_pasta, incluir_subpastas=True)

    if resultados:
        print("\nResultados encontrados:")
        for resultado in resultados:
            print(resultado)
    else:
        print("Nenhum resultado encontrado.")

if __name__ == "__main__":
    main()
