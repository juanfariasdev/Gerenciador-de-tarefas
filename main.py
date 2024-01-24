import os
from components.Tasks import Tasks

def clear_console():
    os.system("cls" if os.name in ("nt", "dos") else "clear")

menu = (
    "1. Adicionar Tarefa",
    "2. Ver tarefa",
    "3. Atualizar Tarefa",
    "4. Deletar Tarefa",
    "5. Completar tarefa",
    "6. Deletar tarefas completadas",
    "7. Sair"
)

print("\nMenu Gerenciador de tarefas")

tasks = Tasks()

while True:
    clear_console()

    [print(item) for item in menu]
    
    selected_item = input("Digite sua escolha: ")

    if not selected_item.isdigit():
        print('\nEntrada inválida!\n')
        break

    selected_item = int(selected_item)

    if selected_item not in range(1, len(menu) + 1):
        print('\nEscolha inválida!!\n')
    elif selected_item == 7:
        break
    else: 
        clear_console()
        match selected_item:
            case 1:
                title = input('\n Adicione o título da tarefa: ')
                tasks.add(title)

            case 2:
                tasks.show()
                input("Pressione ENTER para continuar")
            case 3:
                task_id = int(input('\n Digite o ID da tarefa: '))
                text = input('\n Digite o texto atualizado: ')
                tasks.update(task_id, text)
            case 4:
                task_id = int(input('\n Digite o ID da tarefa: '))
                tasks.remove(task_id)
            case 5:
                task_id = int(input('\n Digite o ID da tarefa: '))
                tasks.mark_completed(task_id)
            case 6:
                tasks.removeCompleted()
