

def adicionar_tarefa(tarefas,nome_tarefa):
 tarefa = {"tarefa": nome_tarefa, "Completada": False}
 tarefas.append(tarefa)
 print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
 return

def ver_tarefa(tarefas):
    for indice, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["Completada"] else ""  # Corrigindo a lógica do status
        nome_tarefa = tarefa["tarefa"]  # Garantindo que o nome da tarefa sempre seja atribuído
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

def tarefa_nome_atualizar(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_ajustado = int(indice_tarefa)  # Converte para número inteiro
    if indice_ajustado >= 0 and indice_ajustado < len(tarefas):
      tarefas[indice_tarefa] ["tarefa"] = novo_nome_tarefa
      print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa Invalido!")
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa)
    tarefas[indice_tarefa_ajustado] ["Completada"] = True
    print(f"Tarefa ({indice_tarefa}) marcada como completada")
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas :
        if tarefa["Completada"]:
            tarefa.remove(tarefa)
    print("Tarefas completada removidas com sucesso!")
    return



# Criando lista de tarefa
tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de Tarefas:")
    print("1. Adicionar Tarefa")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair")
    escolha = int(input("Digite a sua escolha: "))

    if escolha == 6:
        print("Programa finalizado...")
        break

    elif escolha == 1:
     nome_tarefa = input("Qual o nome da tarefa que deseja adicionar:")
     adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == 2:
     ver_tarefa(tarefas)

    elif escolha == 3:
        ver_tarefa(tarefas)
        indice_tarefa =input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        tarefa_nome_atualizar(tarefas, indice_tarefa, novo_nome)

    elif escolha == 4:
        ver_tarefa(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == 5:
        deletar_tarefas_completadas(tarefas)
        ver_tarefa(tarefas)
