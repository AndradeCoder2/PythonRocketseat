#  CondiçãO
True
#  Condição falsa
False


#  Condicionais 
if True: 
  print("Bloco IF vai ser execultado")
else:
    print("Bloco ELSE não sera execultado")



"""  Operador logicos: AND """

# Ele ira comparar se o primeiro e verdadeiro, e se o segundo e verdadeiro, ele execulta o bloco de codigo.
if True and True: 
  print("Bloco sera execultado.")

# Se o primeiro for verdadeiro e o segundo falso, ele nao execultara o codigo.
if True and False: 
  print("Bloco não sera execltado.")

# Caso as duas forem falsas, ele não execultara o codigo.
if False and False: 
  print("Bloco de codigo nao sera execultado.")

print("---------------------------------------------")

""" Operador Logico: OR """
#   Quando pelo menos um dos dois forem verdadeiros.
if True or False:
  print("Bloco OR vai ser execultado.")

#  Quando os dois são falsos, ele não exseculta nenhum codigo.
if False or False:
  print("Bloco de codigo não sera execultado.")

#  Quando os dois forem Verdadeiros, o codigo sera execultado.
if True or True:
   print("Bloco de codigo sera execultado.")


