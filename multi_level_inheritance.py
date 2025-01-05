class CSE_department:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        return f"I am {self.name}, my age is {self.age}"
 
class Cse_Student(CSE_department):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

    def introduction(self):
        student_introduction = super().introduction()
        return f"{student_introduction}, my roll number is {self.roll}"

class Cse_Teacher(CSE_department):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduction(self):
        teacher_introduction = super().introduction()
        return f"{teacher_introduction}, my subject is {self.subject}"

if __name__ == "__main__":
    while True:
        print("Enter your choice:")
        print("1. Student")
        print("2. Teacher")
        print("3. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            roll = int(input("Enter your roll number: "))
            student = Cse_Student(name, age, roll)
            print(student.introduction())
        elif choice == 2:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            subject = input("Enter your subject: ")
            teacher = Cse_Teacher(name, age, subject)
            print(teacher.introduction())
        elif choice == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")
