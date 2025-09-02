#Tuples in Python are immutable sequences of arbitrary elements. They are defined by enclosing elements in parentheses (), separated by commas. 
#For example, my_tuple = (1, "a", 3.14).

#Tuples are often used in situations where an immutable sequence of data is needed. Since tuples are immutable, they can be used as keys in dictionaries, which require immutability for hash mapping. 
#Tuples also have a smaller memory footprint compared to lists, making them more efficient for large datasets.



#Lab 6.8.1 :


#How would you modify the code to create a tuple containing information about a server: SERVER1; 10.66.200.25; 255.255.0.0? 
#How would you unpack the tuple to print out the server's information? Test your code in the code editor.

# Define a tuple for a network device
network_device = ("192.168.1.1", "cisco", "admin", "password")
server_info = ("SERVER1", "10.66.200.25", "255.255.0.0")

# Unpack the tuple
ip_address, device_type, username, password = network_device
# Unpack the server_info tuple. Note that the order of the variables cannot have this order reversed i.e network_device = {variable names here} or it will return an error.
hostname, ip_address, subnet_mask = server_info


# Use the unpacked values
print(f"Connecting to device {device_type} at {ip_address} using username {username}")
print(f"Server info is: {hostname}, {ip_address}, {subnet_mask}")




#Tuples with Single Item
#A tuple with one item is created by placing a single value inside parentheses () and following it with a comma. 
# For example, single_item_tuple = ("admin",). The trailing comma is necessary to distinguish the tuple from a simple parenthesized expression.

#Creating a tuple with a single item can be useful in several scenarios. 
# For instance, when a function is expected to return a tuple, but there is only one value to return, a single-item tuple can be used. 
# This ensures that the function’s return type is consistent, which can help prevent errors.

# Define a tuple with a single item
username = ("admin",)

# Unpack the tuple
(username,) = username

# Use the unpacked value
print(f"Username: {username}")


# Another example:


# Define a tuple with a single item
MAC_addr = ("E0-2E-0B-BA-3D-AC",)

# Unpack the tuple
(mac_address_name,) = MAC_addr

# Use the unpacked value
print(f"MAC: {mac_address_name}")

#The Tuple Constructor

#The tuple() constructor in Python is a built-in function that allows the creation of a tuple. 
# It can take an iterable (like a list or a string) as an argument and convert it into a tuple. 
# This can be useful when there is a need to ensure the immutability of a sequence of data.
#Example :

# Define a list with network device information
network_device_info = ["192.168.1.1", "cisco", "admin", "password"]

# Use the tuple() constructor to convert the list into a tuple
network_device = tuple(network_device_info)

# Print the tuple
print(f"Network device: {network_device}")



#In this example above, the tuple() constructor is used to convert a list of network device information into a tuple. 
# This ensures that the information cannot be accidentally modified later in the code, providing an extra layer of protection for the data.
# This can be particularly important in network automation tasks, where an accidental modification of device information could lead to connection issues or other errors. 
# The tuple() constructor provides a simple and effective way to create tuples from other iterable data types. 
# It is a flexible tool that can be used in a variety of situations to enhance the robustness and reliability of Python code.


device_type, manufacturer, model, ip_address = ["Router", "Cisco", "ISR 4000", "10.0.0.1"]

# create device_tuple
device_tuple = ("Router", "Cisco", "ISR 4000", "10.0.0.1")
# unpack the tuple 
device_type, manufacturer, model, ip_address = device_tuple

print(device_tuple)
print(type(device_tuple))

# Expected output
# ('Router', 'Cisco', 'ISR 4000', '10.0.0.1')
# <class 'tuple'> <---This is from the type() function being applied to the device_tuple 