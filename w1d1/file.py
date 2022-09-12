num1 = 42 # variable declaration, initialize numbers
num2 = 2.3 # variable declaration, initialize numbers
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuples
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, access value of list
pizza_toppings.append('Mushrooms') # add value to list
print(person['name']) # log statement, access value of dictionary
person['name'] = 'George' # variable declration, change value of dictionary
person['eye_color'] = 'blue' # variable declaration, add value to dictionary
print(fruit[2]) # log statement, access value of tuples

if num1 > 45: # if conditional
    print("It's greater") # log statement
else: # else conditional
    print("It's lower") # log statement

if len(string) < 5: # if conditional, length check
    print("It's a short word!") # log statement
elif len(string) > 15: # else if conditional
    print("It's a long word!") # log statement
else: #else conditional
    print("Just right!") # log statement

for x in range(5): # for loop stop, sequence
    print(x)
for x in range(2,5): # for loop start, stop, sequence
    print(x)
for x in range(2,10,3): # for loop start, stop, increment, sequence
    print(x)
x = 0
while(x < 5): # while loop start
    print(x)
    x += 1 # while loop increment

pizza_toppings.pop() #delete value from list
pizza_toppings.pop(1) #delete value from list

print(person) # log statement, access value of dictionary
person.pop('eye_color') # delete value from dictionary
print(person) #log statement, access value of dictionary

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # variable declaration
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): # variable declaration
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): # variable declaration
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) # NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' # TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # KeyError: 'favorite_team'
# print(pizza_toppings[7]) # IndexError: list index out of range
#   print(boolean) # IndentationError: unexpected indent
# fruit.append('raspberry') # AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'