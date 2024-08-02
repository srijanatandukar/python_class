# Exercise 1:
#Day 2: 30 days of python programming 
first_name = "Srijana"
last_name = "Tandukar"
full_name = first_name + ' '+ last_name 
print(f"My name is {full_name}.")
country = "Nepal"
age= 22
year = 2024
is_married = False
is_true = True
is_light_on = True
fruits, vegetable = "apple", "spanish"
print(vegetable) 
cars = "Porsche", "Mercedes", "Jaquar" #tuple
cars = {"Porsche", "Mercedes", "Jaquar"} # set
cars = {"Porsche", "Porsche", "Jaquar"} # set
cars = ["Porsche", "Mercedes", "Jaquar"] #list

#Exercise 2:

print(type(cars))
print(type(full_name))
print(type(age))
print(type(country))
print(type(is_married))
print(type(fruits))
print(type(year))
print(f"The length of the first name is {len(first_name)}.")
length_first_name= len(first_name)
length_last_name= len(last_name)
print(length_first_name)
print(length_last_name)
print(max(length_first_name, length_last_name))
num_one = 5 
num_two = 4
total= num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one/ num_two
remainder = num_two % num_one
exp= num_one ^ num_two
floor_division = num_one // num_two
print(total, diff, product, division, remainder, exp, floor_division)

import math
r = 30
r = float(input("Enter the radius of the circle: ")) # taking input 
_area_of_circle =math.pi * (r * r)
print(f"The area of circle with radius {r} is {_area_of_circle:.3f}.") #with 3 decimal points
_circum_of_circle_ = 2 * math.pi * r 
print(f"The circumference of the circle with radius {r} is {_circum_of_circle_:.3f}.")


fname= str(input("Enter your firstname: "))
lname = str(input("Enter your last name : "))
fullname = fname + ' ' + lname 
country_ = input("Where are you from? ")
age = input("How old are you? ")
print(f"Hello, {fullname}. Good to know you are from {country_}. Am I right that you are {age} years old?")

help("keywords")
