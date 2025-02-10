#from time import struct_time

#from tipos_variaveis.tupla import indice

contatos = []


def Menu():
    while True:
        print("\n=== Agenda do Paulo ===")
        print("1. adicionar lcontato")
        print("2. Listar conatato")
        print("3. Editar contato")
        print("4.Marcar/Desmarcar favorito")
        print("5. Lista de favoritos")
        print("6. Deletar contato")
        print("7. Sair")

        escolher = int(input("Escolha uma das opções: "))

        if escolher == 1:
            adicioanr_contato()
        elif escolher == 2:
            listar_contato()
        elif escolher == 3:
            editar_contato()
        elif escolher == 4:
            marcar_favorito()
        elif escolher == 5:
            listar_favorito()
        elif escolher == 6:
            remover_contato()

        else:
            print("Opção inválida. Tente novamente.")
    

        
            


def adicioanr_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    favorito = input("Favorito: ")

    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'favorito': False
    }

    contatos.append(contato)
    print("Contato adicionado com sucesso!")


def listar_contato():
    for indice, contato in enumerate(contatos):
        status = "⭐" if contato['favorito'] else ""
        print(f"{indice}. [{status}] {contato['nome']} - {contato['telefone']} - {contato['email']} - {'Favorito' if contato['favorito'] else 'Não Favorito'}")
        

def editar_contato():
    listar_contato()
    try:
        indice = int(input("Digite o número do contato para editar: "))

        if 0 <= indice < len(contatos):
            contato = contatos[indice]

            nome = input(f"Novo nome (Atual: {contato['nome']}): ") or contato['nome']
            telefone = input(f"Novo telefone (Atual: {contato['telefone']}): ") or contato['telefone']
            email = input(f"Novo email (Atual: {contato['email']}): ") or contato['email']

            contato.update({'nome': nome, 'telefone': telefone, 'email': email})
            print("Contato editado com sucesso!")
        else:
            print("Contato não encontrado.")

    except ValueError:
        print("Erro: Digite um número válido.")


def marcar_favorito():
    listar_contato()
    try:
        indice = int(input("\nEscolha um número de contato para marcar/desmarcar como favorito: "))

        if 0 <= indice < len(contatos):
            contatos[indice]['favorito'] = not contatos[indice]['favorito']
            status = "favorito" if contatos[indice]['favorito'] else "não favorito"
            print(f"Contato '{contatos[indice]['nome']}' agora está como {status}.")
        else:
            print("Índice inválido.")

    except ValueError:
        print("Erro: Digite um número válido.")


def listar_favorito():
    favoritos = [c for c in contatos if c['favorito']]

    if favoritos:
        print("\n=== Lista de Favoritos ===")
        for contato in favoritos:
            print(f"{contato['nome']} - {contato['telefone']} - {contato['email']}")
    else:
        print("Nenhum contato favorito encontrado.")


def remover_contato(contatos):
    listar_contato()
    indice = int(input("Digite o numero para remover o contato: "))
    if  0 <   len(contatos):
        contato_removido = contatos.pop(indice)
        print(f"contato {contatos['nome']} - {contatos['telefone']} - {contatos['email']}")
    else:
        print("indice invalido.")
        

    

if __name__ == "__main__":
    Menu()