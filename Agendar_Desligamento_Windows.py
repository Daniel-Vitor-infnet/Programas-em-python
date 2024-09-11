import os
import sys
import threading
from time import sleep
from re import compile
from tqdm import tqdm  # Barra de progresso mais sofisticada

# Função para exibir tabela de formato aceito
def mostrar_tabela():
    tabela = """
    Bem-vindo ao programa de agendamento de desligamento do computador!
    Utilize os seguintes formatos para agendar o desligamento:

    | Formato      | Descrição                                      |
    |--------------|------------------------------------------------|
    | h01          | Horas (de 1 até 24 horas)                      |
    | m01          | Minutos (de 1 até 59 minutos)                  |
    | s01          | Segundos (de 1 até 59 segundos)                |
    | 01:05:06     | Horas:Minutos:Segundos (máximo 24:59:59)       |
    | 05:50        | Minutos:Segundos (máximo 59:59)                |
    
    Digite "Sair", "exit", "stop", "parar" ou "finalizar" para cancelar e fechar o programa.
    """
    print(tabela)

# Função para validar a entrada de tempo
def validar_entrada(tempo):
    # Expressões regulares para validar entradas
    regex_h = compile(r'^[hH]\d{2}$')
    regex_m = compile(r'^[mM]\d{2}$')
    regex_s = compile(r'^[sS]\d{2}$')
    regex_hms = compile(r'^\d{2}:\d{2}:\d{2}$')
    regex_ms = compile(r'^\d{2}:\d{2}$')

    if regex_h.match(tempo):  # Verifica formato de horas
        horas = int(tempo[1:])
        if 1 <= horas <= 24:
            return horas * 3600
        else:
            raise ValueError("Erro: Horas devem estar entre 1 e 24.")

    elif regex_m.match(tempo):  # Verifica formato de minutos
        minutos = int(tempo[1:])
        if 1 <= minutos <= 59:
            return minutos * 60
        else:
            raise ValueError("Erro: Minutos devem estar entre 1 e 59.")

    elif regex_s.match(tempo):  # Verifica formato de segundos
        segundos = int(tempo[1:])
        if 1 <= segundos <= 59:
            return segundos
        else:
            raise ValueError("Erro: Segundos devem estar entre 1 e 59.")

    elif regex_hms.match(tempo):  # Verifica formato hh:mm:ss
        horas, minutos, segundos = map(int, tempo.split(':'))
        if 0 <= horas <= 24 and 0 <= minutos <= 59 and 0 <= segundos <= 59:
            return horas * 3600 + minutos * 60 + segundos
        else:
            raise ValueError("Erro: Horas, minutos ou segundos fora do limite.")

    elif regex_ms.match(tempo):  # Verifica formato mm:ss
        minutos, segundos = map(int, tempo.split(':'))
        if 0 <= minutos <= 59 and 0 <= segundos <= 59:
            return minutos * 60 + segundos
        else:
            raise ValueError("Erro: Minutos ou segundos fora do limite.")

    else:
        raise ValueError("Erro: Formato inválido. Verifique a tabela e tente novamente.")

# Função para cancelar agendamento de desligamento
def cancelar_agendamento():
    if os.name == 'nt':  # Windows
        os.system('shutdown /a')
    elif os.name == 'posix':  # Linux/Unix
        os.system('shutdown -c')

# Função para agendar o desligamento
def agendar_desligamento(segundos):
    if os.name == 'nt':  # Windows
        os.system(f'shutdown /s /t {segundos}')
    elif os.name == 'posix':  # Linux/Unix
        os.system(f'sudo shutdown -h +{segundos // 60}')

# Função para exibir a barra de progresso usando tqdm
def barra_progresso(segundos):
    for _ in tqdm(range(segundos), desc="Tempo restante", ncols=100, unit="s", colour="blue"):
        sleep(1)
    print("\nDesligando...")

# Função principal para interagir com o usuário
def iniciar_programa():
    mostrar_tabela()
    agendamento_ativo = False
    tempo_em_segundos = 0

    while True:
        entrada = input("\nDigite o tempo para desligamento ou um comando: ").strip().lower()

        if entrada in ["sair", "exit", "stop", "parar", "finalizar"]:
            if agendamento_ativo:
                cancelar_agendamento()
            print("Programa finalizado.")
            break

        try:
            # Validação e conversão do tempo
            tempo_em_segundos = validar_entrada(entrada)

            # Se houver agendamento ativo, cancelar
            if agendamento_ativo:
                cancelar_agendamento()

            # Agendar o novo tempo
            agendar_desligamento(tempo_em_segundos)
            agendamento_ativo = True
            print(f"Desligamento agendado para {entrada}.")
            
            # Iniciar barra de progresso em uma thread separada
            t = threading.Thread(target=barra_progresso, args=(tempo_em_segundos,))
            t.start()
            t.join()

        except ValueError as e:
            print(e)

# Iniciar o programa
if __name__ == "__main__":
    iniciar_programa()
