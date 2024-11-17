import time

def enviar_alerta(mensagem):
    """
    Função que exibe uma mensagem de alerta no console.
    
    Parâmetros:
    mensagem (str): A mensagem a ser exibida.
    """
    print(f"ALERTA: {mensagem}")

if __name__ == "__main__":
    contador = 0  # Contador para rastrear o número de vezes que o alerta foi exibido

    while contador < 5:  # O loop será executado enquanto o contador for menor que 5
        enviar_alerta("Este é um alerta básico.")
        contador += 1  # Incrementa o contador
        time.sleep(10)  # Pausa de 10 segundos antes de enviar outro alerta

    print("O programa foi finalizado após 5 alertas.")
