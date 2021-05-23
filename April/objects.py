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
        print("Total Employees are", Employee.empCount)

print(Employee.empCount)

emp1 = Employee("Bob",29)
emp2 = Employee("Reagan",1)

#Accessing Attributes
print(emp1.name)

print(emp1.DisplayEmpCount())

###############################################################################################

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

############################################################################################

class Customer:
    def __init__(self, name, age, zipcode):
        self.name = name
        self.age = age
        self.zipcode = zipcode

Jermaine = Customer("Jermaine","21","80301")
Rocket = Customer("Rocket","2","80201")

print(Jermaine.name, Jermaine.age, Jermaine.zipcode)
print(Rocket.name, Rocket.age, Rocket.zipcode)

customers = [Customer("Jermaine","21","80301"),Customer("Rocket","2","80201")]

print(customers[0].name)
print(customers[0].age)
print(customers[1].zipcode)
#__init__ is the constructor
#name, age, zipcode are parameters
#Jermaine, 21, 80301 are arguments
#__init__ is a method


