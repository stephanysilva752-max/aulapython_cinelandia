#desenvolver um código python que leia os dois
#nomes se o primeiro nome for senac ou
#segundo nome for cinelandia imprimir SENAC
#se não imprimir não é SENAC
nome1=input("Digite o primeiro nome")
nome2=input("Digite o segundo nome")
if (nome1 == "senac" or nome2 == "cinelandia"):
    print(f"Bem vindo, {nome1} {nome2}")
else:
    print(f"Você não é senac")