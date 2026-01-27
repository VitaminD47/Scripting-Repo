



# 11.9 Input Validation
# Input validation is a crucial part of programming, especially in network automation where incorrect inputs can lead to significant issues. Here are some ways to validate function inputs in Python:

# Type Checking 
# Ensure that the input is of the expected type.

def connect_to_network_device(ip_address, username, password):
    if not isinstance(ip_address, str) or not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("All inputs must be strings")
# Value Checking
# Check if the input values are within an expected range or format.

def validate_ip(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in parts):
        raise ValueError("Invalid IP address")
# Presence Checking
# Ensure that necessary inputs are not missing.

def connect_to_network_device(ip_address=None, username=None, password=None):
    if ip_address is None or username is None or password is None:
        raise ValueError("IP address, username, and password are required")
# Length Checking 
# Validate the length of the inputs.

def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
# Pattern Matching
# Use regular expressions to match input patterns.

import re
def validate_username(username):
    if not re.match(r'^\w+$', username):
        raise ValueError("Username can only contain letters, numbers, and underscores")


# These are just a few examples. The specific validation checks will depend on the requirements of the network automation task at hand.
#  Always remember, robust input validation can prevent many bugs and security issues. 
# It’s an essential part of writing reliable, secure Python code for network automation.












# try/except Blocks



# In Python, try/except blocks are used for exception handling. 
# They allow the program to continue running even if an error or exception occurs.

# Here’s a basic structure of a try/except block:

# try:
    # Code that might raise an exception
# except ExceptionType:
    # Code to handle the exception


# The try block contains the code that might raise an exception. Python will attempt to execute this code.
# If an exception is raised in the try block, the execution immediately moves to the except block. The ExceptionType is the type of exception that the except block can handle. If the exception type matches ExceptionType, then the code within the except block is executed.
# If no exception is raised in the try block, the except block is skipped.
#Here is an example:

# try:
    x = 1 / 0   # This will raise a ZeroDivisionError
# except ZeroDivisionError:
    x = 0   # This code will be executed when the exception is caught


# In this example, a ZeroDivisionError is raised when we try to divide by zero. The except block catches this exception and sets x to zero, allowing the program to continue running instead of crashing.

# Example:

# This script doesn’t actually connect to a network device, but it demonstrates how you might structure your code to handle exceptions.

 

def connect_to_device(device):
    # Simulate connecting to a device
    if device == "bad_device":
        raise Exception("Could not connect to device")
    else:
        return "Connected to device"
 
def send_command(connection, command):
    # Simulate sending a command
    if command == "bad_command":
        raise Exception("Command failed")
    else:
        return "Command succeeded"
 
# Define device and command
device = "bad_device"
command = "my_command"
 
try:
    # Try to connect to the device and send a command
    connection = connect_to_device(device)
    result = send_command(connection, command)
    print(result)
except Exception as e:
    # If an exception occurs, print the error message
    print(f"An error occurred: {str(e)}")
 

# In this script, the connect_to_device function simulates connecting to a network device. If the device is “bad_device”, it raises an exception. 
#  The send_command function simulates sending a command to the device. If the command is “bad_command”, it also raises an exception.

# The try/except block attempts to connect to the device and send a command. 
# If an exception is raised in either function, the except block catches the exception and prints an error message. 
# This prevents the script from crashing and allows it to handle the error gracefully.

# Please replace “my_device” and “my_command” with your actual device and command. 
# If you want to see the except block in action, you can change the device to “bad_device” or the command to “bad_command”.

# It’s good practice to catch and handle exceptions in your code to make it more robust and less prone to crashing from unexpected inputs or conditions. 
# You can also have multiple except blocks to handle different types of exceptions.

# Remember, it’s generally not a good idea to use a bare except: clause or except Exception: in your code, as these will catch all types of exceptions, 
# including those you might not know how to handle or
# those that should be handled elsewhere in your code. 
# It’s better to catch and handle specific exceptions that you expect and know how to handle.


