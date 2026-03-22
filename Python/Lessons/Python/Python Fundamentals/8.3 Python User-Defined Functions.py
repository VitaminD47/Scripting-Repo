
#Python Functions
#Definition: A Python function is a named block of reusable code.

#Syntax: Defined with def, a name, parameters, and an indented code block.

#Parameters: Input values passed to the function.

#Execution: Performs specific tasks within the code block.

#Return: Optionally provides a result.

#Benefits: Enhances code modularity, readability, and reusability.

#Create a Function
#A Python function is defined using the def keyword, followed by a function name, parentheses (), and a colon :. 
# The function body is indented and includes any number of statements to be executed when the function is called. Here is an example:

def function_name():
    # function body
    pass


# In this case, function_name is the name of the function, and pass is a placeholder for the function body.

#Example:
# Consider a function that adds a new device to a set of network devices:

def add_device(network_devices, device):
    network_devices.add(device)
    return network_devices


# In this case, add_device is a function that takes two arguments: network_devices, which is a set of network devices, and device, which is the new device to be added.
# The function adds device to network_devices and returns the updated set. This represents a network automated with the new device. The function can be called as follows:

network_devices = {'Switch', 'Router', 'Firewall'}
network_devices = add_device(network_devices, 'Load Balancer')

# After this, network_devices will include the ‘Load Balancer’. This represents a network automated with the new ‘Load Balancer’. 
# The add_device function can be reused to add any number of new devices to the network. 
# This demonstrates the power and reusability of functions in Python.





def add_device(network_devices, *device):
    network_devices.update(device)
    return network_devices

# Create a set of network devices
network_devices = {'Switch', 'Router', 'Firewall'}

# Call the function to add a new device
network_devices = add_device(network_devices, 'Load Balancer', 'Proxy Server', 'Switch 2', 'Core Switch')
print(network_devices)




#Example:


#Consider a function that configures a list of network devices:

def configure_devices(device_list):
    for device in device_list:
        print(f"Configuring {device}")

new_network_devices = ['Switch1', 'Switch2', 'Router2','Router3']
configure_devices(new_network_devices)




# Returning a Value 
# A Python function returns a value using the return statement. The value that follows the return keyword is the result that the function sends back when it is called. 
# If no value is specified, the function will return None.

#Here is an example of a function that returns a value:

def function_name():
    return 'value'


#In this case, when function_name is called, it will return the string ‘value’.



#Arguments:

#Arguments in Python are values that are passed to a function when it is called. 
#Each argument is treated as a variable inside the function. 
#Arguments are used to provide inputs to a function so it can perform a task based on those inputs.

#Here is an example of a function with arguments:

def add_device(network_devices, device):
    network_devices.add(device)
    return network_devices


#In this case, network_devices and device are arguments to the function add_device. 

#The function adds device to network_devices and returns the updated set.

# Example:

# Consider a function that adds a new device to a set of network devices:



def add_device(network_devices, device):
    network_devices.add(device)
    return network_devices

# Create a set of network devices
network_devices = {'Switch', 'Router', 'Firewall'}

# Call the function to add a new device
network_devices = add_device(network_devices, 'Load Balancer')


# In this case, network_devices and ‘Load Balancer’ are passed as arguments to the add_device function. 
# The function adds ‘Load Balancer’ to network_devices and returns the updated set.
# After the function call, network_devices includes the ‘Load Balancer’.






# Parameter versus Argument

# Parameters are variables in a function's definition. 
# Arguments are actual values passed to a function.
# Parameters initialize with arguments. Both terms are often used interchangeably in discussions about functions.




# Arbitrary Arguments




# Arbitrary arguments in Python allow a function to accept any number of arguments. This is useful when the exact number of arguments is not known in advance.
#  Arbitrary arguments are defined by prefixing the argument name with an asterisk * in the function definition.

# Here is an example of a function with arbitrary arguments:

def function_name(*args):
    for arg in args:
        print(arg)


# In this case, args is a tuple of all the arguments passed to the function. The function prints each argument.

