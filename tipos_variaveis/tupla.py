minha_tupla = (1, 2, 3, 3 )
print("Minha tupla: ", minha_tupla)

#  Acessando uma (tupla) pelo ultimo elemento.
print(minha_tupla[-1])

print("-----------------------------")

#  Metodo count 
print("Metodo count: Conta quantas vezes o numero foi exibido na nossa tupla.")
print("Numero (3) foi exibido: ",minha_tupla.count(3))

print("-----------------------------")
#  Metodo index
indice = minha_tupla.index(3)
print("Indice da primeira ocorrencia do elemento 3: ",indice)
