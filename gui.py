import tkinter as tk
from tkinter import messagebox
import json

root = tk.Tk()
root.title("To Do List")
root.geometry("300x250")
root.configure(background='lightblue')
root.wm_iconbitmap("1.ico")

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'tasks': []}
    return data

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

data = load_data('data.json')

tasks = data['tasks']

def add_task():
    task = entry.get()
    tasks.append(task)
    save_data('data.json', data)
    list_tasks()  # Update the list of tasks displayed

def list_tasks():
    task_list.delete(0, tk.END)  # Clear the existing list
    for task in tasks:
        task_list.insert(tk.END, task)

def delete_task():
    # Get the index of the selected task
    selected_index = task_list.curselection()
    if selected_index:
        task_index = selected_index[0]
        del tasks[task_index]
        save_data('data.json', data)
        list_tasks()
def delete_all_tasks():
    tasks.clear()
    save_data('data.json', data)
    list_tasks()

l1 = tk.Label(root, text="To Do List", font="PlayfairDisplay 15 bold")
l1.grid(row=1, column=2 )

l2 = tk.Label(root, text="Enter The Task :", font="PlayfairDisplay 10 bold").grid(row=3, column=1)
entry = tk.Entry(root)
entry.grid(row=4, column=1)

b1 = tk.Button(root, text="Add Task", command=add_task)
b1.grid(row=5, column=1)

b2 = tk.Button(root, text="Delete Task", command=delete_task)
b2.grid(row=7, column=1)

b3 = tk.Button(root, text="List Tasks", command=list_tasks)
b3.grid(row=6, column=1)

b4 = tk.Button(root, text="Delete All Tasks", command=delete_all_tasks)
b4.grid(row=8, column=1)

b5 = tk.Button(root, text="Exit", command=root.quit)
b5.grid(row=9, column=1)

# label_task = tk.Label(root, text=" TASKS :", font="PlayfairDisplay 10 bold")
# label_task.grid(row=4, column=1)

# Create a Listbox to display tasks
task_list = tk.Listbox(root)
task_list.grid(row=2, column=2, rowspan=9, padx=8, pady=8)

# Initially populate the list of tasks

root.mainloop()

