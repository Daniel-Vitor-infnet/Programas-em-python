import os
from tqdm import tqdm

def verificar_erros_em_logs(pasta_entrada, pasta_saida):
    # Verifica se a pasta de saída existe; caso contrário, cria a pasta.
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Lista todos os arquivos na pasta de entrada
    arquivos = [f for f in os.listdir(pasta_entrada) if f.endswith(
        ('.RPT', '.txt', '.log', '.mdmp', '.DAM'))]

    total_erros = 0  # Variável para contar o total de erros encontrados

    # Inicializa a barra de progresso
    for arquivo in tqdm(arquivos, desc="Verificando logs", unit="arquivo"):
        caminho_entrada = os.path.join(pasta_entrada, arquivo)
        caminho_saida = os.path.join(
            pasta_saida, f"{os.path.splitext(arquivo)[0]}.txt")

        erros_encontrados = []
        capturando_bloco = False
        bloco_erro = []

        # Lê o conteúdo do arquivo linha por linha
        with open(caminho_entrada, 'r', encoding='utf-8', errors='ignore') as file:
            for linha in file:
                # Se encontrar um erro ou "item", inicia a captura do bloco
                if any(erro in linha.lower() for erro in ["error", "failed", "exception", "crash", "warning", "item"]):
                    capturando_bloco = True
                    bloco_erro.append(linha.strip())
                # Se já está capturando um bloco de erro, continue adicionando as linhas até encontrar uma separação
                elif capturando_bloco:
                    bloco_erro.append(linha.strip())
                    # Se encontrar uma linha em branco ou separadora, para de capturar o bloco
                    if linha.strip() == "" or linha.startswith("------------------------------------"):
                        capturando_bloco = False
                        bloco_erro.append("------------------------------------")  # Adiciona a separação
                        erros_encontrados.append("\n".join(bloco_erro))
                        bloco_erro = []

        total_erros += len(erros_encontrados)  # Atualiza o contador de erros

        # Escreve o resultado no arquivo de saída
        with open(caminho_saida, 'w', encoding='utf-8') as file:
            if erros_encontrados:
                file.write("\n\n".join(erros_encontrados))
            else:
                file.write("Sem erros aqui 🥳🥳")

    # Imprime o resumo final
    print(f"\nVerificação concluída! Um total de {total_erros} blocos de erros foram encontrados.")

# Define os caminhos das pastas
pasta_entrada = r"G:\Outros computadores\Meu computador (1)\Backup (Pc)\Dayz\Python\Verificar Logs\Entrada"
pasta_saida = r"G:\Outros computadores\Meu computador (1)\Backup (Pc)\Dayz\Python\Verificar Logs\Saida"

# Chama a função para verificar os logs
verificar_erros_em_logs(pasta_entrada, pasta_saida)
