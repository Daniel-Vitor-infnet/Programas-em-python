import os
import xml.etree.ElementTree as ET
from tqdm import tqdm

# Solicita ao usuário se deseja processar uma pasta ou um arquivo específico
opcao = input("Você deseja processar uma 'pasta' ou um 'caminho' específico de arquivo? (digite 'pasta' ou 'caminho'): ").strip().lower()

# Inicializa a lista para armazenar os arquivos a serem processados
arquivos_xml = []

if opcao == "pasta":
    # Caminho padrão para a pasta
    pasta_entrada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Extrair Types\Types"
    
    # Verifica se a pasta de entrada existe
    if not os.path.exists(pasta_entrada):
        print("A pasta de entrada não existe!")
        exit()
    
    # Lista todos os arquivos .xml na pasta de entrada
    arquivos_xml = [f for f in os.listdir(pasta_entrada) if f.endswith('.xml')]

elif opcao == "caminho":
    # Solicita o caminho completo do arquivo XML
    caminho_arquivo = input("Digite o caminho completo do arquivo XML (exemplo: \"C:/batata/Teste.xml\"): ").strip('"')
    
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_arquivo) or not caminho_arquivo.endswith('.xml'):
        print("O arquivo especificado não existe ou não é um arquivo XML!")
        exit()
    
    # Adiciona o arquivo à lista
    arquivos_xml.append(os.path.basename(caminho_arquivo))
    pasta_entrada = os.path.dirname(caminho_arquivo)

else:
    print("Opção inválida! Por favor, digite 'pasta' ou 'caminho'.")
    exit()

# Verifica se há arquivos .xml para processar
if not arquivos_xml:
    print("Nenhum arquivo .xml foi encontrado!")
    exit()

# Solicita o nome do arquivo de saída
nome_arquivo_saida = input("Digite o nome do arquivo de saída (sem extensão): ")
caminho_saida = os.path.join(r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Extrair Types\Resultado", f"{nome_arquivo_saida}.txt")

# Inicializa a lista para armazenar os IDs extraídos
ids_extraidos = []

# Processa os arquivos XML
print("Analisando arquivos...")

for arquivo in tqdm(arquivos_xml, total=len(arquivos_xml), unit="arquivo"):
    caminho_arquivo_completo = os.path.join(pasta_entrada, arquivo)
    try:
        tree = ET.parse(caminho_arquivo_completo)
        root = tree.getroot()
        for type_tag in root.findall('.//type'):
            item_name = type_tag.get('name')
            if item_name:
                ids_extraidos.append(item_name)
    except ET.ParseError:
        print(f"Erro ao analisar o arquivo: {arquivo}")

# Salva os IDs extraídos no arquivo de saída
with open(caminho_saida, 'w') as output_file:
    for item in ids_extraidos:
        output_file.write(item + "\n")

print(f"Extração concluída! Os itens foram salvos em: {caminho_saida}")
