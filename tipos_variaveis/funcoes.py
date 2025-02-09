#  Funções em Python, significa que e um bloco de código reutilizavel.
#  Ele execulta uma tarefa expecifica quando chamado.
#  Conseguimos definir um pedaço do código toda vez que quisermos chamar.

""" Criando uma funçaão sem retorno """



# Criando a função
def saudacao(nome):
    print(f"Olá, {nome} ")

# Chamando a função
saudacao("Paulo")
saudacao("Gabrielle")

""" Criando uma função com retorno """
def numero_quadrado(numero):
    resultado = numero ** 2
    return resultado
print("\nChamando função ao quadrado")
print("Resultado da função quadrado:",numero_quadrado(33))

""" Função com multiplos parametros """
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
print("\nChamando a função soma:")
numero1 = 30
numero2 = 30
resul = soma(numero1, numero2)
print(resul)







