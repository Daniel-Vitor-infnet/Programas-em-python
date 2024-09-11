import os
import re
import shutil

def extrair_ids_da_pasta(pasta_ids):
    ids_encontrados = set()
    for root, dirs, files in os.walk(pasta_ids):
        for arquivo in files:
            if arquivo.endswith('.txt'):
                caminho_arquivo = os.path.join(root, arquivo)
                with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                    ids = file.read().splitlines()
                    ids_encontrados.update(ids)
    return ids_encontrados

def criar_backup(caminho_arquivo, pasta_backup):
    if not os.path.exists(pasta_backup):
        os.makedirs(pasta_backup)
    caminho_backup = os.path.join(pasta_backup, os.path.basename(caminho_arquivo))
    shutil.copy2(caminho_arquivo, caminho_backup)

def editar_arquivo_xml(caminho_arquivo, ids, health_min, health_max, pasta_backup):
    criar_backup(caminho_arquivo, pasta_backup)
    
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()

    def adicionar_health(match):
        type_block = match.group(0)
        if '<healthMin>' not in type_block and '<healthMax>' not in type_block:
            # Adiciona as tags antes do fechamento da tag </type>, sem alterar a estrutura existente
            type_block = re.sub(r'\s*</type>', f"\n        <healthMin>{health_min}</healthMin>\n        <healthMax>{health_max}</healthMax>\n    </type>", type_block)
        return type_block

    padrao = re.compile(r'<type name="([^"]+)">.*?</type>', re.DOTALL)
    novo_conteudo = padrao.sub(lambda m: adicionar_health(m) if m.group(1) in ids else m.group(0), conteudo)

    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(novo_conteudo)

# Caminho da pasta de IDs
pasta_ids = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Extrair Trader2\Saida"

# Solicita o caminho do arquivo XML
caminho_xml = input("Digite o caminho completo do arquivo XML: ").strip()

# Solicita o caminho da pasta de backup
pasta_backup = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Editar Vida\Backup"

# Solicita os valores de healthMin e healthMax
health_min = input("Digite o valor de healthMin (ex: 0.5): ").strip()
health_max = input("Digite o valor de healthMax (ex: 1.0): ").strip()

# Extrai os IDs da pasta
ids = extrair_ids_da_pasta(pasta_ids)

# Edita o arquivo XML e cria o backup
editar_arquivo_xml(caminho_xml, ids, health_min, health_max, pasta_backup)

print("Processo concluído. O backup foi criado e o arquivo editado.")
