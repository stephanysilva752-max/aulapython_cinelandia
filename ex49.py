''' Peça dois números e uma operação. Use try-except-else-finally para tratar erros 
como divisão por zero e operação inválida. '''

def calculadora():
    try:
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        op=input("Digite a operação ( +, -, *, /) ")

        match op:
            case '+':
                resultado = a + b
            case '-':
                resultado = a - b
            case '*':
                resultado = a * b
            case '/':
                resultado = a / b
            case _:
                raise ValueError("Operação Inválida")
    except ZeroDivisionError:
        print("Erro: divisão por zero!") 
    except ValueError as e:
        print(f"{e}")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Cálculo encerrado.")     

calculadora()