import argparse
import json
import os
import logging
from colorama import Fore, Style, init

# Setup logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Initialize colorama
init(autoreset=True)

TASK_FILE = 'tasks.json'


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    try:
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Error loading tasks: {e}")
        return []


def save_tasks(tasks):
    try:
        with open(TASK_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        logging.error(f"Error saving tasks: {e}")


def add_task(task):
    try:
        tasks = load_tasks()
        tasks.append({'task': task})
        save_tasks(tasks)
        print(Fore.GREEN + "Task added successfully!")
    except Exception as e:
        logging.error(f"Error adding task: {e}")
        print(Fore.RED + "Failed to add task.")


def view_tasks():
    try:
        tasks = load_tasks()
        if not tasks:
            print(Fore.YELLOW + "No tasks found.")
            return
        print(Fore.CYAN + "Your Tasks:")
        for i, t in enumerate(tasks, 1):
            print(Fore.CYAN + f"{i}. {t['task']}")
    except Exception as e:
        logging.error(f"Error viewing tasks: {e}")
        print(Fore.RED + "Failed to view tasks.")


def delete_task(index):
    try:
        tasks = load_tasks()
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(Fore.RED + f"Deleted: {removed['task']}")
    except IndexError:
        logging.error("Invalid task number for deletion")
        print(Fore.RED + "Invalid task number.")
    except Exception as e:
        logging.error(f"Error deleting task: {e}")
        print(Fore.RED + "Failed to delete task.")


def export_tasks(filename):
    try:
        tasks = load_tasks()
        with open(filename, 'w') as f:
            for i, t in enumerate(tasks, 1):
                f.write(f"{i}. {t['task']}\n")
        print(Fore.GREEN + f"Tasks exported to {filename}")
    except Exception as e:
        logging.error(f"Error exporting tasks: {e}")
        print(Fore.RED + "Failed to export tasks.")


def main():
    parser = argparse.ArgumentParser(
        description="📝 Simple To-Do List CLI App – Add, View, Delete, Export tasks"
    )
    subparsers = parser.add_subparsers(dest='command')

    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('task', type=str, help='Task description')

    subparsers.add_parser('view', help='View all tasks')

    parser_delete = subparsers.add_parser('delete', help='Delete a task by number')
    parser_delete.add_argument('index', type=int, help='Task number to delete')

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
