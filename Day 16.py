import argparse
import json
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# File to store tasks
TASK_FILE = 'tasks.json'


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task})
    save_tasks(tasks)
    print(Fore.GREEN + "Task added successfully!")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print(Fore.YELLOW + "No tasks found.")
        return
    print(Fore.CYAN + "Your Tasks:")
    for i, t in enumerate(tasks, 1):
        print(Fore.CYAN + f"{i}. {t['task']}")


def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(Fore.RED + f"Deleted: {removed['task']}")
    except IndexError:
        print(Fore.RED + "Invalid task number.")


def export_tasks(filename):
    tasks = load_tasks()
    with open(filename, 'w') as f:
        for i, t in enumerate(tasks, 1):
            f.write(f"{i}. {t['task']}\n")
    print(Fore.GREEN + f"Tasks exported to {filename}")


def main():
    parser = argparse.ArgumentParser(
        description="📝 Simple To-Do List CLI App – Add, View, Delete, Export tasks"
    )
    subparsers = parser.add_subparsers(dest='command')

    # Add task
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('task', type=str, help='Task description')

    # View tasks
    subparsers.add_parser('view', help='View all tasks')

    # Delete task
    parser_delete = subparsers.add_parser('delete', help='Delete a task by number')
    parser_delete.add_argument('index', type=int, help='Task number to delete')

    # Export tasks
    parser_export = subparsers.add_parser('export', help='Export tasks to a text file')
    parser_export.add_argument('filename', type=str, help='Output filename (e.g., todo.txt)')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.task)
    elif args.command == 'view':
        view_tasks()
    elif args.command == 'delete':
        delete_task(args.index)
    elif args.command == 'export':
        export_tasks(args.filename)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
