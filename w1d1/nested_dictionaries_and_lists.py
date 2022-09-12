# 1. Update Values in Dictionaries and Lists
# 1-1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
from doctest import OutputChecker


x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)
# output: [[5, 2, 3], [15, 8, 9]]


# 1-2. Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]["last_name"] = "Bryant"
print(students[0])
# output: {'first_name': 'Michael', 'last_name': 'Bryant'}]


# 1-3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
# output: {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'soccer': ['Andres', 'Ronaldo', 'Rooney']}


# 1-4. Change the value 20 in z to 30
z = [{'x': 10, 'y': 20}]
z[0]["y"] = 30
print(z)
#  output: [{'x': 10, 'y': 30}]


# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    for i in range(0, len(some_list)):
        for key, val in some_list[i].items():
            print(key, ' - ', val)

iterateDictionary(students)
# output:
# first_name  -  Michael
# last_name  -  Jordan
# first_name  -  John
# last_name  -  Rosales
# first_name  -  Mark
# last_name  -  Guillen
# first_name  -  KB
# last_name  -  Tonel


# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
def iterateDictionary2(key, some_list):
    for x in some_list:
        print(x[key])

iterateDictionary2('first_name', students)
# output:
# Michael
# John
# Mark
# KB

iterateDictionary2('last_name', students)
# output:
# Jordan
# Rosales
# Guillen
# Tonel



# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, val in some_dict.items():
        print(len(val), key.upper())
        for val in some_dict[key]:
            print(val)

printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon