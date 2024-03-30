import json

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'name': [], 'tasks': []}
    return data

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

data = load_data('data.json')
name = data['name']
tasks = data['tasks']

print(f"Hello , {name}")

if not name:
    name = input("Enter your name: ")
    data['name'] = name

while True:
    choice = input("Enter 0 to view tasks, 1 to create a task, 2 to delete a task, or 3 to quit: ")
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 0:
        if not tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif choice == 1:
        new_task = input("Enter a new task (or press Enter to finish): ")
        while new_task:
            tasks.append(new_task)
            new_task = input("Enter a new task (or press Enter to finish): ")
        save_data('data.json', data)
    elif choice == 2:
        if not tasks:
            print("No tasks to delete.")
        else:
            try:
                index = int(input("Enter index number to delete that task: ")) - 1
                if 0 <= index < len(tasks):
                    del tasks[index]
                    save_data('data.json', data)
                else:
                    print("Index out of range.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    elif choice == 3:
        save_data('data.json', data)
        print("Exiting...")
        break
    else:
        print("Invalid input.")
