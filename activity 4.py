class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_pay(self):
        return self.salary
    
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

        
emp = Employee("Ali", 30000)
mgr = Manager("Asha", 50000, 10000)

print(emp.calculate_pay())
print(mgr.calculate_pay())
    
    