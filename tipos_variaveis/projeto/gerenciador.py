def adicionar_tarefa(tarefas,nome_tarefa):
 tarefa = {"tarefa": nome_tarefa, "Completada": False}
 tarefas.append(tarefa)
 print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
 return

def ver_tarefa(tarefas):
 for indice, tarefa in enumerate(tarefas):
  if tarefa["Completada"]:
   status = "✓"
  else:
   status = ""
   nome_tarefa = tarefa["tarefa"]
   print(f"{indice}. [{status}] {nome_tarefa}")



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
     print("Visualizando minhas tarefas:")
     ver_tarefa(tarefas)

