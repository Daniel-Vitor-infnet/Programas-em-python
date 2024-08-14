import os
from tqdm import tqdm

def carregar_lista(caminho):
    """Carrega uma lista de filmes/séries de um arquivo txt."""
    # Remove aspas duplas e espaços extras do caminho
    caminho = caminho.strip().strip('"')
    
    # Verifica se o arquivo existe antes de tentar carregar
    if not os.path.exists(caminho):
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        return []
    
    with open(caminho, 'r', encoding='utf-8') as file:
        return [linha.strip() for linha in file.readlines() if linha.strip()]

def remover_duplicados(lista, listas_referencia):
    """Remove itens da lista original que estão presentes nas listas de referência."""
    lista_filtrada = []
    for item in tqdm(lista, desc="Comparando listas", unit="item"):
        duplicado = False
        for referencia in listas_referencia:
            if item in referencia:
                duplicado = True
                break
        if not duplicado:
            lista_filtrada.append(item)
    return lista_filtrada

def processar_lista(tipo_escolhido, caminho_lista, pasta_formatada):
    # Carrega a lista principal
    lista_principal = carregar_lista(caminho_lista)
    
    if not lista_principal:
        print("Nenhuma entrada foi carregada da lista principal. Verifique o arquivo e tente novamente.")
        return

    # Define os caminhos dos arquivos de referência
    arquivos_referencia = ["Ignorar.txt", "ParaAssistir.txt", "TalvezVer.txt", "Historico.txt"]

    # Carrega as listas de referência
    listas_referencia = []
    for arquivo in arquivos_referencia:
        caminho_referencia = os.path.join(pasta_formatada, arquivo)
        if os.path.exists(caminho_referencia):
            listas_referencia.append(carregar_lista(caminho_referencia))

    # Remove duplicados da lista principal
    lista_filtrada = remover_duplicados(lista_principal, listas_referencia)

    # Define o caminho de saída
    caminho_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Filmes\Recomendações.txt"

    # Salva o resultado
    with open(caminho_saida, 'w', encoding='utf-8') as file:
        if not lista_filtrada:
            file.write("Não foi dessa vez vc já viu todos 😢\n")
        else:
            for item in lista_filtrada:
                file.write(f"{item}\n")

    print(f"Resultado salvo em: {caminho_saida}")

# Passo 1: Perguntar se é filme ou série
tipo_escolhido = input("Deseja processar filmes ou séries? ").strip().lower()

# Mapear os tipos possíveis para filmes e séries
tipos_filmes = {'movie', 'movies', 'filmes', 'filme'}
tipos_series = {'serie', 'series', 'show', 'shows'}

if tipo_escolhido in tipos_filmes:
    pasta_formatada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Filmes\Lista Formatada\Filmes"
elif tipo_escolhido in tipos_series:
    pasta_formatada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Filmes\Lista Formatada\Series"
else:
    print("Tipo inválido. Escolha entre filmes ou séries.")
    exit()

# Passo 2: Perguntar onde está a lista
caminho_lista = input("Por favor, informe o caminho completo da lista (ex: C:\\Batata\\lista.txt): ").strip()

# Passo 3 e 4: Processar a lista e comparar com as listas de referência
processar_lista(tipo_escolhido, caminho_lista, pasta_formatada)
