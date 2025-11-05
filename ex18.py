produto=input("Qual desses produtos você comprou? (MOUSE,TECLADO OU MEMORIA) ").upper()
if (produto == "MOUSE"):
    val=10
    print(f"O valor deste item é {val}")
elif (produto == "TECLADO"):
      val=20
      print(f"O valor deste item é {val}")
elif (produto == "MEMORIA"):
      val=100
      print(f"O valor deste item é {val}")
else:
    val=0
    print("Você não comprou nenhum produto da seleção")
    
quantidade=int(input("Quantos itens você comprou "))
total= val*quantidade
if (quantidade > 10 ):
    p = total * 0.05
else:
    p = total * 0.1

valorfinal = total + p
print("***NOTA FISCAL***")
print(f"Produto escolhido {produto}")
print(f"Valor do seu produto {val}")
print(f"Quantidade escolhida {quantidade}")
print(f"Valor do seu imposto {p}")
print(f"Seu valor final é {valorfinal}")

#exemplo pisco

produto=input("Digite o nome do produto ").upper()
if(produto=="MOUSE"):
    preco=10
elif(produto=="MEMORIA"):
    preco=100
elif(produto=="TECLADO"):
    preco=20
else:
    preco=0
    print("Produto não existe")
qtd=int(input("Digite a quantidade"))
total = preco * qtd
if(qtd > 10):
    imposto=total*0.05
else:
    imposto=total*0.1
vf= total + imposto
print(f"Produto escolhido {produto}")
print(f"Valor do seu produto {preco}")
print(f"Quantidade escolhida {qtd}")
print(f"Seu valor final é {vf}")
