'''Desenvolva um código python que leia um cargo de
funcionário, de acordo com o cargo mostre o salário
vide tabela abaixo
caixa-1500
vendedor-2400
gerente-4000
de acordo com os salários acima, calcule:
inss = 12% sobre o salário 
se o salário for maior que 2000 o irrf será de 14% 
sobre o salário se não será de 8%
salário fina = salário - irrf - inss '''
cargo=(input("Qual seu cargo ")).upper()
if (cargo=="CAIXA"):
    sal=1500
elif (cargo=="VENDEDOR"):
    sal=2400
elif (cargo=="GERENTE"):
    sal=4000
else:
    sal=0
    print("Cargo não existe")
inss = sal *0.12
if (sal > 2000):
    irrf = sal *0.14
else:
    irrf = sal *0.08
salfinal = sal - irrf - inss
print(f"Olá seu salário inicial é {sal}")
print(f"Seu inss é de {inss}")
print(f"Seu imposto de renda é de {irrf}")
print(f"Seu salário final é {salfinal}")