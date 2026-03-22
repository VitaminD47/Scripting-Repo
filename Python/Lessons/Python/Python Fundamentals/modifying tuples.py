#6.9 Modifying Tuples
#Accessing Item in a Tuple
#Items in a tuple can be accessed using indexing. Indexing in Python starts from 0, meaning the first item in a tuple is at index 0, the second item is at index 1, and so on. 
# To access an item, the index of the item is placed inside square brackets [] after the tuple name.

#Example:

# Define a tuple for a network device
network_device = ("192.168.1.1", "cisco", "admin", "password")

# Access the IP address (first item in the tuple)
ip_address = network_device[0]

# Access the device type (second item in the tuple)
device_type = network_device[1]

# Print the accessed items
print(f"IP Address: {ip_address}, Device Type: {device_type}")

# The below section is mostly the same as for lists.

# Range of Indexes

# A range of indexes in a tuple can be specified using slicing. 
# Slicing in Python is done by specifying a start index and an end index separated by a colon : inside square brackets []. 
# The start index is inclusive, and the end index is exclusive.
# If the start index is omitted, slicing starts from the beginning of the tuple. 
# If the end index is omitted, slicing goes until the end of the tuple.

network_device = ("192.168.1.1", "cisco", "admin", "password", "port 22", "ssh")

# Access a range of items in the tuple (from the third item to the fifth item)
credentials = network_device[2:5]

# Print the accessed items
print(f"Credentials: {credentials}")

#Negative indexes

# Negative indexing in Python starts from the end of the sequence. 
# The last item in a tuple is at index -1, the second last item is at index -2, and so on.
#  To specify a range of negative indexes in a tuple, slicing can be used in the same way as with positive indexes.
#  The start index is inclusive, and the end index is exclusive.

#example : 

# Define a tuple for a network device
network_device = ("192.168.1.1", "cisco", "admin", "password", "port 22", "ssh")

# Access a range of items in the tuple (from the third last item to the last item)
connection_info = network_device[-3:]

# Print the accessed items
print(f"Connection Info: {connection_info}")


#Check if an item exists in a Tuple

# To determine whether a specific item exists in a tuple, the in keyword can be used in Python. 
# This keyword checks if a value is found in a sequence like a tuple. 
# If the value is in the tuple, the expression returns True. Otherwise, it returns False.

# Define a tuple for a network device
network_device = ("192.168.1.1", "cisco", "admin", "password")

# Check if 'cisco' is in the tuple
device_exists = 'cisco' in network_device

# Print the result
print(f"Device exists: {device_exists}")