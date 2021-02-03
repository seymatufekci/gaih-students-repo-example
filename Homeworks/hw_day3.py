#!/usr/bin/env python
# coding: utf-8

#Seyma Tufekci - @seymaatufekci
#Homework-Day3

#Question-1:

print("User Login Application")
print("")

username = input("Username: ")
password = input("Password: ")

username_1 = "Seyma"
password_1 = "seyma123"

if (username == username_1 and password == password_1):
    print("Logged in!")
else:
    print("Username or password is wrong!")


#Question-1 Extra:

print("")
print("Extra")
print("")

login_dict = {"Seyma":"seyma123", "Zeynep":"zeynep123"}

username_2 = input("Username: ")

if (username_2 in login_dict.keys()):
    password_2 = input("Password: ")
    
    if(username_2 == "Seyma" and password_2 == "seyma123"):
        print("You're logged in, Seyma!")
    elif(username_2 == "Zeynep" and password_2 == "zeynep123"):
        print("You're logged in, Zeynep!")
    else:
        print("Password is wrong!")
else:
    print("Username is wrong!")

