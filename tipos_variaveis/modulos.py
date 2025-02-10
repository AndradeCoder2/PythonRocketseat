"""
Modulos:

Definição:
São arquivos que contem definições que contem instruções que podem ser reutilizadas em outros arquivos.

Como utilizar:
1. Devmos utilizar a palavra (import) e colocar (nome_do_modulo)

Maneiras de importar:
1. import math = Estamos importando o módulo inteiro.
2. from math import sqrt = Aqui nos escolhemos o que queremos importar.
"""
from tipos_variaveis.meu_modulo import saudacao, dobro

print("Exemplo da (primeira) forma de importar:")
# Aqui estamos a importar o módulo inteiro
import math
raiz_quadra = math.sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadra}")

print("Exemplo da (Segundo) forma de importar:")
# Aqui estamos a importar o módulo inteiro
from math import sqrt
raiz_quadra = sqrt(25)
print(f"A raiz quadrada de 25 é: {raiz_quadra}")

print("\nExemplo de criação de um modulo personalizado:")
import meu_modulo
# Podemos fazer a importação separada tambem se quisermos.
mensagem = saudacao("Paulo")
resultado = meu_modulo.dobro(5)
print(mensagem)
print(f"O dobro de 5 é: {resultado}")