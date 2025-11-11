''' 
Desenvolva um código em python usando while
que digite um nome e imprima, só para o
programa a digitar sair em maiusculo
!= diferente
'''
n=0
while n != 'SAIR':
    n=input("Qual seu nome? ").upper()

#PISCO

nome=""
while nome != "SAIR":
    nome=input("Digite um nome ").upper()
    print(f"Olá {nome} ")

nome=""
while nome != "SAIR":
    nome=input("Digite um nome ").upper()
    if nome == 'SAIR ':
        break #sai do laço while
    print(f"Olá {nome} ")