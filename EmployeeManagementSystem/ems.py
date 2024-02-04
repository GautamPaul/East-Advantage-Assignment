import json


class Employee:
    def __init__(self, name, id, title, department):
        self.name = name
        self.id = id
        self.title = title
        self.department = department

    def display_employee(self):
        print(f"Name: {self.name}, ID: {self.id}, Title: {self.title}, Department: {self.department}")

        
    def __str__(self):
        return f"{self.name} {self.id}"
    

class Department:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def add_employee(self, employee):
        emp_ids = [emp.id for emp in self.employees]
        if employee.id not in emp_ids:
            self.employees.append(employee)
        else:
            # update to take valid id
            raise(f"Employee with id {employee.id} already exists.")
    
    def remove_employee(self, employee_id):
        e = None
        for employee in self.employees:
            if employee.id == employee_id:
                e = employee
                break
        self.employees.remove(e)
        

    def list_employees(self):
        for employee in self.employees:
            employee.display_employee()

    def display_department(self):
        print(f"Department Name: {self.name}")
        print("Employees List:")
        self.list_employees()


class DepartmentEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


    
company = {}

with open("company.json", "r") as c:
    company_data = json.load(c) or {}
    for department in company_data.keys():
        employees = company_data[department]["employees"]
        employee_list = []
        for employee in employees:
            e = Employee(**employee)
            employee_list.append(e)
        d = Department(name=department, employees=employee_list)
        company[department] = d


def menu():
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Display Department")
    print("4. Exit")


def add_employee():
    name = input("Enter name: ")
    id = input("Enter id: ")
    title = input("Enter title: ")
    department = input("Enter department: ")
    employee = Employee(name=name, id=id, title=title, department=department)
    if company.get(department):
        company[department].add_employee(employee)
    else:
        d = Department(name=department, employees=[employee])
        company[department] = d
    with open("company.json", "w") as f:
        f.write(json.dumps(company, cls=DepartmentEncoder))

def remove_employee():
    departments = [key for key in company.keys()]
    print(f"Available departments: {departments}")
    department = input("Choose a department from which you wish to remove employee: ")
    if department in company.keys():
        company[department].list_employees()
        employee_id = input("Enter id of employee to remove: ")
        company[department].remove_employee(employee_id)
    else:
        print("Invalid department.")
    with open("company.json", "w") as f:
        f.write(json.dumps(company, cls=DepartmentEncoder))


def display_department():
    print(list(company.keys()))
    department = input("Enter department to display: ")
    if department in company.keys():
        company[department].display_department()
    else:
        print(f"Department {department} does not exist.")


if __name__ == "__main__":
    while True:
        menu()
        choice = int(input("Select an operation: "))
        if choice == 1:
            add_employee()
        elif choice == 2:
            remove_employee()
        elif choice == 3:
            display_department()
        elif choice == 4:
            break