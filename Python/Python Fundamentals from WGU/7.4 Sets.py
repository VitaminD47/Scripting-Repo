# 7.4 Python Sets
#    A Python set is a built-in data type that holds an unordered collection of unique items.
#   The purpose of a set is to perform operations like the mathematical set operations. 
#   Sets are used when the existence of an object in a collection is more important than the order or how many times it occurs.

#   Using sets can make code more readable and efficient when dealing with collections of items where each item is unique and the order does not matter.
#    Sets allow for efficient membership tests, meaning it is faster to check whether an item exists in a set compared to other data types.
# Example:
network_devices = {'Switch', 'Router', 'Firewall'}
new_devices = {'Firewall', 'Load Balancer'}

# Add new devices to the network
network_devices = network_devices.union(new_devices)

# In this case, a ‘Load Balancer’ is added to the network_devices set. 
# The union operation combines the network_devices and new_devices sets, automatically removing any duplicate items. 
# The network is now automated with the new ‘Load Balancer’. The ‘Firewall’, which already existed in the network_devices set, is not duplicated. 
# This demonstrates the usefulness of sets in maintaining collections of unique items.




# Creating a Set
# A Python set is created by placing a comma-separated sequence of items inside curly braces {}. Alternatively, the set() function can be used to create a set from a list or other iterable. Here is an example:



# Using curly braces
set1 = {'item1', 'item2', 'item3'}

# Using the set() function
set2 = set(['item1', 'item2', 'item3'])

#In both cases, set1 and set2 are sets containing the items ‘item1’, ‘item2’, and ‘item3’.



# Example:
# Consider creating a set of network devices:

network_devices = {'Switch', 'Router', 'Firewall'}


# In this case, network_devices is a set containing the items ‘Switch’, ‘Router’, and ‘Firewall’. This represents a network automated with these three devices.






# Determine the Number of Items in a Set
# The number of items in a Python set can be determined using the len() function. Here is an example:

set1 = {'item1', 'item2', 'item3'}
number_of_items = len(set1)


# In this case, number_of_items will be 3, as there are three items in set1.



# Example:
# Consider a set of network devices:

network_devices = {'Switch', 'Router', 'Firewall'}
number_of_devices = len(network_devices)


# In this case, number_of_devices will be 3, as there are three devices in the network_devices set.
#  This represents a network automated with three devices.



# The set() Constructor


# The Python set constructor, set(), is a built-in function for creating a set. 
# It takes an iterable (like a list or a string) as an argument and returns a set containing the unique elements of the iterable.
#  If no argument is given, it creates an empty set.

# Here is an example:

# Using a list as an argument
set1 = set(['item1', 'item2', 'item3', 'item1'])

# Using a string as an argument
set2 = set('hello')


# In the first case, set1 will be {'item1', 'item2', 'item3'}, as the duplicate ‘item1’ is removed.
# In the second case, set2 will be {'h', 'e', 'l', 'o'}, as the duplicate ‘l’ is removed and the order of the elements is not preserved.





# Example:
# Consider creating a set of VLANs:

vlans = set([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

#In this case, vlans is a set containing the VLAN IDs 10, 20, 30, 40, 50, 60, 70, 80, 90, and 100. This represents a network with these ten VLANs configured.



# Accessing items in a Set :
# Items in a Python set cannot be accessed by referring to an index or a key, because sets are unordered collections of items.
# However, one can loop through the set items using a for loop, or ask if a specified value is present in a set by using the in keyword.

# Here is an example of looping through a set:

set1 = {'item1', 'item2', 'item3'}
for item in set1:
    print(item)


# This will print each item in the set.

# Here is an example of checking if an item is in the set:

set1 = {'item1', 'item2', 'item3'}
if 'item1' in set1:
    print('item1 is in the set')

# This will print ‘item1 is in the set’ if ‘item1’ is in set1.


# Example 2:
# Consider a set of network devices:

network_devices = {'Switch', 'Router', 'Firewall'}
for device in network_devices:
    print(device)


# This will print each device in the network_devices set. This represents a network automated with these devices.

# Note: Once a set is created, the items within the set cannot be changed. However, new items can be added to the set. 

