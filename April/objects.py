mystuff = {'apple': "I AM APPLES"}
print (mystuff['apple'])

def apple():
    print("I AM APPLES")

class Employee:

    empCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Employee.empCount += 1

    def DisplayEmpCount(self):
        print("Total Employees are", empCount)

emp1 = Employee("Bob",29)
emp2 = Employee("Reagan",1)

#Accessing Attributes
print(emp1.name)

print(emp1.DisplayEmpCount())



