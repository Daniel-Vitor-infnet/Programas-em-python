import os
import re
import shutil

def limpar_pasta_saida(caminho_saida):
    """Limpa todos os arquivos na pasta de saída."""
    for arquivo in os.listdir(caminho_saida):
        caminho_arquivo = os.path.join(caminho_saida, arquivo)
        try:
            if os.path.isfile(caminho_arquivo):
                os.unlink(caminho_arquivo)
            elif os.path.isdir(caminho_arquivo):
                shutil.rmtree(caminho_arquivo)
        except Exception as e:
            print(f"Erro ao limpar arquivo {caminho_arquivo}: {e}")

def extrair_classes(conteudo):
    """Extrai todas as classes do conteúdo."""
    return re.findall(r'class\s+(\S+):\s+\S+', conteudo)

def processar_arquivos(caminho_entrada, caminho_saida):
    """Processa os arquivos na pasta de entrada e salva as classes na pasta de saída."""
    classes_extraidas = []

    for root, dirs, files in os.walk(caminho_entrada):
        for file in files:
            caminho_arquivo = os.path.join(root, file)
            with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo:
                conteudo = arquivo.read()
                classes_extraidas.extend(extrair_classes(conteudo))

    # Salva as classes extraídas na pasta de saída
    caminho_saida_txt = os.path.join(caminho_saida, "classes_extraidas.txt")
    with open(caminho_saida_txt, 'w', encoding='utf-8') as arquivo_saida:
        for classe in classes_extraidas:
            arquivo_saida.write(f"{classe}\n")

def main():
    caminho_entrada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Extrair Class\Entrada"
    caminho_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Extrair Class\Saida"

    # Limpa a pasta de saída antes de salvar as novas classes
    limpar_pasta_saida(caminho_saida)

    # Processa os arquivos na pasta de entrada e salva as classes na pasta de saída
    processar_arquivos(caminho_entrada, caminho_saida)

    print("Processamento concluído. Classes extraídas e salvas na pasta de saída.")

if __name__ == "__main__":
    main()
