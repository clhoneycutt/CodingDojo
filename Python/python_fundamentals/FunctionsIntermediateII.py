# 1. Given

x = [ [5,2,3], [10,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  

x[1][0] = 15

# How would you change the last_name of the first student from 'Jordan' to "Bryant"?

# students[0]['last_name'] = "Bryant"

# For the sports_directory, how would you change 'Messi' to 'Andres'?

sports_directory['soccer'][0] = "Andres"

# For z, how would you change the value 20 to 30?

z[0]['y'] = 30

# 2. Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  For example, given the following list:

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterate_dictionary(list_of_dicts):
    for dic in list_of_dicts:
        for key in dic:
            print(f"{key} - {dic[key]},", end=", ")
        print('\n')

# I had a bit of trouble with this one, I eventually needed help from reddit after not finding the answer in python docs or SO.  :)  It was a suggestion though, not just code given to me.



# iterateDictionary( students ) should output

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# 3. Create a function that given a list of dictionaries and a key name, it outputs the value stored in that key for each dictionary.  For example, iterateDictionary2('first_name', students) should output

# Michael
# John
# Mark
# KB

def iterateDictionary2(keyName, list_of_dicts):
    for dic in list_of_dicts:
        print(f"{keyName}: {dic[keyName]}")


# 4.  Say that

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# Create a function that prints the name of each location and also how many locations the Dojo currently has.  Have the function also print the name of each instructor and how many instructors the Dojo currently has.  For example, printDojoInfo(dojo) should output


def printDojoInfo(dic):
    locationCount = len(dojo["locations"])
    instructorCount = len(dojo["instructors"])
    print(locationCount, "Locations")
    for city in dic["locations"]:
        print(city)
    print(instructorCount, "Instructors")
    print()
    for instructor in dic["instructors"]:
        print(instructor)

        

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