''' Crie uma função que receba o lado de um quadrado e retorne o valor dasua área ($A = lado^2$) '''

def quadrado(lado):
    #Usando o operador de exponenciação (**)
    return lado ** 2
    #interação com o usuário 
medida_lado= float(input("Digite a medida do lado do quadrado: "))
    #chamada da função e exibição do resultado
area = quadrado(medida_lado) 
print(f"A área do quadrado é: {area}")