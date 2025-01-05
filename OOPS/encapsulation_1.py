class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Private attribute

    def get_salary(self):  # Getter method
        return self.__salary

    def set_salary(self, new_salary):  # Setter method
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")

# Create an employee object
emp = Employee("John", 50000)
print("Salary:", emp.get_salary())  # Access private attribute via getter

emp.set_salary(60000)  # Update private attribute via setter
print("Updated Salary:", emp.get_salary())
