#Create a virtual supermarket. For every article there is a price per article and a quantity
#The customers fill their carts, one after the other. Check if enough goods are available! Create a receipt for each customer.
#Get the largest and smallest number from that list
#Create a calculator

virtual_supermarket={
    'Copy': {
        'quantity': 10,
        'price': 100},
    'Pen':{
        'quantity':12,
        'price':50
    }
}
print(virtual_supermarket)
user_input = input("What would you like to buy? ")
if user_input == 'copy':
    num= input("How many do you want? ")
    y= list(virtual_supermarket)


#Get the largest and smallest number from that list

"""list_of_num=[1222,23,34,5667,-43,65,23,1,3,4,-987]
list_of_num.sort()
print(list_of_num)
print(max(list_of_num))
print(min(list_of_num))
#or
print(list_of_num[0])
print(list_of_num[-1])"""


#Create a calculator 

"""while True:
    x=float(input("Enter a number: "))
    y=float(input("Enter another number: "))
    z=input("what do you want to do (add, substract,multiple,divide): ")
    if z == 'add':
        print(x+y)
    elif z== 'substract':
        print(x-y)
    elif z =='multiple':
        print(x*y)
    elif z=='divide':
        print(x/y)
    else:
        print("Please put a valid option as given in the question.")
    user_input= input("Do you want to continue (y/n): ")
    if user_input == 'n':
        break"""
    


        