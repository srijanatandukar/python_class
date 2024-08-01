"""#My_list
my_list= [1,2,3,'a','b','c']
#Add an element 
my_list.append('d')
#print(my_list)

#remove an elemeent
my_list.remove(2)
#print(my_list)

print(len(my_list))
print(my_list)"""


#tuples
"""my_tuple=(10,20,30,40,50)
#access and print second element
print(my_tuple[1])
print(my_tuple[-4]) #negative indexing access

y=list(my_tuple)
y.remove(y[2])
print(y)
y.insert(2,35)
print(y)"""

"""fruits=("apple","banana", "cherry", "strawberry", "raspberry")
(green,yellow, *red) = fruits
print(green)
print(yellow)
print(red)"""

#SET
my_set={1,2,2,3,4,4,5}
my_set.add(6)
my_set.remove(3)
num=4
if num in my_set:
    print(my_set)

#Dictionaries
my_dict={
    'name':'John',
    'age': 25,
    'city':'New York'
}
my_dict['job'] = "Engineer"
my_dict['age'] =26

print(my_dict)







