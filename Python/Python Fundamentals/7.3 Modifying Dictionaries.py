# Change Dictionary Items
# In Python, you can change the values in a dictionary by directly assigning a new value to a specific key. Dictionaries are mutable, allowing for in-place modifications.

# Changing Values in a Python Dictionary:
# Creating a dictionary
network_devices = {
    'Router1': '192.168.1.1',
    'Switch1': '10.0.0.1',
    'Firewall1': '172.16.0.1',
    'Server1': '192.168.2.1',
}

# Changing the value of a specific key
network_devices['Router1'] = '192.168.1.100'



# In network automation, you might want to update the IP address of a router in a device information dictionary.

# Device information dictionary
device_info = {
    'Router1': {'ip': '192.168.1.1', 'vendor': 'Cisco', 'os': 'IOS'},
    'Switch1': {'ip': '10.0.0.1', 'vendor': 'Cisco', 'os': 'IOS-XE'},
    'Firewall1': {'ip': '172.16.0.1', 'vendor': 'PaloAlto', 'os': 'PAN-OS'},
}
 
# Changing the IP address of a specific router
device_info['Router1']['ip'] = '192.168.1.100'

# In this example, the IP address of 'Router1' is updated to '192.168.1.100' within the device_info dictionary. 
# This ability to modify values makes dictionaries well-suited for representing and managing dynamic information in network automation scripts.


# Removing an Item from a Dictionary
# To remove an item from a Python dictionary, the del keyword or the pop() method can be used.

# Here is an example using the del keyword:

dictionary = {'key1': 'value1', 'key2': 'value2'}
del dictionary['key1']


# In this case, the item with ‘key1’ is removed from the dictionary.

# The pop() method also removes an item from the dictionary and returns the value of the removed item:

dictionary = {'key1': 'value1', 'key2': 'value2'}
value = dictionary.pop('key1')


# Here, the item with ‘key1’ is removed and its value ‘value1’ is returned and stored in the variable value.

# For a network automation example, consider a dictionary that stores network devices and their IP addresses. To remove a device from the network:

network_devices = {'Switch': '192.168.1.1', 'Router': '192.168.1.2'}
del network_devices['Switch']


# In this case, the ‘Switch’ and its corresponding IP address are removed from the network_devices dictionary. The network is now automated without the ‘Switch’.





# Updating a Python Dictionary 
# In Python, the update() method is used to update a dictionary with the key/value pairs from another dictionary, or from an iterable of key/value pairs. 
# Here is a general example:


# Define two dictionaries
dict1 = {"key1": "value1", "key2": "value2"}
dict2 = {"key2": "new_value2", "key3": "value3"}

# Update dict1 with dict2
dict1.update(dict2)

# After this code is executed, dict1 will be {"key1": "value1", "key2": "new_value2", "key3": "value3"}.










# In the context of network automation, the update() method might be used to update information about a network device. 

# Example 2:
# Define a dictionary with device information
device_info = {"ip_address": "192.168.1.1", "hostname": "switch1", "model": "Cisco 3750"}

# Define a dictionary with updated device information
updated_info = {"model": "Cisco 3850", "os_version": "15.2"}

# Update device_info with updated_info
device_info.update(updated_info)

# In this example, the model of the network device is updated from “Cisco 3750” to “Cisco 3850”, and the OS version is added to the dictionary. 
# After this code is executed, device_info will be {"ip_address": "192.168.1.1", "hostname": "switch1", "model": "Cisco 3850", "os_version": "15.2"}.
# Note that if a key in the second dictionary already exists in the first dictionary, the value for that key in the first dictionary will be updated. 
# If a key in the second dictionary does not exist in the first dictionary, a new item with that key and value will be added to the first dictionary.



# Adding Dictionary Items 
# To add an item to a Python dictionary, simply assign a value to a new key in the dictionary. Here is an example:

dictionary = {'key1': 'value1', 'key2': 'value2'}
dictionary['key3'] = 'value3'

# In this case, a new item with ‘key3’ and ‘value3’ is added to the dictionary.

# For a network automation example, consider a dictionary that stores network devices and their IP addresses. To add a new device to the network:

network_devices = {'Switch': '192.168.1.1', 'Router': '192.168.1.2'}
network_devices['Firewall'] = '192.168.1.3'





 # Clearing a Dictionary
 # To clear a Python dictionary, the clear() method is used. Here is an example:

dictionary = {'key1': 'value1', 'key2': 'value2'}
dictionary.clear()


# After executing the clear() method, the dictionary will be empty.

# For a network automation example, consider a dictionary that stores network devices and their IP addresses. To clear the network:

network_devices = {'Switch': '192.168.1.1', 'Router': '192.168.1.2'}
network_devices.clear()


# After executing the clear() method, the network_devices dictionary will be empty, indicating that the network has no automated devices.







# 7.3.1 Lab : Modifying Dictionary Items 


networking_dict = {
    'router': {
        'model': 'Cisco 2900 Series',
        'ports': 24,
        'ip_address': '192.168.1.1',
        'subnet_mask': '255.255.255.0'
    },
    'switch': {
        'model': 'Juniper EX Series',
        'ports': 48,
        'ip_address': '192.168.1.2',
        'subnet_mask': '255.255.255.0'
    },
    'firewall': {
        'model': 'Palo Alto Networks PA-220',
        'ports': 8,
        'ip_address': '192.168.1.3',
        'subnet_mask': '255.255.255.0'
    }
}
# do not edit above this line

# alter the number of ports on the router to "28"
networking_dict['router']['ports'] = '28'

# change the subnet mask of the firewall to "255.255.254.0"
networking_dict['firewall']['subnet_mask'] = '255.255.254.0'

# remove the entry for the switch from the dictionary
del networking_dict['switch']

# do not edit below this line
print(networking_dict)

# Expected output
# {'router': {'model': 'Cisco 2900 Series', 'ports': 28, 'ip_address': '192.168.1.1', 'subnet_mask': '255.255.255.0'}, 
# 'firewall': {'model': 'Palo Alto Networks PA-220', 'ports': 8, 'ip_address': '192.168.1.3', 'subnet_mask': '255.255.254.0'}}