# Add Items to a Set
# To add an item to a Python set, the add() method is used. Here is an example:

set1 = {'item1', 'item2', 'item3'}
set1.add('item4')


#In this case, ‘item4’ is added to set1.

#To add multiple items to a Python set, the update() method is used. Here is an example:

set1 = {'item1', 'item2', 'item3'}
set1.update(['item4', 'item5'])


#In this case, ‘item4’ and ‘item5’ are added to set1.

#Example:
#Consider a set of network devices:

network_devices = {'Switch', 'Router', 'Firewall'}
network_devices.add('Load Balancer')
print(network_devices)


#In this case, a ‘Load Balancer’ is added to the network_devices set. This represents a network automated with the new ‘Load Balancer.’

# Adding Sets
# To add items from another set into the current set in Python, the update() method is used. 
# This method takes one or more sets as arguments and adds all their elements to the current set. Here is an example:

set1 = {'item1', 'item2', 'item3'}
set2 = {'item4', 'item5'}
set1.update(set2)


# Example:
# Consider two sets of network devices:

network_devices = {'Switch', 'Router', 'Firewall'}
new_devices = {'Load Balancer', 'Proxy Server'}
network_devices.update(new_devices)


# In this case, ‘Load Balancer’ and ‘Proxy Server’ from the new_devices set are added to the network_devices set. 
# This represents a network automated with these five devices. 
# The update() method ensures that there are no duplicate devices in the network_devices set, even if a device is already present in the set before the update.







# Removing an Item from a Set 
# To remove an item from a Python set, the remove() or discard() method can be used. 
# The remove() method removes the specified item from the set, but if the item does not exist, it raises an error. 
# The discard() method also removes the specified item from the set, but it does not raise an error if the item does not exist.

# Here is an example using the remove() method:

set1 = {'item1', 'item2', 'item3'}
set1.remove('item1')

#In this case, ‘item1’ is removed from set1.

# Here is an example using the discard() method:

set1 = {'item1', 'item2', 'item3'}
set1.discard('item1')

# Example 2:
# Consider a set of network devices:

network_devices = {'Switch', 'Router', 'Firewall'}
network_devices.remove('Switch')

# In this case, the ‘Switch’ is removed from the network_devices set. This represents a network automated without the ‘Switch’.




# Emptying a Set 
# To empty a Python set, the clear() method is used. Here is an example:

set1 = {'item1', 'item2', 'item3'}
set1.clear()


# After executing the clear() method, set1 will be an empty set.

# Example:
# Consider a set of network devices:

network_devices = {'Switch', 'Router', 'Firewall'}
network_devices.clear()


# After executing the clear() method, the network_devices set will be empty. This represents a network with no automated devices





# Deleting a Set
# In Python, you can delete a set using the del keyword. 
# This removes the entire set from memory, and attempting to use the set afterward will result in a NameError because the set no longer exists.


# Example of deleting:

# Creating a set
network_devices = {'Router1', 'Switch1', 'Firewall1'}
# Using del to delete the set
del network_devices

# Deleting a set can be useful when you no longer need the set and want to free up memory resources.





# Lab 7.5.1: Modifying Python Sets


# Two existing sets "protocol1" and "protocol2" contain various internet protocols. 
# Add the protocol "FTP" to the first set of protocols. 
# Next combine both protocol sets together into "protocol1".
# Last, remove "TCP' from the combined set.

protocol1 = {'TCP', 'UDP', 'ICMP', 'TCP', 'IGMP'}
protocol2 = {'UDP', 'ICMP', 'HTTP', 'HTTPS', 'HTTPS'}
# do not edit above this line

# add "FTP" to protocol1
protocol1.add('FTP')

# combine sets into protocol1
protocol1.update(protocol2)

# remove "TCP" from combined protocol1
protocol1.remove('TCP')

# do not edit below this line
print("Number of combined protocols: ", len(protocol1))
print("Contains FTP: ", "FTP" in protocol1)
print("Contains TCP: ", "TCP" in protocol1)

# Expected output
# Number of combined protocols:  6
# Contains FTP:  True
# Contains TCP:  False

