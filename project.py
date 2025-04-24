import datetime

def is_valid_date(date_string):
    """Проверяет, является ли строка корректной датой в формате YYYY-MM-DD."""
    try:
        datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_task(tasks):
    """Добавляет задачу в календарь."""
    while True:
        date = input("Введите дату задачи (YYYY-MM-DD): ")
        if is_valid_date(date):
            break
        else:
            print("Некорректный формат даты. Пожалуйста, введите дату в формате YYYY-MM-DD.")

    task = input("Введите описание задачи: ")

    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]

    print("Задача успешно добавлена!")

def view_tasks(tasks):
    """Просматривает задачи на указанную дату."""
    while True:
        date = input("Введите дату для просмотра задач (YYYY-MM-DD): ")
        if is_valid_date(date):
            break
        else:
            print("Некорректный формат даты. Пожалуйста, введите дату в формате YYYY-MM-DD.")

    if date in tasks:
        print(f"Задачи на {date}:")
        for i, task in enumerate(tasks[date]):
            print(f"{i+1}. {task}")
    else:
        print(f"На {date} задач не найдено.")

def main():
    """Главная функция программы."""
    tasks = {}  # Словарь для хранения задач (дата: список задач)

    while True:
        print("\nКалендарь задач")
        print("1. Добавить задачу")
        print("2. Посмотреть задачи на дату")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()