class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        return f"I am {self.name}, my age is {self.age}"

class CSE_department:
    def __init__(self, department_name):
        self.department_name = department_name

    def department_info(self):
        return f"I am part of the {self.department_name} department."

class Cse_Student(Person, CSE_department):
    def __init__(self, name, age, roll, department_name):
        Person.__init__(self, name, age)
        CSE_department.__init__(self, department_name)
        self.roll = roll

    def introduction(self):
        person_info = Person.introduction(self)
        department_info = CSE_department.department_info(self)
        return f"{person_info}, my roll number is {self.roll}. {department_info}"

class Cse_Teacher(Person, CSE_department):
    def __init__(self, name, age, subject, department_name):
        Person.__init__(self, name, age)
        CSE_department.__init__(self, department_name)
        self.subject = subject

    def introduction(self):
        person_info = Person.introduction(self)
        department_info = CSE_department.department_info(self)
        return f"{person_info}, I teach {self.subject}. {department_info}"

if __name__ == "__main__":
    while True:
        print("\nEnter your choice:")
        print("1. Student")
        print("2. Teacher")
        print("3. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            roll = int(input("Enter your roll number: "))
            department_name = "CSE"
            student = Cse_Student(name, age, roll, department_name)
            print(student.introduction())
        elif choice == 2:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            subject = input("Enter your subject: ")
            department_name = "CSE"
            teacher = Cse_Teacher(name, age, subject, department_name)
            print(teacher.introduction())
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")
