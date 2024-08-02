#Integer Operation 
#Create two integer variables, a and b, and assign them values of your choice.
a= 10
b=78
print(a,b)
#Perform addition, subtraction, multiplication, and division with these variables and print the results.
addition= a+b
if a>b:
    subtraction= a-b
else:
    subtraction=b-a
multiplication= a*b
if a>b:
    division= a/b
else:
    division = b/a
print(addition)
print(subtraction)
print(multiplication)
print(division)


#Float Operation
#Create two float variables, x and y, and assign them values of your choice.
#Perform addition, subtraction, multiplication, and division with these variables and print the results.
x= 58.6
y= 586.55555
addition= x+y
if x>y:
    subtraction= x-y
else:
    subtraction=y-x
multiplication= x*y
if x>y:
    division= x/y
else:
    division = y/x
print(addition)
print(subtraction)
print(multiplication)
print(division)
print(type(addition))
print(type(multiplication))
print(type(division))

#String operation 
greeting= "Hello, World"
#Print the length of the string 
print(len(greeting))
#Convert the string to upercase and print the result
print(greeting.upper())
#Extracting the substring "World" from the greeting variable
world= greeting[7:]
print(world.upper())

#Boolean Operations
#Create two boolean variables, is_sunny and is_raining, with values True and False, respectively.
is_sunny = bool(1)
is_raining = bool(0)
print(is_sunny)
print(is_raining)

#Print the result of the logical AND operation between is_sunny and is_raining.
condition1= is_sunny and is_raining
condition2= is_sunny or is_raining
print(condition1, condition2)
