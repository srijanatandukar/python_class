#List 

my_list = [1,2,3,'a', 'b' , 'c']
my_list.append('d')
print(my_list)
my_list.remove(2)
print(my_list)
print(len(my_list))
print(my_list)

# Tuples
my_tuple= 10,20,30,40,50
print(type(my_tuple))
print(my_tuple[2])
a= list(my_tuple)
a[3] = 35
my_tuple =tuple (a)
print(my_tuple)

#Sets
my_set = {1,2,2,3,4,4,5}
print(type(my_set))
my_set.add(6)
my_set.remove(3)
print(my_set)

a= list(my_set)

for num in a:
    if num == 3:
        print("There is 3")
        print(set(a))
else:
    print("There is no 3 in the set.")

for num in a:
    if num == 4:
        print("There is 4.")
        print(set(a))

#Dictionaries:

my_dict ={'name': 'John',
    'age': 25,
    'city' : 'New York'}

my_dict["job"]= "Engineer"
my_dict["age"]= 26
my_dict.pop("city")
print(my_dict.values())
print(my_dict.keys())
print(my_dict.get("name"))
print(my_dict)


