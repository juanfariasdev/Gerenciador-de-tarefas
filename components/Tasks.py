class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

class Tasks:
    def __init__(self):
        self.tasks = []

    def verifyRange(self, position):
        if position < 0 or position >= len(self.tasks):
            raise ValueError("Posição fora do intervalo")

    def add(self, text):
        self.tasks.append(Task(text))
    
    def update(self, position, text):
        self.tasks[position].title = text

    def mark_completed(self, position):
        self.tasks[position].completed = True

    def remove(self, position):
        del self.tasks[position]

    def removeCompleted(self):
        self.tasks = [task for task in self.tasks if not task.completed]

    def show(self):
        print("\nTasks")
        print("--------------------")
        if not self.tasks:
            print("Nenhuma task cadastrada.")
            print("--------------------")

        else:
            for index, task in enumerate(self.tasks):
                print(f"ID: {index}")
                print(f"Título: {task.title}")
                print(f"Completada: {task.completed}")
                print("--------------------")


# tarefas = Tasks()

# tarefas.add('opa')
# tarefas.add('bão')
# tarefas.add('item')
# tarefas.add('item')

# tarefas.mark_completed(0)
# tarefas.update(0, 'Obaa')
# tarefas.remove(2)
# tarefas.removeCompleted()

# tarefas.show()

