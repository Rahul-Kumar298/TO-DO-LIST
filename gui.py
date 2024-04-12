import tkinter as tk
from tkinter import messagebox
import json
import os

root = tk.Tk()
root.title("To Do List")
root.geometry("350x250")
root.minsize(350,250)
root.maxsize(350,250)
root.configure(background='aqua')
root.wm_iconbitmap("D:/python/Project/To Do List/TO-DO-LIST/1.ico")


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

def add_task(event=None):
    task = entry.get()
    if task:
        tasks.append(task)
        save_data('data.json', data)
        list_tasks()  # Update the list of tasks displayed
        entry.delete(0, tk.END)  # Clear the entry widget after adding task

task_vars = []

def list_tasks():
    for widget in task_list.winfo_children():
        widget.destroy()  # Clear the existing widgets
    task_vars.clear()  # Clear the existing list of BooleanVars
    for task in tasks:
        var = tk.BooleanVar()
        task_vars.append(var)  # Append the BooleanVar to the list
        check = tk.Checkbutton(task_list, text=task, variable=var, width=10, onvalue=True, offvalue=False, bg='lawngreen', justify="center")
        check.pack(anchor=tk.W)

def delete_task():
    # Iterate through the tasks list in reverse order to avoid index issues
    for i in range(len(tasks)-1, -1, -1):
        # Get the variable associated with the Checkbutton
        var = task_vars[i]
        # Check if the task has been selected for deletion
        if var.get():
            # Remove the task from the list
            del tasks[i]
    # Save the updated data
    save_data('data.json', data)
    # Update the list of tasks displayed
    list_tasks()

def delete_all_tasks():
    tasks.clear()
    save_data('data.json', data)
    list_tasks()

l1 = tk.Label(root, text="To Do List", font="PlayfairDisplay 15 bold", bg="cyan")
l1.grid(row=1, column=1 , padx=30, pady=10)

l2 = tk.Label(root, text="Enter The Task :", font="PlayfairDisplay 10 bold", width=18, bg="beige").grid(row=3, column=1)
entry = tk.Entry(root, width=25, bg="beige")
entry.grid(row=4, column=1, pady=10 ,padx=0)
entry.bind("<Return>", add_task)  # Bind the <Return> event to add_task function

b1 = tk.Button(root, text="Add Task", command=add_task, width=20, bg="beige")
b1.grid(row=5, column=1)

b2 = tk.Button(root, text="Delete Task", command=delete_task, width=20, bg="beige")
b2.grid(row=7, column=1)

b3 = tk.Button(root, text="List Tasks", command=list_tasks, width=20, bg="beige")
b3.grid(row=6, column=1)

b4 = tk.Button(root, text="Delete All Tasks", command=delete_all_tasks, width=20, bg="beige")
b4.grid(row=8, column=1)

b5 = tk.Button(root, text="Exit", command=root.quit, width=20, bg="beige")
b5.grid(row=9, column=1)

# Create a Listbox to display tasks
task_list = tk.Listbox(root, height=10, width=25, bg="beige")
task_list.grid(row=2, column=2, rowspan=9, padx=8, pady=8)

 # Initially populate the list of tasks

root.mainloop()