
#You can perform different actions to modify lists. That could be deleting it, clearing it, changing values within it based off index, etc. Here are some options below:

#In Python, the pop() method is used to remove an item at a specified position in a list and return it.
#  If no index is specified, it removes and returns the last item in the list. 
# The syntax is list.pop(index), where index is the position of the item to be removed.

#Example:
#Here’s an example where a device name is popped from a list of device names:

device_names = ["Switch1", "Router2", "Firewall3", "Switch4"]
# Pop the last device from the list
popped_device = device_names.pop()
print(popped_device)  # Output: 'Switch4'
print(device_names)  # Output: ['Switch1', 'Router2', 'Firewall3']



#In Python, the remove() method is used to remove the first occurrence of a specified item from a list. 
# The syntax is list.remove(element), where element is the item to be removed.


#Here’s an example where a device name is removed from a list of device names:

device_names = ["Switch1", "Router2", "Firewall3", "Switch4"]
# Remove a device from the list
device_names.remove("Switch4")
print(device_names)  # Output: ['Switch1', 'Router2', 'Firewall3']



#Extend List
#In Python, the extend() method is used to add multiple items to the end of a list.
#  The syntax is list.extend(iterable), where iterable can be a list, tuple, string, or any iterable object.


#Here’s an example where a list of device names is extended with another list:

device_names = ["Switch1", "Router2", "Firewall3"]
# Extend the list with new devices
new_devices = ["Switch4", "Router5"]
device_names.extend(new_devices)
print(device_names)  # Output: ['Switch1', 'Router2', 'Firewall3', 'Switch4', 'Router5']






#Add List Items 
#In Python, the append() method is used to add an item to the end of a list. 
# The syntax is list.append(element), where element is the item to be added.

#Here’s an example where a device name is appended to a list of device names:

device_names = ["Switch1", "Router2", "Firewall3"]
# Append a new device to the list
device_names.append("Switch4")
print(device_names)  # Output: ['Switch1', 'Router2', 'Firewall3', 'Switch4']



#Inserting Items into a List
#In Python, the insert() method is used to add an item at a specific position in a list. 
# The syntax is list.insert(index, element), where index is the position in the list where the new element should be inserted.

#Here’s an example where a device name is inserted into a list of device names:

device_names = ["Switch1", "Router2", "Firewall3"]
# Insert a new device at the second position
device_names.insert(1, "Switch2")
print(device_names)  # Output: ['Switch1', 'Switch2', 'Router2', 'Firewall3']






#Change a Range of Items in a List 
#In Python, the values of specific items within a range in a list can be changed by using slicing and assignment. 
# The syntax is list[start:stop] = new_values, where new_values is a list of new values.


#Here’s an example where the values of specific items within a range in a list of device statuses are changed:

device_statuses = ["up", "down", "up", "up", "down"]
# Change the status of the second and third devices
device_statuses[1:3] = ["up", "up"]
print(device_statuses)  # Output: ['up', 'up', 'up', 'up', 'down']



#Changing Item in a List 
#In Python, the value of a specific item in a list can be changed by referring to the index of the item. The syntax is list[index] = new_value.

#Here’s an example where the value of a specific item in a list of device names is changed:

device_names = ["Switch1", "Router2", "Firewall3"]
# Change the name of the second device
device_names[1] = "Router_A"
print(device_names)  # Output: ['Switch1', 'Router_A', 'Firewall3']

























#Lab 6.4.2 activity example:
network_devices = ['Switch39', 'Router49', 'Server27', 'Switch58', 'Router44', 'Server31', 'Server34', 'Switch84', 'Hub43', 'Switch80', 'Router20', 'Hub67', 'AccessPoint89', 'Firewall53', 'Server15', 'Router68', 'Router56', 'AccessPoint27', 'Router90', 'Hub33', 'Server51', 'Server12', 'AccessPoint17', 'Firewall73', 'AccessPoint28', 'Switch37', 'Switch92', 'AccessPoint99', 'AccessPoint60', 'Hub10', 'Server56', 'AccessPoint13', 'Hub5', 'Switch65', 'Router4', 'Firewall38', 'Server25', 'AccessPoint57', 'Firewall63', 'Switch17', 'AccessPoint92', 'Hub88', 'AccessPoint23', 'Firewall88', 'Switch74', 'Firewall38', 'Hub84', 'Router30', 'Router79', 'Switch56']

altered_list = []
# do not edit above this line
del network_devices[10:]
network_devices[1:3] = ["removal pending", "removal pending"]
network_devices[8] = "AccessPoint23"
altered_list = network_devices


# remove last 40 devices

# change second and third devices to "removal pending"

# change device at index 8 to "AccessPoint23"


# do not edit below this line
print(f"devices: {len(altered_list)}")
print(altered_list)

# Expected output
# devices: 10
# ['Switch39', 'removal pending', 'removal pending', 'Switch58', 'Router44', 'Server31', 'Server34', 'Switch84', 'AccessPoint23', 'Switch80']

