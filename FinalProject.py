#!/usr/bin/env python
# coding: utf-8

#Seyma Tufekci - @seymaatufekci
#Final Project

#I created 3 classes as Company, Employee and Manager

print("Company Management System")
print("")

class Company():
    def __init__(self, name, age, language, job):
        self.name = name
        self.age = age
        self.language = language
        self.job = job
        
    def define_person(self):
        print("Hey! It's " + self.name + ". He's " + str(self.age) + " years old.")
        
    def show_language(self):
        print(self.name + " can talk " + self.language)  
        
    def print_name(self):
        print(self.name)


class Employee(Company):
    def __init__(self, name, age, language, job, department):
        super().__init__(name, age, language, job)
        self.department = department
    
    def print_job(self):
        print(self.name + " is " + self.job + ".")
        
    def print_dep(self):
        print(self.name + " is in " + self.department + ".")
        
employee = Employee("Dwight", 36, "English and German", "Assistan to the Regional Manager", "Sales Department")

employee.define_person()
employee.show_language()
employee.print_job()
employee.print_dep()
employee.print_name()

print("")

class Manager(Company):
    def __init__(self, name, age, language, job, year):
        super().__init__(name, age, language, job)
        self.year = year
        
    def print_year(self):
        print(self.name + " has been with this company for " + str(self.year) + " years. ")
        
manager = Manager("Michael", 40, "English", "mudur", 6)

manager.define_person()
manager.show_language()
manager.print_year()
manager.print_name()

print("")

# I tried to take name of employee.

employee.print_name()


# I added new employee who name is Jim.


employee1 = Employee("Jim", 34, "English and France", "Employee", "Sales Department")
employee1.print_name()


# I added new manager who name is Jan.


manager1 = Manager("Jan", 42, "English", "Second Manager", 3)
manager1.print_name()


# I wanted a name from users. When I take it, I compare the given name with names already know.
# If there is a match, the languages of the given name are printed. Otherwise it will be printed as an error.  

print("")
wanted = input("Please enter a name: ")

if (wanted == employee.name):
    employee.show_language()
    
elif (wanted == employee1.name):
    employee1.show_language()
    
elif (wanted == manager.name):
    manager.show_language()

elif (wanted == manager1.name):
    manager1.show_language()
else:
    print("There's no one with that name here!")





