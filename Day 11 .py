# employee.py
class Employee:
    def __init__(self, name, department, salary, joining_year):
        self.name = name
        self.department = department
        self.salary = float(salary)
        self.joining_year = int(joining_year)

    def display(self):
        print(f"Name: {self.name}, Department: {self.department}, Salary: {self.salary}, Year: {self.joining_year}")

    def to_line(self):
        return f"{self.name},{self.department},{self.salary},{self.joining_year}\n"

    @staticmethod
    def from_line(line):
        name, department, salary, year = line.strip().split(',')
        return Employee(name, department, float(salary), int(year))


# manager.py
from employee import Employee
import os

class EmployeeManager:
    def __init__(self, filepath="employee_data.txt"):
        self.filepath = filepath
        self.employees = []
        self.load()

    def load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as file:
                for line in file:
                    self.employees.append(Employee.from_line(line))

    def save(self):
        with open(self.filepath, "w") as file:
            for emp in self.employees:
                file.write(emp.to_line())

    def add_employee(self):
        try:
            name = input("Enter name: ")
            department = input("Enter department: ")
            salary = float(input("Enter salary: "))
            year = int(input("Enter joining year: "))
            emp = Employee(name, department, salary, year)
            self.employees.append(emp)
            print("Employee added.")
        except ValueError:
            print("Invalid input.")

    def list_employees(self):
        for emp in self.employees:
            emp.display()

    def search_employee(self, term):
        results = list(filter(lambda e: term.lower() in e.name.lower() or term.lower() in e.department.lower(), self.employees))
        for emp in results:
            emp.display()

    def sort_by_salary(self, desc=False):
        self.employees.sort(key=lambda e: e.salary, reverse=desc)
        self.list_employees()

    def generate_report(self, filename="employee_report.txt"):
        with open(filename, "w") as file:
            file.write(f"Total Employees: {len(self.employees)}\n")
            if self.employees:
                avg = sum(e.salary for e in self.employees) / len(self.employees)
                file.write(f"Average Salary: {avg:.2f}\n")
                top = max(self.employees, key=lambda e: e.salary)
                file.write(f"Top Earner: {top.name} - {top.salary}\n")


# utils.py
def clear_screen():
    print("\n" * 100)

def pause():
    input("Press Enter to continue...")


# main.py
from manager import EmployeeManager
from utils import clear_screen, pause

def main():
    manager = EmployeeManager()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Search by Name/Dept")
        print("4. Sort by Salary")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.list_employees()
        elif choice == "3":
            term = input("Enter search term: ")
            manager.search_employee(term)
        elif choice == "4":
            desc = input("Sort descending? (y/n): ").lower() == "y"
            manager.sort_by_salary(desc)
        elif choice == "5":
            manager.generate_report()
        elif choice == "6":
            manager.save()
            print("Exiting...")
            break
        else:
            print("Invalid option.")

        pause()
        clear_screen()

if __name__ == "__main__":
    main()
