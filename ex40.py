def somar(a, b):
    return a + b 

def subtrair(a, b):
    return a - b
    
def mult(a, b):
    return a * b

def divi(a, b):
    if b != 0:
        return a / b
    else:
        print("Valor inválido")
escolha = ""
while escolha != "0":
    escolha = input("Digite a opção que você quer realizar : 1-somar 2-subtrair, 3-multiplicar, 4-dividir ou digite zero ( 0 ) para sair do programa: ")
    num1=int(input("Digite um número ")) 
    num2=int(input("Digite outro número ")) 
    if escolha == '1':
        x=somar(num1, num2)
    elif escolha == '2': 
        x=subtrair(num1, num2)
    elif escolha == '3': 
        x=mult(num1, num2)
    elif escolha == '4':
        x=divi(num1, num2)
    else:
        break

    print(f"Resultado da operação: {x}")