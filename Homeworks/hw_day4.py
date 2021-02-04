#!/usr/bin/env python
# coding: utf-8

#Seyma Tufekci - seymaatufekci@gmail.com
#Homework-Day4

print("Found prime numbers between 0 and 100:")
print("")

def find_prime():

    for num in range(0, 100 + 1):
        if (num == 1):
            continue
        if num > 1:
            for i in range(2,num):
                if(num % i == 0) :
                    break
            else:
                print(num)

find_prime()

