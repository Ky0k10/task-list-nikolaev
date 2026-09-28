def show_menu():
    print("\n===== Список задач =====")
    print("1. Добавить задачу")
    print("2. Показать список задач")
    print("3. Удалить задачу")
    print("4. Выход")


def add_task(tasks):
    task = input("Введите текст задачи: ").strip()
    if not task:
        print("Задача не может быть пустой.")
        return
    tasks.append(task)
    print(f"Задача «{task}» добавлена.")


def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    print("\nВаши задачи:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    if not tasks:
        print("Список задач пуст, удалять нечего.")
        return
    show_tasks(tasks)
    number = input("Введите номер задачи для удаления: ").strip()
    if not number.isdigit():
        print("Нужно ввести число.")
        return
    index = int(number) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Задача «{removed}» удалена.")
    else:
        print("Задачи с таким номером нет.")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Выберите пункт меню: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Такого пункта нет, выберите от 1 до 4.")


if __name__ == "__main__":
    main()