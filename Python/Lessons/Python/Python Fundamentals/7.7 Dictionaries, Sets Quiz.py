# 7.7.1 Lesson Quiz on Dictionaries & Sets

# What is the primary advantage of using dictionaries in Python?

# Answer ) Dictionaries allow you to associate values with descriptive keys, 
# which is particularly useful in network automation for managing information about devices, configurations, 
# or any data that involves a key-value relationship.

#2) Which Python code snippet correctly demonstrates the creation of a dictionary with key-value pairs?

# Answer ) devices = {'Router1': '192.168.1.2', 'Switch2': '10.0.0.2'}

# This is the correct way to create a dictionary in Python. It involves using curly braces and specifying key-value pairs separated by colons.

#3) Which Python code snippet correctly demonstrates the creation of a dictionary with various data types for both keys and values?

# data_types = {'string_key': [1, 2, 3], (4, 5, 6): 'tuple_key'}

# This is the correct way to create a dictionary in Python with various data types for both keys and values.
#  It involves using strings and tuples as keys and lists and strings as values.

#4) Which Python code snippet correctly demonstrates the use of the dictionary constructor, dict()?

# Answer :
d = dict([('key1', 'value1'), ('key2', 'value2')])

# This is the correct way to use the dict() function. It involves passing an iterable containing key-value pairs

#5) Which Python code snippet correctly demonstrates how to access an item in a dictionary using its key?

# Answer : 

dict2 = {"keyA": "valueA", "keyB": "valueB"}
value = dict2["keyA"]
# This is the correct way to access an item in a dictionary using its key

# 6) Which Python code snippet correctly demonstrates how to change the value of a specific key in a dictionary?

# Answer : 
devices = {"DeviceA": "192.168.1.1", "DeviceB": "10.0.0.1"}; 
devices["DeviceA"] = "192.168.1.100"

#This is the correct way to change the value of a specific key in a dictionary


#7 ) Which Python code snippet correctly demonstrates the use of the update() method to update a dictionary with the key/value pairs from another dictionary?

# Answer : 
info1 = {"A": "1", "B": "2"}; info2 = {"B": "3", "C": "4"}; 
info1.update(info2)


# 8) How can an item be added to a Python dictionary?
# To add an item to a Python dictionary, simply assign a value to a new key in the dictionary


#9) Which Python code snippet correctly demonstrates how to remove an item from a dictionary?
# Answer 
dict3 = {"keyX": "valueX", "keyY": "valueY"}; 
del dict3["keyX"]

# This is the correct way to remove an item from a dictionary using the del keyword. Remember that the .pop() method can also be used.

# 10) What does the clear() method do in a Python dictionary?
# Answer ) It removes all items from the dictionary


# 11) Which Python code snippet correctly demonstrates the use of a set to maintain a collection of unique items?

# Answer ) 

devices = {'Switch', 'Router', 'Firewall'}
new_devices = {'Firewall', 'Load Balancer'}
devices = devices.union(new_devices)


# This is the correct way to use the union() method to combine sets in Python, which automatically removes any duplicate items

# 12) How can a set be created in Python?
# Answer ) A Python set is created by placing a comma-separated sequence of items inside curly braces {}
# or by using the set() function to create a set from a list or other iterable.


# 13) What is the primary characteristic of a set created using the Python set constructor, set()?

# Answer ) The Python set constructor, set(), takes an iterable as an argument and returns a set containing the unique elements of the iterable.

# 14) How can you check if a specific item is present in a Python set?

# 15) How can items be added to a Python set?

# Answer) To add an item to a Python set, the add() method is used. To add multiple items to a Python set, the update() method is used


# 16) What does the update() method do in a Python set?

# Answer) The update() method in Python takes one or more sets as arguments and adds all their elements to the current set

#17 ) What is the difference between the remove() and discard() methods in a Python set?

# Answer) The remove() method removes the specified item from the set, but if the item does not exist, it raises an error.
# The discard() method also removes the specified item from the set, but it does not raise an error if the item does not exist.

#18) What does the clear() method do in Python? 

# Answer) The clear() method is used to empty a set, removing all items.




#19) What will be the result of trying to access the network_devices set after the following code is executed?

# Creating a set
network_devices = {'Router1', 'Switch1', 'Firewall1'}

# Using del to delete the set
del network_devices
# Answer) Once the set is deleted with the del keyword, trying to access it will result in a NameError because the set no longer exists in memory
# e.g here's the result after adding a print statement to network_devices on line 118:
# NameError: name 'network_devices' is not defined. Did you mean: 'new_devices'?