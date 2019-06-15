x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")
else:
    print("oooo needs some work")

x = 5
y = 10
if len("cat") < x:
    print("Question 2 works!")
else:
    print("Still missing out")
    
x = 2
y = 5
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")
else:
    print("Oh good you can count")

name = input("whats your name?")

group1 = ["Greg", "Tony", "Susan"]
group2 = ["Gerarld", "Paul", "Ryder"]
group3 = ["Carla", "Dan", "Jefferson"]

if name in group1:
    print(name + " is in group 1")
elif name in group2:
    print(name + " is in group 2")
elif name in group3:
    print(name + " is in group 3")
else:
    print(name + " does not have a group")
    
    
height = 65
age = 18
adult_permission = True

if (height > 70) and (age >=18):
    print("Can ride all roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height >60) and (age >=18):
    print("Can ride light roller coasters")
elif ((height > 50) and (age >= 18) or (adult_permission) and (height >50)):
    print("Can ride bumber cars")
else:
    print("Stick to lazy river")
    
    
    
    

 


















# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 17:45:20 2019

@author: Jose L. Mendoza
"""

