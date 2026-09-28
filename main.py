tasks = []

while True:
    print("\n===== Список задач =====")
    print("1. Добавить задачу")
    print("2. Показать список задач")
    print("3. Удалить задачу")
    print("4. Выход")
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        task = input("Введите текст задачи: ")
        tasks.append(task)
        print("Задача добавлена.")
    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        number = int(input("Введите номер задачи для удаления: "))
        tasks.pop(number - 1)
        print("Задача удалена.")
    elif choice == "4":
        break