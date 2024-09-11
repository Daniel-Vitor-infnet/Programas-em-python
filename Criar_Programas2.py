import os
import subprocess
from pathlib import Path

# Pegar os diretórios.
caminho_Correto = Path.cwd()
pasta_Codigos = caminho_Correto.joinpath("Codigos")
pasta_Programas = caminho_Correto.joinpath("Programas")
pasta_Build = caminho_Correto.joinpath("build")
pasta_Spec = caminho_Correto.joinpath("Spec")

# Lista com todas as pastas.
pastas = [pasta_Codigos, pasta_Programas, pasta_Build, pasta_Spec]

# Função para verificar e criar pastas se necessário
def verificar_e_criar_pastas(pastas):
    for pasta in pastas:
        if not pasta.exists():
            pasta.mkdir(parents=True)  # Cria a pasta e os diretórios pais, se necessário
            print(f"Pasta '{pasta}' criada.")
        else:
            print(f"Pasta '{pasta}' já existe.")

# Função para criar o executável usando pyinstaller
def criar_executavel(programaNome):
    # Caminho completo do arquivo Python que será convertido em exe
    script_path = pasta_Codigos.joinpath(programaNome)
    
    if not script_path.exists():
        print(f"O arquivo {programaNome} não foi encontrado em {pasta_Codigos}.")
        return
    
    # Comando do PyInstaller com os parâmetros necessários
    comando = [
        "pyinstaller",
        "--onefile",  # Cria um único arquivo .exe
        "--distpath", str(pasta_Programas),  # Salva o executável em pasta_Programas
        "--workpath", str(pasta_Build),  # Usa pasta_Build como diretório de compilação
        "--specpath", str(pasta_Spec),  # Salva o .spec na pasta_Spec
        str(script_path)  # Caminho do script Python
    ]
    
    # Executa o comando do PyInstaller
    try:
        subprocess.run(comando, check=True)
        print(f"Arquivo executável criado com sucesso em {pasta_Programas}.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao criar o arquivo executável: {e}")

if __name__ == "__main__":
    # Verificar e criar pastas necessárias
    verificar_e_criar_pastas(pastas)

    # Nome do programa a ser convertido
    programaNome = "teste.py"

    # Criar o executável
    criar_executavel(programaNome)

    input("Aperte qualquer tecla para sair")
