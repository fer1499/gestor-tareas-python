from config import Config
from task_manager import TaskManager


def print_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Salir")


def show_tasks(manager: TaskManager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No hay tareas registradas.")
        return

    for task in tasks:
        status = "Completada" if task["completed"] else "Pendiente"
        print(f"{task['id']}. {task['description']} [{status}]")


def main():
    config = Config()
    manager = TaskManager()

    if config.debug:
        print(f"[DEBUG] Archivo de datos: {manager.data_file}")

    while True:
        print_menu()
        option = input("Selecciona una opción: ").strip()

        if option == "1":
            description = input("Escribe la nueva tarea: ")
            try:
                task = manager.add_task(description)
                print(f"Tarea agregada con ID {task['id']}.")
            except ValueError as error:
                print(error)

        elif option == "2":
            show_tasks(manager)

        elif option == "3":
            show_tasks(manager)
            try:
                task_id = int(input("ID de la tarea a completar: "))
                if manager.complete_task(task_id):
                    print("Tarea marcada como completada.")
                else:
                    print("No existe una tarea con ese ID.")
            except ValueError:
                print("Debes introducir un ID numérico.")

        elif option == "4":
            manager.save_tasks()
            print("Tareas guardadas. Hasta luego.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
