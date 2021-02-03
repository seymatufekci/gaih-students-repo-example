#!/usr/bin/env python
# coding: utf-8

#Seyma Tufekci - @seymaatufekci
#Homework-Day2


#Question-1:

print("Question-1")
print("")
hw_list = list(range(10))
print(hw_list)
part1_list = hw_list[0:5]
hw_list[0:5] = []
hw_list.extend(part1_list)
print(hw_list)


#Question-2:

print("")
print("Question-2")
print("")
n = int(input("Please enter a single digit integer: "))
while n<0 or n>9:
    n = int(input("Try Again! Please enter a single digit integer: "))

nums = list(range(n+1))
#print(nums)
even_list = [i for i in nums if i %2 == 0]
while 0 <= n and n <= 9:
    print(even_list)
    break

