print("Exemplo de captura de exeçcões")
while True:
    try:
        numero = int(input("Digite um numero inteiro:"))
        resultado = 10 / numero
        print(resultado)
    except ValueError as e:
        print(f"Erro de value error: {e}")
