# 13.4 Python Libraries

# Install Library
# Python libraries can be installed using package managers like pip. 
# The command pip install library_name is used in the command line interface.
# For instance, to install the netmiko library, which is commonly used in network automation, the command would be pip install netmiko. 


# It’s recommended to use a virtual environment to avoid conflicts between libraries. 
# If the library is already installed, it can be upgraded using pip install --upgrade library_name.
# Always ensure pip is upgraded to the latest version before installing libraries.


# Standard Library
# The Python Standard Library is a collection of modules and packages that come pre-installed with Python.
# It provides a wide range of functionalities, including mathematical operations, file I/O, system calls, and even Internet protocols. 

# This library is considered “standard” because it’s available in every Python installation. 
# It’s designed to enhance Python’s usability and standardize solutions for common programming tasks, reducing the need for third-party libraries. 
# The Python Standard Library is a key reason for Python’s popularity, as it simplifies many complex tasks in areas like network automation, data analysis, and web development.



# Running a Library 
# Running a Python library involves importing it into a Python script and then calling its functions or classes. 
# For instance, the socket library, which is part of the Python Standard Library, can be used for network automation tasks. 

#Example:
# Here’s an example of using it to establish a TCP connection:

import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server and the port
server = 'hostname'
port = 80

# Connect to the server
s.connect((server, port))


# In this script, the socket library is imported, and its socket function is used to create a socket object. 
#The connect method of this object is then used to establish a connection to a server.
# This is a basic example of how a Python library can be run to perform a network automation task.