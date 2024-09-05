import os
from tqdm import tqdm


def verificar_erros_em_logs(pasta_entrada, pasta_saida):
    # Verifica se a pasta de saída existe; caso contrário, cria a pasta.
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Lista todos os arquivos na pasta de entrada
    arquivos = [f for f in os.listdir(pasta_entrada) if f.endswith(
        ('.RPT', '.txt', '.log', '.mdmp', '.DAM'))]

    # Inicializa a barra de progresso
    for arquivo in tqdm(arquivos, desc="Verificando logs", unit="arquivo"):
        caminho_entrada = os.path.join(pasta_entrada, arquivo)
        caminho_saida = os.path.join(
            pasta_saida, f"{os.path.splitext(arquivo)[0]}.txt")

        erros_encontrados = []

        # Lê o conteúdo do arquivo
        with open(caminho_entrada, 'r', encoding='utf-8', errors='ignore') as file:
            linhas = file.readlines()

        # Verifica cada linha em busca de padrões de erros comuns
        for linha in linhas:
            if any(erro in linha.lower() for erro in ["error", "failed", "exception", "crash", "warning"]):
                erros_encontrados.append(linha.strip())

        # Escreve o resultado no arquivo de saída
        with open(caminho_saida, 'w', encoding='utf-8') as file:
            if erros_encontrados:
                file.write("\n".join(erros_encontrados))
            else:
                file.write("Sem erros aqui 🥳🥳")


# Define os caminhos das pastas
pasta_entrada = r"G:\Outros computadores\Meu computador (1)\Backup (Pc)\Dayz\Python\Verificar Logs\Entrada"
pasta_saida = r"G:\Outros computadores\Meu computador (1)\Backup (Pc)\Dayz\Python\Verificar Logs\Saida"

# Chama a função para verificar os logs
verificar_erros_em_logs(pasta_entrada, pasta_saida)
