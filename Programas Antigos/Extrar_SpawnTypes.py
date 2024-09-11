import os
import re
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

def extrair_ids(pasta_entrada, pasta_saida):
    # Limpa a pasta de saída
    limpar_pasta(pasta_saida)

    # Inicializa um set para armazenar IDs únicos
    ids_encontrados = set()

    # Percorre todos os arquivos na pasta de entrada
    for root, dirs, files in os.walk(pasta_entrada):
        for arquivo in tqdm(files, desc="Processando arquivos", unit="arquivo"):
            if arquivo.endswith('.xml'):
                caminho_arquivo = os.path.join(root, arquivo)
                
                # Lê o conteúdo do arquivo
                with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                    conteudo = file.read()
                    
                    # Encontra todos os IDs em <item name="ID" ... />
                    ids_item = re.findall(r'<item\s+name\s*=\s*"([^"]+)"', conteudo)
                    
                    # Adiciona IDs encontrados ao set (evitando duplicados)
                    ids_encontrados.update(ids_item)

    # Caminho do arquivo de saída
    caminho_saida = os.path.join(pasta_saida, 'ids_extraidos.txt')
    
    # Escreve os IDs únicos em um arquivo txt, um por linha
    with open(caminho_saida, 'w', encoding='utf-8') as file_saida:
        for id_item in sorted(ids_encontrados):
            file_saida.write(f'{id_item}\n')

    print(f'IDs extraídos e salvos em {caminho_saida}')

# Define os caminhos das pastas
pasta_entrada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Extrair Spawnabletypes\Entrada"
pasta_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Extrair Spawnabletypes\Saida"

# Chama a função para extrair os IDs e salvar no arquivo de saída
extrair_ids(pasta_entrada, pasta_saida)
