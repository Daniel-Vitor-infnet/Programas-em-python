import os
import re

def editar_tag(conteudo, tag, novo_valor):
    """Edita o valor dentro da tag especificada para o valor informado."""
    padrao = rf'(<{tag}>)(\d+)(</{tag}>)'
    return re.sub(padrao, rf'\g<1>{novo_valor}\g<3>', conteudo)

def processar_arquivos(caminho_entrada, caminho_saida, modificar, valor_nominal=None, valor_min=None):
    """Processa os arquivos na pasta de entrada e salva na pasta de saída."""
    for root, dirs, files in os.walk(caminho_entrada):
        # Cria a estrutura de pastas na pasta de saída
        estrutura_pasta = os.path.relpath(root, caminho_entrada)
        caminho_destino_pasta = os.path.join(caminho_saida, estrutura_pasta)
        os.makedirs(caminho_destino_pasta, exist_ok=True)

        for file in files:
            caminho_arquivo_entrada = os.path.join(root, file)
            caminho_arquivo_saida = os.path.join(caminho_destino_pasta, file)

            with open(caminho_arquivo_entrada, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()

            if "<nominal>" in conteudo or "<min>" in conteudo:
                # Edita o valor conforme a escolha do usuário
                if modificar in {'1', '3'} and "<nominal>" in conteudo:
                    conteudo = editar_tag(conteudo, "nominal", valor_nominal)
                
                if modificar in {'1', '2'} and "<min>" in conteudo:
                    conteudo = editar_tag(conteudo, "min", valor_min)

                # Salva o novo conteúdo na pasta de saída
                with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
                    arquivo_saida.write(conteudo)

def main():
    caminho_entrada = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Spawn\Entrada"
    caminho_saida = r"C:\Users\Administrador\Desktop\Backup (Pc)\Dayz\Python\Spawn\Saida"

    # Pergunta o que o usuário deseja modificar
    print("Deseja modificar:")
    print("1. Todos (nominal e min)")
    print("2. Apenas min")
    print("3. Apenas nominal")
    modificar = input("Digite o número da sua escolha: ").strip()

    valor_nominal, valor_min = None, None

    if modificar in {'1', '3'}:
        # Pergunta o valor que o usuário deseja colocar na tag <nominal>
        valor_nominal = input("Informe o valor que deseja colocar em <nominal>: ").strip()

    if modificar in {'1', '2'}:
        # Pergunta o valor que o usuário deseja colocar na tag <min>
        valor_min = input("Informe o valor que deseja colocar em <min>: ").strip()

    processar_arquivos(caminho_entrada, caminho_saida, modificar, valor_nominal, valor_min)
    print("Processamento concluído. Arquivos salvos na pasta de saída.")

if __name__ == "__main__":
    main()
