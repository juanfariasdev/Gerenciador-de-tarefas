from components.Tasks import Tasks
from components.Utils import clear_console

def print_menu():
    menu = (
        "Adicionar Tarefa",
        "Ver tarefas",
        "Atualizar Tarefa",
        "Deletar Tarefa",
        "Completar tarefa",
        "Deletar tarefas completadas",
        "Sair"
    )

    print("\nMenu Gerenciador de tarefas")
    [print(f"{i + 1}. {item}") for i, item in enumerate(menu)]

def Menu():
    tasks = Tasks()

    while True:
        clear_console()
        print_menu()

        selected_item = input("Digite sua escolha: ")

        try:
            selected_item = int(selected_item)
        except ValueError:
            print('\nEntrada inválida! Digite um número.\n')
            break

        if selected_item not in range(1, 8):
            print('\nEscolha inválida!\n')
        elif selected_item == 7:
            break
        else:
            handle_menu_choice(selected_item, tasks)

def handle_menu_choice(choice, tasks):

    def get_valid_task_id_input(prompt):
        while True:
            task_id_input = input(prompt)

            if task_id_input.strip() and task_id_input.isdigit():
                try:
                    id = int(task_id_input)
                    tasks.verifyRange(id)
                    return id
                except ValueError as e:
                    print(f"ID da tarefa inválido. Tente novamente.")
            else:
                print("ID da tarefa inválido. Tente novamente.")

    clear_console()
    tasks.show()

    if choice in(3,4,5,6):
        if len(tasks.tasks) == 0:
            input("Pressione ENTER para continuar")
            return False

    match choice:
        case 1:
            title = input('\n Adicione o título da tarefa: ')
            if len(title.strip()) < 3:
                print("O título deve conter pelo menos 3 caracteres")
                pass
            else:
                tasks.add(title)   
                print(f'Tarefa "{title}" adicionada na lista!')

        case 3:
            task_id = get_valid_task_id_input('\n Digite o ID da tarefa: ')
            text = input('\n Digite o título atualizado: ')
            
            if len(text.strip()) < 3:
                print("O título deve conter pelo menos 3 caracteres")
                pass
            else:
                tasks.update(task_id, text)

                print(f'A tarefa foi renomeada para "{text}" com sucesso!')

        case 4:
            task_id = get_valid_task_id_input('\n Digite o ID da tarefa: ')
            tasks.remove(task_id)

            print(f'A tarefa com ID {task_id} foi removida com sucesso!')
            
        case 5:
            task_id = get_valid_task_id_input('\n Digite o ID da tarefa: ')
            tasks.mark_completed(task_id)

            print(f'Tarefa com ID {task_id} concluída com sucesso!')

        case 6:
            tasks.removeCompleted()

            print(f'Tarefas concluídas removidas da lista!')

    input("Pressione ENTER para continuar")
