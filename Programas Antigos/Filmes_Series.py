import os
import csv
import random
from tqdm import tqdm
from datetime import datetime

def obter_data_mais_recente(caminho_arquivo):
    """Retorna a data de modificação ou criação mais recente do arquivo."""
    estatisticas = os.stat(caminho_arquivo)
    data_criacao = datetime.fromtimestamp(estatisticas.st_ctime)
    data_modificacao = datetime.fromtimestamp(estatisticas.st_mtime)
    return max(data_criacao, data_modificacao)

def processar_lista(tipo_escolhido, pasta_entrada, pasta_saida):
    # Define os arquivos CSV de entrada
    arquivos_csv = {
        "Ignorar": "Daniel-Vitor-list-ignorar.csv",
        "Favoritos": "Daniel-Vitor-list-melhores.csv",
        "Historico": "Daniel-Vitor-history-all.csv",
        "ParaAssistir": "Daniel-Vitor-list-watchlist.csv",
        "TalvezVer": "Daniel-Vitor-list-talvez-ver.csv"
    }

    # Cria as pastas de saída, se não existirem
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Verifica e processa cada arquivo CSV
    for categoria, nome_arquivo in tqdm(arquivos_csv.items(), desc="Processando categorias", unit="arquivo"):
        caminho_csv = os.path.join(pasta_entrada, nome_arquivo)
        caminho_saida = os.path.join(pasta_saida, f"{categoria}.txt")

        # Verifica se o arquivo CSV existe
        if not os.path.exists(caminho_csv):
            print(f"Arquivo {nome_arquivo} não encontrado. Pulando...")
            continue

        # Verifica a data de modificação/criação mais recente
        data_entrada = obter_data_mais_recente(caminho_csv)
        if os.path.exists(caminho_saida):
            data_saida = obter_data_mais_recente(caminho_saida)
        else:
            data_saida = None

        # Só processa se o arquivo CSV for mais recente ou se não houver arquivo de saída
        if data_saida is None or data_entrada > data_saida:
            print(f"Processando {categoria}...")
            with open(caminho_csv, 'r', encoding='utf-8') as csvfile, open(caminho_saida, 'w', encoding='utf-8') as saida_file:
                leitor_csv = csv.DictReader(csvfile)
                linhas_processadas = 0

                for linha in leitor_csv:
                    if linha['type'].lower() in tipo_escolhido:
                        titulo = linha['title']
                        ano = linha['year']
                        saida_file.write(f"{titulo} ({ano})\n")
                        linhas_processadas += 1

                if linhas_processadas == 0:
                    saida_file.write("Nenhum item encontrado para essa categoria.\n")

def selecionar_favoritos_aleatoriamente(tipo_escolhido, pasta_saida):
    # Define o caminho do arquivo de favoritos baseado no tipo escolhido
    caminho_favoritos = os.path.join(pasta_saida, "Favoritos.txt")
    
    # Verifica se o arquivo de favoritos existe
    if not os.path.exists(caminho_favoritos):
        print(f"Arquivo de favoritos não encontrado: {caminho_favoritos}")
        return

    # Carrega os favoritos do arquivo
    with open(caminho_favoritos, 'r', encoding='utf-8') as file:
        favoritos = [linha.strip() for linha in file.readlines() if linha.strip()]

    if not favoritos:
        print("Nenhum favorito encontrado no arquivo.")
        return

    # Pergunta ao usuário quantos favoritos selecionar
    try:
        num_favoritos = int(input("Quantos favoritos deseja selecionar? ").strip())
        num_favoritos = min(num_favoritos, len(favoritos))

        # Seleciona favoritos aleatoriamente
        favoritos_selecionados = random.sample(favoritos, num_favoritos)

        # Define o caminho de saída baseado no tipo escolhido
        if tipo_escolhido == 'movie':
            caminho_saida_selecionados = r"C:\Users\Administrador\Desktop\Backup (Pc)\Filmes\Melhores\FilmesFavoritos.txt"
        else:
            caminho_saida_selecionados = r"C:\Users\Administrador\Desktop\Backup (Pc)\Filmes\Melhores\SeriesFavoritas.txt"

        # Cria a pasta de saída, se não existir
        os.makedirs(os.path.dirname(caminho_saida_selecionados), exist_ok=True)

        # Salva os favoritos selecionados no arquivo correspondente
        with open(caminho_saida_selecionados, 'w', encoding='utf-8') as file:
            for favorito in favoritos_selecionados:
                file.write(f"{favorito}\n")

        print(f"\nFavoritos selecionados salvos em: {caminho_saida_selecionados}")

    except ValueError:
        print("Número inválido.")

# Loop principal para execução do programa
# Pergunta ao usuário se quer processar filmes ou séries
tipo_escolhido = input("Deseja processar filmes ou séries? ").strip().lower()

# Mapear os tipos possíveis para filmes e séries
tipos_filmes = {'movie', 'movies', 'filmes', 'filme'}
tipos_series = {'serie', 'series', 'show', 'shows'}

if tipo_escolhido in tipos_filmes:
    tipo = 'movie'
    pasta_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Filmes\Lista Formatada\Filmes"
elif tipo_escolhido in tipos_series:
    tipo = 'series'
    pasta_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Filmes\Lista Formatada\Series"
else:
    print("Tipo inválido. Escolha entre filmes ou séries.")

# Define a pasta de entrada e saída
pasta_entrada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Filmes\Lista"

# Chama a função para processar a lista
processar_lista({tipo}, pasta_entrada, pasta_saida)

# Pergunta se o usuário deseja selecionar aleatoriamente filmes da lista de favoritos
deseja_selecionar = input("Deseja selecionar aleatoriamente filmes da lista de favoritos? (sim/não) ").strip().lower()
if deseja_selecionar in {'sim', 's', 'yes', 'y'}:
    selecionar_favoritos_aleatoriamente(tipo, pasta_saida)

print("Programa finalizado.")