# Example:
# Consider a function that adds any number of new devices to a set of network devices:

def add_devices(network_devices, *devices):
    for device in devices:
        network_devices.add(device)
    return network_devices


# In this case, devices is a tuple of all the new devices to be added. The function adds each device to network_devices and returns the updated set.

# The function can be called as follows:

network_devices = {'Switch', 'Router', 'Firewall'}
network_devices = add_devices(network_devices, 'Load Balancer', 'Proxy Server')


# After this, network_devices will include the ‘Load Balancer’ and ‘Proxy Server’




# Another example that shows passing a list as input : 

def configure_devices(device_list):
    for device in device_list:
        print(f"Configuring {device}")

devices = ['Switch', 'Router', 'Firewall']
configure_devices(devices)





# Keyword Arguments

# Keyword arguments in Python are arguments that are identified by the parameter name in a function call.
#  With keyword arguments, the caller identifies the arguments by the parameter name,
#  which allows for the arguments to be passed in any order and makes the function call more clear.

# Here is an example of a function with keyword arguments:

def function_name(keyword1='value1', keyword2='value2'):
    # function body
    pass


# In this case, keyword1 and keyword2 are keyword arguments with default values value1 and value2.

# Example:
# Consider a function that configures a network device:

def configure_device(device_type='Switch', ip_address='192.168.1.1'):
    print(device_type, ip_address)
    pass


# In this case, device_type and ip_address are keyword arguments with **default values** ‘Switch’ and ‘192.168.1.1’. 

# The function can be called with keyword arguments as follows:

configure_device(device_type='Router', ip_address='192.168.1.2')



# This will configure a ‘Router’ with the IP address ‘192.168.1.2’. This represents a network automated with a ‘Router’.




# Arbitrary Keyword Arguments

# Arbitrary keyword arguments in Python allow a function to accept any number of keyword arguments.

# This is useful when the exact number of keyword arguments is not known in advance. 

# Arbitrary keyword arguments are defined by prefixing the argument name with double asterisks ** in the function definition.

# Here is an example of a function with arbitrary keyword arguments:

