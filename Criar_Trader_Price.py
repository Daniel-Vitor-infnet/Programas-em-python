import os
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

def formatar_ids(conteudo, preco_compra, preco_venda):
    """Formata os IDs conforme a especificação e retorna a lista formatada."""
    linhas = conteudo.strip().splitlines()
    linhas_formatadas = []
    for linha in linhas:
        linhas_formatadas.append(f'"{linha},1,-1,0,{preco_compra},{preco_venda}"')
    return linhas_formatadas

def processar_arquivos(caminho_entrada, caminho_saida, preco_compra, preco_venda):
    """Processa os arquivos na pasta de entrada e salva os IDs formatados na pasta de saída."""
    for root, dirs, files in os.walk(caminho_entrada):
        for file in files:
            caminho_arquivo = os.path.join(root, file)
            with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo:
                conteudo = arquivo.read()
                ids_formatados = formatar_ids(conteudo, preco_compra, preco_venda)

                # Define o caminho do arquivo de saída
                caminho_saida_txt = os.path.join(caminho_saida, f"trader_{file}")
                
                # Salva os IDs formatados no arquivo de saída
                with open(caminho_saida_txt, 'w', encoding='utf-8') as arquivo_saida:
                    for id_formatado in ids_formatados[:-1]:  # Todos menos o último
                        arquivo_saida.write(f"{id_formatado},\n")
                    arquivo_saida.write(f"{ids_formatados[-1]}")  # Último item sem a vírgula final

def main():
    caminho_entrada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Criar Trader Price\Entrada"
    caminho_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Criar Trader Price\Saida"

    # Pergunta os valores de preço de compra e de venda
    preco_compra = input("Informe o preço de compra: ").strip()
    preco_venda = input("Informe o preço de venda: ").strip()

    # Limpa a pasta de saída antes de salvar os novos IDs
    limpar_pasta_saida(caminho_saida)

    # Processa os arquivos na pasta de entrada e salva os IDs formatados na pasta de saída
    processar_arquivos(caminho_entrada, caminho_saida, preco_compra, preco_venda)

    print("Processamento concluído. IDs formatados e salvos na pasta de saída.")

if __name__ == "__main__":
    main()
