#!/usr/bin/env python
# coding: utf-8

#Seyma Tufekci - @seymaatufekci
#Homework-Day5

#Class 1 - Animals

print("Homework for Day 5")
print("")

class Animals:
    def __init__(self, name, owner, gender, species, age, genus):
        self.name = name
        self.owner = owner
        self.gender = gender
        self.species =species
        self.age = age
        self.genus = genus
        
    def print_tag(self):
        print("It's a " + self.species + " and " + self.gender + " name is " + self.name + ". " + self.gender + " owner is " + self.owner + "." )
        
    def print_appearance(self):
        print(self.name + "'s a " + str(self.age) + " year old " + self.genus + ".")
        


#Class 2 - Dogs
print("")

class Dogs(Animals):
    def __init__(self, name, owner, gender, species, age, genus, job, toilet):
        super().__init__(name, owner, gender, species, age, genus)
        self.job = job
        self.toilet = toilet
        
    def print_job(self):
        print(self.name + " is a " + self.job + ".")
        
    def toilet_train(self):
        print(self.name + " " + self.toilet + " toilet training.")
        
    def showGenus(self):
        print(self.name + " is " + self.genus)

dogs = Dogs("Max", "Dwight Schrute", "his", "dog", 4, "german shephard", "police dog", "has")

dogs.print_tag()
dogs.print_appearance()
dogs.print_job()
dogs.toilet_train()
dogs.showGenus()


#Class 3 - Cats
print("")

class Cats(Animals):
    def __init__(self, name, owner, gender, species, age, genus, color, habit):
        super().__init__(name, owner, gender, species, age, genus)
        self.color = color
        self.habit = habit
        
    def print_color(self):
        print(self.name + " is a " + self.color + " " + self.genus + "." )
    
    def print_habit(self):
        print(self.name + " is " + self.habit + ".")
        
    def showAge(self):
        print(self.name + " is " + str(self.age) + " years old.")
        
cats = Cats("Lucy", "Jim Halpert", "her", "cat", 2, "British short hair", "gray", "sleppy")

cats.print_tag()
cats.print_color()
cats.print_habit()
cats.showAge()

#I made some adding for show how it can be. In the following lines I added for cats.
print("")


cat2 = Cats("Sprinkles", "Angela Martin", "her", "cat", 5, "Persian cat", "white", "naughty")

cat2.print_tag()
cat2.print_color()
cat2.print_habit()
cat2.showAge()

#In the following lines I added for dogs.
print("")


dog2 = Dogs("Freckles", "Michael Scott", "his", "dog", 3, "dalmatian", "pet", "has")

dog2.print_tag()
dog2.print_appearance()
dog2.print_job()
dog2.toilet_train()
dog2.showGenus()

#Then I tried to see if functions work by themselves.
print("")


cat2.showAge()


print("")


dog2.showGenus()

