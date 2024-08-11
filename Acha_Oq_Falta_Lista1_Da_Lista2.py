from tqdm import tqdm

# Solicita os caminhos dos arquivos de lista 1 e lista 2
caminho_lista_1 = input("Digite o caminho da Lista 1 entre aspas (exemplo: \"C:\\bataat\\teste.txt\"): ").strip('"')
caminho_lista_2 = input("Digite o caminho da Lista 2 entre aspas (exemplo: \"C:\\bataat\\teste.txt\"): ").strip('"')

# Solicita o nome do arquivo de saída
nome_arquivo_saida = input("Digite o nome do arquivo de saída (sem extensão): ")

# Define o caminho de saída
caminho_saida = fr"C:\Users\Administrador\Desktop\Backup (Pc)\Programas em python\Resultados_TXT\{nome_arquivo_saida}.txt"

# Abra os arquivos e leia as linhas
with open(caminho_lista_1, 'r') as file1:
    lista_1 = set(file1.read().splitlines())

with open(caminho_lista_2, 'r') as file2:
    lista_2 = set(file2.read().splitlines())

# Preparar a barra de progresso
total_items = len(lista_2)
diff_trader_not_in_types = []

print("Comparando as listas...")
for item in tqdm(lista_2, total=total_items, unit="item"):
    if item not in lista_1:
        diff_trader_not_in_types.append(item)

# Salvar os resultados no arquivo de saída
with open(caminho_saida, 'w') as output_file:
    for item in diff_trader_not_in_types:
        output_file.write(item + "\n")

print(f"Os itens faltando foram salvos em: {caminho_saida}")
