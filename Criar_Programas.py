import os
import time
import subprocess
import re

# 1. Obter o diretório atual
caminhoInicial = os.getcwd()
caminhoInicial2 = os.getcwd()

# 2. Verificar se há arquivos .py na pasta "Codigos"
pasta_codigos = os.path.join(caminhoInicial, "Codigos")
if os.path.exists(pasta_codigos):
    arquivos_py = [f for f in os.listdir(pasta_codigos) if f.endswith(".py")]
    if not arquivos_py:
        print("Não existem programas Python na pasta 'Codigos'. O programa será encerrado em 300 segundos.")
        time.sleep(300)
        exit()
    else:
        print("Programas encontrados:")
        for idx, arquivo in enumerate(arquivos_py, 1):
            print(f"{idx}. {arquivo}")
        # Escolha do programa
        escolha = int(input("Digite o número do programa que deseja compilar: "))
        arquivo_escolhido = arquivos_py[escolha - 1]
else:
    print(pasta_codigos + " A pasta 'Codigos' não existe.")
    time.sleep(300)
    exit()

# 3. Substituir a variável 'caminhoPadrao' por 'caminhoInicial' usando expressão regular
def substituir_caminho_padrao(arquivo, caminho_inicial):
    with open(os.path.join(pasta_codigos, arquivo), 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Usar expressão regular para substituir qualquer valor existente de caminhoPadrao
    conteudo_novo = re.sub(r'caminhoPadrao = r".*"', f'caminhoPadrao = r"{caminho_inicial}"', conteudo)

    with open(os.path.join(pasta_codigos, arquivo), 'w', encoding='utf-8') as f:
        f.write(conteudo_novo)

substituir_caminho_padrao(arquivo_escolhido, caminhoInicial2)

# 4. Caminhos para Spec e Programas
pasta_spec = os.path.join(caminhoInicial, "Spec")
pasta_programas = os.path.join(caminhoInicial, "Programas")
os.makedirs(pasta_spec, exist_ok=True)
os.makedirs(pasta_programas, exist_ok=True)

# 5. Remover traços e sublinhados do nome do executável
nome_exe = arquivo_escolhido.replace("-", " ").replace("_", " ").replace(".py", "")

# Comando PyInstaller
comando_pyinstaller = f'pyinstaller --onefile --name "{nome_exe}" --distpath "{pasta_programas}" --specpath "{pasta_spec}" {os.path.join(pasta_codigos, arquivo_escolhido)}'
print(comando_pyinstaller)
subprocess.run(comando_pyinstaller, shell=True)


# print(f"O executável foi gerado com o nome '{nome_exe}.exe' na pasta '{pasta_programas}'.")