from tqdm import tqdm

# Solicita os caminhos dos arquivos de lista 1 e lista 2
caminho_lista_1 = input("Digite o caminho da Lista 1 entre aspas (exemplo: \"C:\\bataat\\teste.txt\"): ").strip('"')
caminho_lista_2 = input("Digite o caminho da Lista 2 entre aspas (exemplo: \"C:\\bataat\\teste.txt\"): ").strip('"')

# Solicita o nome do arquivo de saída
nome_arquivo_saida = input("Digite o nome do arquivo de saída (sem extensão): ")

# Define o caminho de saída
caminho_saida = fr"G:\Outros computadores\Meu computador (1)\Backup (Pc)\Dayz\Python\Comparar listas\Resultados\{nome_arquivo_saida}.txt"

# Abra os arquivos e leia as linhas
with open(caminho_lista_1, 'r') as file1:
    lista_1 = set(file1.read().splitlines())

with open(caminho_lista_2, 'r') as file2:
    lista_2 = set(file2.read().splitlines())

# Preparar a barra de progresso
total_items = len(lista_2)
diferencas_completas = []
diferencas_simples = []

print("Comparando as listas...")

def comparar_strings(str1, str2):
    diferencas = []
    for i in range(max(len(str1), len(str2))):
        if i < len(str1) and i < len(str2):
            if str1[i] != str2[i]:
                diferencas.append(f'Posição {i+1}: "{str1[i]}" em lista 1 vs "{str2[i]}" em lista 2')
        elif i < len(str1):
            diferencas.append(f'Posição {i+1}: "{str1[i]}" em lista 1, faltando em lista 2')
        elif i < len(str2):
            diferencas.append(f'Posição {i+1}: "{str2[i]}" em lista 2, faltando em lista 1')
    return diferencas

for item2 in tqdm(lista_2, total=total_items, unit="item"):
    if item2 not in lista_1:
        similar_encontrado = False
        for item1 in lista_1:
            # Verifica similaridade baseando-se em diferenças de maiúsculas/minúsculas e pequenas diferenças de letras.
            if item2.lower() == item1.lower() or (len(item2) == len(item1) and sum(c1 != c2 for c1, c2 in zip(item2, item1)) <= 2):
                diferencas = comparar_strings(item1, item2)
                if diferencas:
                    diferencas_completas.append(f'{item2} ////// Diferença encontrada: {"; ".join(diferencas)}')
                similar_encontrado = True
                break
        if not similar_encontrado:
            diferencas_simples.append(item2)
            diferencas_completas.append(item2)

# Pergunta se deve mostrar todas as diferenças ou apenas as que realmente faltam
mostrar_diferencas = input("Deseja mostrar as diferenças de letras e maiúsculas/minúsculas? (S/N): ").strip().upper()

# Ordena os resultados em ordem alfabética
diferencas_completas.sort()
diferencas_simples.sort()

# Salvar os resultados no arquivo de saída
with open(caminho_saida, 'w') as output_file:
    if mostrar_diferencas == 'S':
        for item in diferencas_completas:
            output_file.write(item + "\n")
    else:
        for item in diferencas_simples:
            output_file.write(item + "\n")

print(f"Os itens faltando foram salvos em: {caminho_saida}")
