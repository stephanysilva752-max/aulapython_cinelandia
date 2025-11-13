''' Crie uma função que receba dois números e retorne o maior deles '''

def numeros (a, b):
    if a >= b:
        return a
    else:
        return b

v1=int(input("Digite um valor "))
v2=int(input("Digite mais um valor "))

maior = numeros(v1, v2)
print(f"Esse número é maior {maior}")

#pisco

def maior(a, b):
    if a >= b:
        return a
    else:
        return b
        
n1=int(input("Digite um valor "))
n2=int(input("Digite mais um valor "))

maior_numero = maior(v1, v2)
print(f"O maior número entre {n1} e {n2} é {maior_numero}")