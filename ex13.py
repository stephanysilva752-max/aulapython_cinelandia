''' Desenvolva um código python que leia 3 valores e mostre qual o maior '''
v1=int(input("Digite um valor "))
v2=int(input("Digite mais um valor "))
v3=int(input("Digite outro valor "))
if (v1 > v2 and v1 > v3):
    maior = v1
elif (v2 > v3 and v2 > v1):
    maior = v2
else:
    maior = v3
print(f"o maior valor é {maior}")