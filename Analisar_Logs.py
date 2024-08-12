import os
import re
from tqdm import tqdm

def verificar_erros_ou_incompatibilidades(pasta_entrada, pasta_saida):
    # Verifica se a pasta de entrada e saída existem; caso contrário, cria as pastas.
    if not os.path.exists(pasta_entrada):
        os.makedirs(pasta_entrada)
        
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Extensões permitidas
    extensoes_permitidas = ['.RPT', '.txt', '.log', '.mdmp', '.DAM']

    # Lista todos os arquivos na pasta de entrada com as extensões permitidas
    arquivos = [f for f in os.listdir(pasta_entrada) if os.path.splitext(f)[1] in extensoes_permitidas]

    # Inicializa a barra de progresso
    for arquivo in tqdm(arquivos, desc="Analisando arquivos", unit="arquivo"):
        caminho_entrada = os.path.join(pasta_entrada, arquivo)
        caminho_saida = os.path.join(pasta_saida, os.path.splitext(arquivo)[0] + ".txt")

        # Lê o conteúdo do arquivo
        with open(caminho_entrada, 'r', encoding='utf-8', errors='ignore') as file:
            linhas = file.readlines()

        # Verifica erros ou incompatibilidades
        erros_encontrados = []
        for linha in linhas:
            # Aqui você pode adicionar padrões de erro que deseja buscar
            if re.search(r'error|fail|exception|crash|incompatible|warning', linha, re.IGNORECASE):
                erros_encontrados.append(linha.strip())

        # Se encontrou erros, escreve no arquivo de saída
        if erros_encontrados:
            with open(caminho_saida, 'w', encoding='utf-8') as file:
                file.write("\n".join(erros_encontrados))
        else:
            # Se não encontrou erros, escreve a mensagem padrão
            with open(caminho_saida, 'w', encoding='utf-8') as file:
                file.write("Sem erros aqui 🥳🥳")

# Obtém o caminho do diretório onde o executável está sendo executado
caminho_base = os.path.dirname(os.path.abspath(__file__))

# Define as pastas de entrada e saída com base no diretório do executável
pasta_entrada = os.path.join(caminho_base, "Entrada")
pasta_saida = os.path.join(caminho_base, "Saida")

# Chama a função para verificar os arquivos de log
verificar_erros_ou_incompatibilidades(pasta_entrada, pasta_saida)
