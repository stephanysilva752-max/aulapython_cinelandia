'''Desenvolva um código python que leia um valor e verifica se é positivo. negativo ou 0'''

valor=float(input("Digite um valor"))
if (valor > 0 ):
    print(f"{valor} é um número postivo")
elif (valor < 0):
    print(f"{valor} é um número negativo")
else:
    print(f"Esse número é 0")