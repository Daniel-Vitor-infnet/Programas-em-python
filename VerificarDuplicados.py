from collections import Counter

def verificar_ids_duplicados(caminho_arquivo):
    # Inicializa um contador para contar as ocorrências de cada ID
    contador_ids = Counter()

    # Lê o conteúdo do arquivo e conta as ocorrências dos IDs
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        ids = file.read().splitlines()
        contador_ids.update(ids)

    # Identifica os IDs duplicados
    duplicados = [item for item, count in contador_ids.items() if count > 1]

    if duplicados:
        print("IDs duplicados encontrados:")
        for id_item in duplicados:
            print(f'{id_item}: {contador_ids[id_item]} vezes')
    else:
        print("Nenhum ID duplicado encontrado.")

# Exemplo de uso:
caminho = input("Digite o caminho do arquivo txt: ")
verificar_ids_duplicados(caminho)
