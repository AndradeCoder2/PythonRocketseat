"""
 Módulos de terceiros são pacotes criados por terceiros, não faz parte do padrão Python.
 Iremos fazer uma requisição da ‘internet’.
 Biblioteca (request) que contém funções, que ajdua a fazer requisções http,
 Basicamente são rquisicões em sites na ‘internet’
 Neste exemplo específico vamos faze uma requisição e vamos receber um retorno
"""
from conda.core.portability import replace_pyzzer_entry_point_shebang

# pip3 install requests==2.31.0

print("\nImportação do uso de um módulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")