import json
import os
from tqdm import tqdm

# Solicita o caminho do arquivo JSON
caminho_arquivo = input("Digite o caminho completo do arquivo JSON (exemplo: \"C:/batata/teste.json\"): ").strip('"')

# Verifica se o arquivo existe
if not os.path.exists(caminho_arquivo) or not caminho_arquivo.endswith('.json'):
    print("O arquivo especificado não existe ou não é um arquivo JSON!")
    exit()

# Solicita o nome das categorias (uma ou mais, separadas por espaço entre aspas)
categorias = input('Digite o nome das categorias que você deseja extrair (exemplo: "Peixaria" "Padaria"): ').strip().split('" "')
categorias = [categoria.strip('"') for categoria in categorias]

# Pergunta se o usuário quer apenas "id" ou "tudo"
modo = input("Você deseja extrair apenas 'id' ou 'tudo'? ").strip().lower()

# Define o caminho da pasta de saída
pasta_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Extrair Trader\Resultados"

# Define o nome do arquivo de saída baseado no número de categorias
if len(categorias) == 1:
    nome_arquivo_saida = categorias[0]
else:
    nome_arquivo_saida = "_".join(categorias[:3])

caminho_saida = os.path.join(pasta_saida, f"{nome_arquivo_saida}.txt")

# Carrega o arquivo JSON
with open(caminho_arquivo, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Inicializa a lista para armazenar os resultados
resultados = []

# Acessa a lista de categorias no JSON
trader_categories = data.get("TraderCategories", [])

# Verifica as categorias e extrai os dados
print("Analisando categorias...")

if 'tudo' in [categoria.lower() for categoria in categorias]:
    categorias_encontradas = trader_categories
else:
    categorias_encontradas = [cat for cat in trader_categories if cat['CategoryName'].lower() in [c.lower() for c in categorias]]

# Verifica se encontrou alguma categoria
if not categorias_encontradas:
    print("Nenhuma das categorias especificadas foi encontrada!")
    exit()

# Processa cada categoria encontrada
for categoria_dados in tqdm(categorias_encontradas, total=len(categorias_encontradas), unit="categoria"):
    nome_categoria = categoria_dados['CategoryName']
    produtos = categoria_dados['Products']

    if modo == "id":
        for produto in produtos:
            produto_id = produto.split(',')[0]
            resultados.append(produto_id)
    
    elif modo == "tudo":
        resultados.append(f"===== Categoria: {nome_categoria} =====")
        for produto in produtos:
            produto_id = produto.split(',')[0]
            resultados.append(produto_id)
        resultados.append("\n")

# Salva os resultados no arquivo de saída, substituindo se já existir
with open(caminho_saida, 'w', encoding='utf-8') as output_file:
    for item in resultados:
        output_file.write(item + "\n")

print(f"Extração concluída! Os resultados foram salvos em: {caminho_saida}")
