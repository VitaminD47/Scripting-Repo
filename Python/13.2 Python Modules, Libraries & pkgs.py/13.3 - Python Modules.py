# 13.3 Python Modules

# Creating a Python module involves writing a Python script with functions, classes, or variables, and saving it with a .py extension.
# This file can then be imported into other Python scripts using the import statement. 
# For example, if a file named mymodule.py contains a function my_function(), it can be imported and used in another script as follows:

# import mymodule
# mymodule.my_function()


# This allows for code reuse across multiple scripts, improving code organization and readability.




# Example:
# Consider a module named network.py with a function ping_device(ip_address). This function could use the os library to ping a device:

import os

def ping_device(ip_address):
    response = os.system("ping -c 1 " + ip_address)
    if response == 0:
        return True
    else:
        return False


# This module can be used in another script as follows:

#import network           network is not an actual module here

ip = '192.168.1.1'
# if network.ping_device(ip):
    #print(f'Device {ip} is online.')
# else:
    #print(f'Device {ip} is offline.')


# This script imports the network module and uses its ping_device function to check if a device is online. 
# This demonstrates how modules can be used to organize and reuse code in network automation tasks.






# Renaming a Module 
# In Python, a module can be renamed when it’s imported using the as keyword. This allows for more convenient or intuitive naming.

# Example:
# Consider a network automation module named network.py with a function ping_device(ip_address). It can be renamed upon import as follows:

# import network as net

ip = '192.168.1.1'
#if net.ping_device(ip):
    #print(f'Device {ip} is online.')
#else:
    #print(f'Device {ip} is offline.')


#In this script, network is renamed to net, making subsequent calls to the module’s functions more concise. 
# This is particularly useful when dealing with modules that have long or complex names.



# Built-In Modules
# Built-in modules in Python are libraries that come pre-installed with Python. 
# They provide functions and classes for a variety of tasks without the need for additional installation.

# For example, the os and socket modules are often used in network automation.
#  The os module provides functions for interacting with the operating system, while the socket module is used for network communications.


# Here’s an example of using these modules to get the hostname and IP address:

import socket
import os

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f'Hostname: {hostname}')
print(f'IP Address: {ip_address}')


# In this script, socket.gethostname() gets the host name and socket.gethostbyname(hostname) gets the IP address of the host. 
# The os module could be used for tasks like changing directories or running system commands.









# List Function Names :
# To list all function names in a Python module, the dir() function can be used.
# It returns a list of names in the current local scope or a list of attributes of an object.
# When a module is passed as an argument to dir(), it returns a list of the module’s attributes, including its functions. Here’s an example:



import math
functions = [name for name in dir(math) if callable(getattr(math, name))]
print(functions)


# In this script, dir(math) returns a list of all attributes of the math module. 
# The list comprehension filters this list to include only callable attributes, i.e., functions. 

# The result is a list of all function names in the math module. This method can be applied to any module to list its functions. 
# Note that this will also include built-in functions and classes. To exclude these, additional filtering criteria may be needed.






# Import from a Module
# In Python, specific parts of a module can be imported using the from ... import ... statement. 
# This allows for importing only the necessary functions or classes, making the code more efficient.

# Consider a network automation task that requires the ping function from a module named network_tools.py. 
# Instead of importing the entire module, only the ping function can be imported as follows:

# from network_tools import ping          this is commented out because network_tools is not an actual module

ip = '192.168.1.1'
# if ping(ip):
  #  print(f'Device {ip} is online.')
# else:
  #  print(f'Device {ip} is offline.')


# In this script, only the ping function is imported from network_tools, and it can be used directly without prefixing it with the module name. 
# This makes the code cleaner and more readable.









# The ipaddress Module
# The ipaddress module in Python is a powerful tool for manipulating and analyzing IP addresses and networks.
# It provides classes for handling IPv4 and IPv6 addresses, networks, and interfaces. These classes support validation, comparison, sorting, and other operations.

# Example:
import ipaddress

# Define the network
network = ipaddress.ip_network('192.0.2.0/24')

# Iterate over all hosts in the network
for host in network.hosts():
    print(host)


# In this example, ipaddress.ip_network('192.0.2.0/24') creates an IPv4 network object.
# The hosts() method of the network object is used to iterate over all the hosts in the network. 

# Each host is then printed to the console. 
# This can be useful in network automation tasks, such as configuring network devices or checking the status of hosts in a network. 

# Note that the ipaddress module automatically handles the intricacies of IP addressing, such as excluding the network and broadcast addresses from the list of hosts.

# This allows network engineers to focus on the automation task at hand, rather than the details of IP addressing.










# The help Module
# The help() function in Python is a built-in function that can be used to access the built-in documentation for Python modules, functions, classes, keywords, etc.
# This function is most commonly used in the Python interpreter, and it is a very useful tool for understanding and using different Python functionalities.

# Here is an example of how to use the help() function:

help(print)
 

# This will display the documentation for the print function. The output will include a brief description of the function, its syntax, the arguments it takes, and what it returns.

# The help() function can also be used on Python modules. For example:

import os
help(os)


# This will display the documentation for the os module, including descriptions of the module’s functions and attributes.

# In conclusion, the help() function is a powerful tool for accessing Python’s built-in documentation and understanding how to use different Python functionalities. 
# It is highly recommended to use this function when unsure about the usage of a Python function, method, or module. 
# It is an essential tool for Python programming and network automation.







# 13.3.1 Python Modules Lab : 

# Complete the function "get_ip_version()" that accepts a string representing a valid IP address. 
# Use "ipaddress.ip_address()" on the string to convert the value into a IPv4Address or IPv6Address object. 
# Then use "version" from the imported ipaddress module to determine whether the object is version 4 or 6. Return both the IP object and the version.


# The version of an IP object can be determined by running "name_of_ip_object.version"

import ipaddress

def get_ip_version(ip_address_str):
    ip = ipaddress.ip_address(ip_address_str)
    version = ip.version
    return ip, version



# You may alter the code below to view your return value(s).
# Only the get_ip_version function will be graded for this assessment.

# Example usage: "192.168.1.1 is version 4"
results = get_ip_version("192.168.1.1")
print(f"{results[0]} is version {results[1]}")

# Example usage: "2001:db8:85a3::8a2e:370:7334 is version 6"
# results = get_ip_version("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
# print(f"{results[0]} is version {results[1]}")

# help(ipaddress.ip_address)