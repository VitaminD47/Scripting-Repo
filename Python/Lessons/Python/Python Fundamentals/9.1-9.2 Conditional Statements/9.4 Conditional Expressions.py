#9.4 Conditional Expressions

# 'and' Logical Operator 
# The and keyword in Python is a logical operator used in conditional statements. It returns True if both the conditions on its left and right are True. 
# If either or both conditions are False, it returns False.

# Example:
ip_address = "192.168.1.1"
first_octet = int(ip_address.split(".")[0])

if first_octet >= 1 and first_octet <= 126:
   print(f"{ip_address} is a Class A IP address.")
else:
    print(f"{ip_address} is not a Class A IP address.")
 

#This script classifies the IP address as Class A or not based on its first octet. 
# The if/else statement with the and logical operator is used to check if the first octet of the IP address is within the range of 1 to 126 (inclusive),
# and print a message accordingly.





# or Logical Operator
# The or keyword in Python is a logical operator used in conditional statements.
#  It returns True if either or both of the conditions on its left and right are True. 
# If both conditions are False, it returns False.

# Example:
ip_address = "192.168.1.1"
first_octet = int(ip_address.split(".")[0])

if first_octet == 10 or first_octet == 172 or first_octet == 192:
    print(f"{ip_address} is a private IP address.")
else:
    print(f"{ip_address} is not a private IP address.")


# This script classifies the IP address as private or not based on its first octet.
# The if/else statement with the or logical operator is used to check if the first octet of the IP address is 10, 172, or 192, 
# and prints a message accordingly.




# not Logical Operator
# The not keyword in Python is a logical operator used in conditional statements. 
# It returns True if the condition following it is False, and False if the condition is True.
#  In other words, it reverses the truth value of the condition.

#Example:
ip_address = "192.168.1.1"
first_octet = int(ip_address.split(".")[0])

if not first_octet == 127:
    print(f"{ip_address} is not a loopback IP address.")
else:
    print(f"{ip_address} is a loopback IP address.")
 

# This script classifies the IP address as a loopback or not based on its first octet.
# The if/else statement with the not logical operator is used to check
# if the first octet of the IP address is not 127, and print a message accordingly.






# Shorthand if/else


# A shorthand if statement, also known as a one-liner if statement or a ternary operator, is a way to write an if/else statement in a single line in Python. 
# It’s used when there are simple, short conditions to be checked and actions to be taken. 

# Here’s the syntax of a shorthand if statement:

# value_if_true if condition else value_if_false
 

# This will return value_if_true if condition is True, and value_if_false if condition is False.

# Example:
# Assume there is a function `is_device_up(device_ip)` that returns True if the device is up and False if it's down.

device_ip = "192.168.1.1"  # IP address of the network device

# status = "up" if is_device_up(device_ip) else "down"
# print(f"Device {device_ip} is {status}.")


# In this script, is_device_up(device_ip) is a hypothetical function that checks the status of a network device. 
# The shorthand if statement checks if the device is up, and assigns the string “up” to the variable status if it is, and “down” if it isn’t. 
# The script then prints the status of the device.

#Shorthand if statements can be very useful for making code more concise and readable, especially for simple conditions and actions.






#9.4.1 Lab : Conditional Expressions 


#A function is needed to identify the network status. Create a function name "check_network_status()". 

# The function should accept two Boolean values representing a network connection and firewall status. 

#- If both the connection and firewall are True, return "No issues detected"
#- If the connection is True and the firewall is False, return "Proceed with caution"
#- If the connection is False, return "Network not detected"
# For any other situation, return "Unexpected network status"

# Only the phrase returned by check_network_status() will be graded for this assignment. 
# The function should work for any two values passed to the function beyond the examples provided.

# 

def check_network_status(net_connection,firewall_status):
    
    if net_connection and firewall_status == True:
        return "No issues detected"
    elif net_connection == True and firewall_status == False:
        return "Proceed with caution"
    elif net_connection == False:
        return "Network not detected"
    else:
        return "Unexpected network status"


# You may alter the code below to view your return value(s).
# Only the check_network_status function will be graded for this assessment.

# No issues detected
#print(check_network_status(True, True))

# Unexpected network status
print(check_network_status(True,"Nope"))