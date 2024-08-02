#For loop 
numbers= [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)
    number +=1

sum= 0
for num in numbers:
    sum = sum + num 
    num += 1
print(f"The total sum of the numbers in the list is {sum}")


#While Loop 

counter = 1
while counter <= 10 :
    print(counter)
    counter +=1

count = 0 
while count <= 10:
    print(count)
    count +=2

#Looping over a string
message = "Hello, World!"
for i in message:
    print(i)
    
#Nested Loop 

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

for row in matrix:
    for element in row:
        print(element)