''' Crie uma função que receba um nome como argumento (string) e retorne uma mensagem de saudação completa.'''

def saudar(nome):
    return (f"Olá, {nome}! Seja bem-vindo(a) ao mundo Python!")
    #interação com o usuário
nome_usuário = input("Digite seu nome: ")
    #chamada da função e exibição do resultado
mensagem = saudar(nome_usuário)
print(mensagem)