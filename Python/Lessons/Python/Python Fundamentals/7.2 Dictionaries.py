
#Python Dictionaries
#  A dictionary in Python is an unordered, mutable collection that stores key-value pairs.
#  Each key must be unique, and it is associated with a specific value.
#  Dictionaries are defined using curly braces {}, and key-value pairs are separated by colons.

#Purpose of Dictionaries
# Key-Value Mapping: Dictionaries allow you to associate values with descriptive keys, providing a convenient way to represent relationships between data.
# Fast Retrieval: Due to hashing, dictionaries offer fast and efficient retrieval of values based on keys.
# Flexibility: Dictionaries are versatile for representing complex data structures, configurations, and mappings.



# Creating Dictionaries
# In Python, you can create dictionaries using curly braces {} and specifying key-value pairs separated by colons :.
# Each key-value pair represents an item in the dictionary.

# Example:

# Creating a dictionary with key-value pairs
network_devices = {
    'Router1': '192.168.1.1',
    'Switch1': '10.0.0.1',
    'Firewall1': '172.16.0.1',
    'Server1': '192.168.2.1',
}






# Example 2:
# Consider a scenario where you want to store information about network devices, including their IP addresses and roles.

# Dictionary representing network devices
network_devices = {
    'Router1': '192.168.1.1',
    'Switch1': '10.0.0.1',
    'Firewall1': '172.16.0.1',
    'Server1': '192.168.2.1',
}
 
# Accessing information about a specific device
router_ip = network_devices['Router1']
 
# Adding a new device to the dictionary
network_devices['Switch2'] = '10.0.0.2'
 
# Resulting updated dictionary
# {'Router1': '192.168.1.1', 'Switch1': '10.0.0.1', 'Firewall1': '172.16.0.1', 'Server1': '192.168.2.1', 'Switch2': '10.0.0.2'}



#  Creating a dictionary with device information
device_info = {
    'Router1': {'ip': '192.168.1.1', 'vendor': 'Cisco', 'os': 'IOS'},
    'Switch1': {'ip': '10.0.0.1', 'vendor': 'Cisco', 'os': 'IOS-XE'},
    'Firewall1': {'ip': '172.16.0.1', 'vendor': 'PaloAlto', 'os': 'PAN-OS'},
}





#In Python dictionaries, the keys and values can be of various data types. Commonly supported data types include:

# Keys in dictionaries can be of any immutable data type, such as integers, strings, or tuples.
# Lists and dictionaries, which are mutable, cannot be used as keys.

# Values can be of any data type, including integers, floats, strings, lists, dictionaries, tuples, and more.
# The flexibility of Python dictionaries allows for the storage of diverse and nested data structures.
# Example:
# Dictionary with various data types
mixed_data_types = {
    'integer_key': 42,
    'string_key': 'hello',
    'list_key': [1, 2, 3],
    'nested_dict_key': {'nested_key': 'value'},
    'tuple_key': (4, 5, 6),
}

# In this example, the mixed_data_types dictionary demonstrates the ability to use different data types for both keys and values. 
# The versatility of Python dictionaries makes them powerful for handling a wide range of data structures in network automation and other applications.





# Python Dictionary Constructor

# The Python dictionary constructor, dict(), is a built-in function that allows you to create a dictionary from various data structures.
# It can take no arguments, a dictionary, or an iterable containing key-value pairs.

# Role and Function of the Dictionary Constructor : 

# Creating Empty Dictionaries: You can use dict() to create an empty dictionary.

# Converting from Iterables: It can convert a list of tuples or other iterable sequences into a dictionary.

# Copying Dictionaries: It can create a new dictionary by copying the contents of an existing dictionary.

# Example:

# Example: Creating a dictionary using the constructor for network devices
device_list = [('Router1', '192.168.1.1'), ('Switch1', '10.0.0.1'), ('Firewall1', '172.16.0.1')]
 
# Using the dictionary constructor to convert a list of tuples into a dictionary
network_devices = dict(device_list)
 
# Resulting dictionary: {'Router1': '192.168.1.1', 'Switch1': '10.0.0.1', 'Firewall1': '172.16.0.1'}
 

# In this network automation example, the device_list contains tuples representing device names and their corresponding IP addresses. 
# The dict() constructor is used to convert this list of tuples into a dictionary (network_devices), providing a concise way to organize device information in a format suitable for network automation tasks.





# 7.2.1 LAB :

# A dictionary of device names and IP addresses has been stored in the variable "network_devices".

# Alter the existing variable "ip" to store the IP value of the dictionary "network_devices" based on the input device name. 


network_devices = {
    "router": "192.168.1.1",
    "switch": "192.168.1.2",
    "firewall": "192.168.1.3",
    "server": "192.168.1.4",
    "printer": "192.168.1.5"
}

device_name = input("Enter a device name: ")

if device_name not in network_devices:
  print("Device not found")
# do not edit above this line

else:
  ip = network_devices[device_name]
  print(ip)

# Expected output
# Enter a device name: firewall
# 192.168.1.3

# Expected output
# Enter a device name: laptop
# Device not found

