import os
import json
from tqdm import tqdm

def limpar_pasta(pasta_saida):
    # Limpa a pasta de saída antes de iniciar o processo
    for arquivo in os.listdir(pasta_saida):
        caminho_arquivo = os.path.join(pasta_saida, arquivo)
        try:
            if os.path.isfile(caminho_arquivo) or os.path.islink(caminho_arquivo):
                os.unlink(caminho_arquivo)
            elif os.path.isdir(caminho_arquivo):
                os.rmdir(caminho_arquivo)
        except Exception as e:
            print(f'Falha ao deletar {caminho_arquivo}. Motivo: {e}')

def criar_estrutura_item(id_ou_detalhes, preco_padrao=999):
    # Verifica se o input contém mais detalhes ou é apenas o ID
    if "," in id_ou_detalhes and id_ou_detalhes.count(",") == 5:
        detalhes = id_ou_detalhes.split(",")
        id_item = detalhes[0].strip()
        max_price_threshold = int(detalhes[4].strip())
        min_price_threshold = int(detalhes[4].strip())
    else:
        # Caso seja apenas o ID, usa o preço padrão fornecido
        id_item = id_ou_detalhes.strip()
        max_price_threshold = preco_padrao
        min_price_threshold = preco_padrao

    # Cria a estrutura com o ID processado
    return {
        "ClassName": id_item,
        "MaxPriceThreshold": max_price_threshold,
        "MinPriceThreshold": min_price_threshold,
        "SellPricePercent": -1.0,
        "MaxStockThreshold": 1,
        "MinStockThreshold": 1,
        "QuantityPercent": -1,
        "SpawnAttachments": [],
        "Variants": []
    }

def extrair_ids_e_criar_estrutura(pasta_entrada, pasta_saida, preco_padrao):
    # Limpa a pasta de saída
    limpar_pasta(pasta_saida)

    # Estrutura base para o JSON
    estrutura_completa = {
        "m_Version": 12,
        "DisplayName": "Itens Exemplo",
        "Icon": "Deliver",
        "Color": "FBFCFEFF",
        "IsExchange": 0,
        "MaxStockThreshold": 19.0,
        "Items": []
    }

    # Percorre todos os arquivos na pasta de entrada
    for root, dirs, files in os.walk(pasta_entrada):
        for arquivo in tqdm(files, desc="Processando arquivos", unit="arquivo"):
            if arquivo.endswith('.txt'):
                caminho_arquivo = os.path.join(root, arquivo)
                
                # Lê o conteúdo do arquivo e extrai os IDs
                with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                    ids = file.read().splitlines()
                    for id_item in ids:
                        item_formatado = criar_estrutura_item(id_item, preco_padrao)
                        estrutura_completa["Items"].append(item_formatado)

    # Caminho do arquivo de saída
    caminho_saida = os.path.join(pasta_saida, 'estrutura_final.json')
    
    # Salva a estrutura JSON no arquivo de saída
    with open(caminho_saida, 'w', encoding='utf-8') as file_saida:
        json.dump(estrutura_completa, file_saida, indent=4, ensure_ascii=False)

    print(f'Estrutura JSON criada e salva em {caminho_saida}')

# Define os caminhos das pastas
pasta_entrada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Novo Trader\Entrada"
pasta_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Novo Trader\Saida"

# Define o preço máximo e mínimo para os itens
preco_padrao = int(input("Digite o preço máximo e mínimo para todos os itens que não têm detalhes: "))

# Chama a função para extrair os IDs e criar a estrutura JSON
extrair_ids_e_criar_estrutura(pasta_entrada, pasta_saida, preco_padrao)
