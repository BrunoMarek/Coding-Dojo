# # Update Values in Dictionaries and Lists

# x = [ [5,2,3], [15,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Bryant'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Andres', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 30} ]


# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# # Change the last_name of the first student from 'Jordan' to 'Bryant'
# # In the sports_directory, change 'Messi' to 'Andres'
# # Change the value 20 in z to 30


# # Iterate Through a List of Dictionaries
# # Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(some_list):
    for i in range(0, len(some_list)):
        output = ""
        for key,val in some_list[i].items():
            output += f" {key} - {val},"
        print(output)

iterate_dictionary(students)

# ! Get Values From a List of Dictionaries
# : Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
# * Michael
# * John
# * Mark
# * KB

def iterate_dictionary2(key_name,some_list):
    for i in range(0, len(some_list)):
        
        for key,val in some_list[i].items():
            if key == key_name:
                print(val)

iterate_dictionary2('first_name',students)
iterate_dictionary2('last_name',students)

# # TODO: And iterateDictionary2('last_name', students) should output:
# # * Jordan
# # * Rosales
# # * Guillen
# # * Tonel


# ! Iterate Through a Dictionary with List Values
# TODO: Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(some_dict):
    for key,val in some_dict.items():
        print(f"{len(val)}")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)
# * output:
# * 7 LOCATIONS
# * San Jose
# * Seattle
# * Dallas
# * Chicago
# * Tulsa
# * DC
# * Burbank
    
# * 8 INSTRUCTORS
# * Michael
# * Amy
# * Eduardo
# * Josh
# * Graham
# * Patrick
# * Minh
# * Devon