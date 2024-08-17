import os
from tqdm import tqdm

def ajustar_flags_em_linha(pasta_entrada, pasta_saida):
    # Verifica se a pasta de saída existe; caso contrário, cria a pasta.
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Percorre todos os arquivos na pasta de entrada, incluindo subpastas
    for root, dirs, files in os.walk(pasta_entrada):
        for arquivo in tqdm(files, desc="Processando arquivos", unit="arquivo"):
            if arquivo.endswith('.xml'):
                caminho_entrada = os.path.join(root, arquivo)
                
                # Cria a estrutura de pastas na saída
                estrutura_relativa = os.path.relpath(root, pasta_entrada)
                caminho_saida_pasta = os.path.join(pasta_saida, estrutura_relativa)
                if not os.path.exists(caminho_saida_pasta):
                    os.makedirs(caminho_saida_pasta)
                
                caminho_saida = os.path.join(caminho_saida_pasta, arquivo)

                # Lê o conteúdo do arquivo
                with open(caminho_entrada, 'r', encoding='utf-8') as file:
                    linhas = file.readlines()

                # Ajusta apenas as tags <flags> para que fiquem em uma linha, mantendo a formatação original
                conteudo_ajustado = []
                i = 0
                while i < len(linhas):
                    linha = linhas[i].rstrip()
                    if linha.strip().startswith("<flags") and not linha.strip().endswith("/>"):
                        espaco_inicial = len(linha) - len(linha.lstrip())
                        linha_completa = linha.strip()
                        i += 1
                        while not linhas[i].strip().endswith("/>"):
                            linha_completa += " " + linhas[i].strip()
                            i += 1
                        linha_completa += " " + linhas[i].strip()
                        conteudo_ajustado.append(" " * espaco_inicial + linha_completa)
                    else:
                        conteudo_ajustado.append(linha)
                    i += 1

                # Escreve o conteúdo ajustado no arquivo de saída
                with open(caminho_saida, 'w', encoding='utf-8') as file:
                    file.write("\n".join(conteudo_ajustado) + "\n")

# Define os caminhos das pastas
pasta_entrada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Ajustar Flags\Entrada"
pasta_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Ajustar Flags\Saida"

# Chama a função para ajustar os arquivos
ajustar_flags_em_linha(pasta_entrada, pasta_saida)
