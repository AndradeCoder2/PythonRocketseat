import requests

# URL do site que queremos baixar
url = "https://www.python.org/"

# Fazer a requisição GET
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    with open("python_org.html", "w", encoding="utf-8") as file:
        file.write(response.text)  # Salvar o conteúdo HTML no arquivo
    print("Página baixada com sucesso! Abra 'python_org.html' no navegador.")
else:
    print(f"Erro ao baixar a página. Código: {response.status_code}")



'''
🎯 Como testar?
Execute o código em Python.
Um arquivo chamado python_org.html será criado na mesma pasta do script.
Abra o arquivo no navegador e veja o site baixado!
'''