def function_name(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# In this case, kwargs is a dictionary of all the keyword arguments passed to the function. The function prints each keyword and its corresponding value.

# Example:

# Consider a function that configures a network device with arbitrary settings:

def configure_device(**settings):
    for setting, value in settings.items():
        print(f"Setting {setting} to {value}")


# In this case, settings is a dictionary of all the settings for the device. The function prints each setting and its value.

# The function can be called with arbitrary keyword arguments as follows:

configure_device(ip_address='192.168.1.1', subnet_mask='255.255.255.0', gateway='192.168.1.254')


# This will configure a device with the IP address ‘192.168.1.1’, subnet mask ‘255.255.255.0’, and gateway ‘192.168.1.254’.

# This represents a network automated with these settings. The configure_device function can be reused to configure any number of settings on a device. 






# Default Parameter Values

#  A default parameter value in Python is a value that is assigned to a function parameter when the function is defined.
#  If the function is called without an argument for that parameter, the default value is used. 
#  Default parameter values are specified by using the assignment operator = in the function definition.

# Here is an example of a function with a default parameter value:

def function_name(parameter='default value'):
    # function body
    pass


# In this case, if function_name is called without an argument, parameter will be 'default value'.


# Example:
# Consider a function that configures a network device with a default IP address:

def configure_device(device, ip_address='192.168.1.1'):
    # function body
    pass


# In this case, if configure_device is called with only one argument, ip_address will be '192.168.1.1'. The function can be called as follows:


configure_device('Router')


# This will configure a ‘Router’ with the default IP address ‘192.168.1.1’. This represents a network automated with a ‘Router’ with a default IP address. 
# The configure_device function can be reused to configure any type of device with a specified or default IP address.




# Code Editor 8.3.7: Practice

def configure_device(device, ip_address='192.168.1.1'):
   
    print(device, ip_address)
 

configure_device('Router', ip_address='10.198.20.2')





# Passing a List as an Argument




# A list can be passed as an argument to a Python function just like any other data type. The function can then perform operations on the list. Here is an example:

def function_name(list_parameter):
    for item in list_parameter:
        print(item)


# In this case, list_parameter is a list that is passed to function_name. The function prints each item in the list.

# Example:
# Consider a function that configures a list of network devices:

def configure_devices(device_list):
    for device in device_list:
        print(f"Configuring {device}")

# In this case, device_list is a list of devices that is passed to configure_devices. 
# The function prints a message for each device in the list. The function can be called with a list of devices as follows:

devices = ['Switch', 'Router', 'Firewall']
configure_devices(devices)







# Returning a Value 
# A Python function returns a value using the return statement. 
# The value that follows the return keyword is the result that the function sends back when it is called. 
# If no value is specified, the function will return None.

# Here is an example of a function that returns a value:

def function_name():
    return 'value'


# In this case, when function_name is called, it will return the string ‘value’.

# Example:
# Consider a function that counts the number of network devices:

def count_devices(network_devices):
    return len(network_devices)


# In this case, count_devices takes a list of network devices as an argument and returns the number of devices in the list.
# The function can be called as follows:


network_devices = ['Switch', 'Router', 'Firewall']
number_of_devices = count_devices(network_devices)
print(number_of_devices)



# Function Recursion:


# Function recursion in Python is a process in which a function calls itself as a subroutine. 

# This allows the function to be repeated several times, as it can call itself during its execution. Recursion can be direct or indirect.
# A direct recursion occurs if a function calls itself; 
# an indirect recursion involves the function calling another function, which eventually results in the original function being called.


# Recursion can be a powerful tool, but it can also be computationally expensive and cause a program to crash if not implemented with care.

# It's important to ensure that a recursion has a base case that will be met, which will stop the recursion.


# Here is an example of a recursive function:

def countdown(n):
    if n <= 0:
        print('Liftoff!')
    else:
        print(n)
        countdown(n-1)


# In this case, countdown is a function that takes an argument n. If n is less than or equal to 0, it prints ‘Liftoff!’. 
# Otherwise, it prints n and then calls itself with the argument n-1.

# Doing this will result in 3, 2, 1, Liftoff!
countdown(3)


# Example:
# Consider a function that pings a list of servers until it finds one that is online:

def find_online_server(servers):
    if len(servers) == 0:
        return None
    elif ping(servers[0]):
        return servers[0]
    else:
        return find_online_server(servers[1:])



#   In this case, find_online_server is a function that takes a list of servers as an argument. 
#   If the list is empty, it returns None. Otherwise, it pings the first server in the list. 
#   If the server is online (i.e., ping(server) returns True), it returns the server. 
#   Otherwise, it calls itself with the rest of the list. The ping function is a hypothetical function that checks if a server is online.
#   This represents a network automated with a recursive function to find an online server. 


# Code Editor 8.3.9: Practice It



def ping(server):
    # this function mimics finding online vs offline status by returning a Boolean at random
    from random import choice
    return choice([True, False])


def find_online_server(servers):
    if len(servers) == 0:
        return None
    elif ping(servers[0]):
        return servers[0]
    else:
        return find_online_server(servers[1:])


my_servers = ['server1', 'server2', 'server3', 'server4']
print(f"First server online: {find_online_server(my_servers)}")






#8.3.2 Lab (took me a while)

# A list of usernames contains duplicate values.
# Complete the function "set_convert()" to accept a list of usernames and any number of additional username values using arbitrary arguments. 
# The function should combine the list of usernames with the additional string values, returning  the combined list as a set with no duplicate values.


def set_convert(lst, *new_values):
    for everyitem in new_values:
        lst.add(everyitem)
    return lst


sample_values = ['user4', 'admin10', 'user5', 'user8', 'admin6', 'admin3', 'user9', 'guest9', 'guest5', 'admin3']
sample_values = set(sample_values)
set_convert(sample_values)
# You may alter the code below to view your return value(s).
# Only the set_convert function will be graded for this assessment.

print(set_convert(sample_values))
# print(set_convert(sample_values, "newuser1", "newuser2", "newuser3"))





