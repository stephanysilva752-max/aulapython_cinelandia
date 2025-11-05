'''Estudo de caso:
Você foi contratado pelo exercíto brasileiro
para desenvolver um sistema de alistamento
militar, onde se le o ano de nascimento
do candidato e o genero, o sistema irá calcular 
a idade,
se a idade for maior igual a 18 e o sexo masculino
ele estará apto a se alistar, se não apto '''

ano_nasc_cand=int(input("Digite seu ano de nascimento "))
genero=input("Digite o sexo M ou F ").upper()
#print(ano_nasc_cand)
#print(genero)
idade=2025-ano_nasc_cand
if(idade >= 18 and genero == "M"):
    print("Apto a se alistar")
else:
    print("Não apto")