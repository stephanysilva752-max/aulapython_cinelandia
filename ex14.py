''' Desenvolva um código python que verifique se
a temperatura está frio, agradavel ou calor,
siga a tabela abaixo
menor que 18 - frio
entre 18 e 30 - agradavel
maior que 30 - calor '''

temperatura=float(input("Digite a temperatura de hoje"))
if (temperatura < 18):
    print("Hoje o clima está frio")
elif (temperatura > 18 and temperatura < 30):
    print("Hoje o clima está agradável")
else:
    print("Hoje o clima está calor")

