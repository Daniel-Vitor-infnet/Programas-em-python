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



if __name__ == "__main__":
    verificar_e_criar_pastas(pastas)

input("Aperta qualquer tecla1")
