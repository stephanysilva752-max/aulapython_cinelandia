''' Leia duas notas, calcule a média e trate o erro de entrada (valor invalido ou divisão incorreta) '''

def calcular_media():
    try:
        num1=float(input("Digite um número ")) 
        num2=float(input("Digite outro número "))
        media = (num1 + num2) /2
    except ValueError:
        print("Erro: Digite apenas números válidos!")
    else:
        print(f"Média calculada: {media:.2f}")
    finally:
        print("Fim do cálculo de média.")

calcular_media()