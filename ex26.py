''' Desenvolva um código python 
que leia 5 números e diga se cada
número ao momento que for lido se é par ou impar '''

for i in range(1,6):
    s=int(input('Digite um valor '))
    if s % 2 == 0:
        print(f"{s} é par")
    else:
        print(f"{s} é impar")
        