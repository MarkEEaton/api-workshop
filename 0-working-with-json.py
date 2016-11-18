# let's make a list
my_list = ["reference", "circulation", "cataloging", "instruction"]

# let's print our list
print(my_list)

# let's make a dictionary
# a dictionary consists of key/value pairs
my_dictionary = {"M": "music",
                 "P": "literature",
		 "B": "religion",
		 "L": "education",
		 "V": "naval science"}

# let's print our dictionary
print(my_dictionary)

# how do we get something out of a list?
# we identify it by its position in the list!
# the first item in the list is 0, the next is 1, etc.
# try it out:
print(my_list[1])

# how do we get something out of a dictionary?
# we identify it by its key!
print(my_dictionary['V'])

# we can combine these data types to build more complex structures
my_list.append(my_dictionary)

# let's print our fancy multidimensional data
print(my_list)

# as you might guess, you can keep adding additional complexity to
# your data. It can get as complex as you want!
