"""
Loop while, e o tipo loop utlizado para reptir o bloco de código enquanto uma condição e verdadeira
Verdade -> ele continua o código.
Falso -> ele encerra o código.
break -> ele forçca a saida do while ou for.
"""

contador = 0
while contador < 5:
    contador += 1 # Adicionando o contador. Para que o loop não seja infinito.
    print("Contagem:",contador)
#  O programa faz a contagem do 0 ao 4, quando ele chega no valor, o programa reconhece que e falso.
#  Sempre que usarmos o while, precisamos de uma condição falsa. Ou podemos utilizar o (Break).