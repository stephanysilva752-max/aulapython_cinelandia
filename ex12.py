'''Desenvolva um código python que verifique se digitou m ou f, masculino para m e feminino para f caso seja diferente de um dos dois, diga indefinido '''
genero=input("Digite seu genero (M ou F)").upper()
if (genero == "M" ):
    print("Seu genero é masculino")
elif (genero == "F"):
    print("Seu genero é feminino")
else:
    print("Seu genero é indefinido")
