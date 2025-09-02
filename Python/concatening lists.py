#Lesson 6.7
#In Python, lists can be concatenated using the + operator or the extend() method.
# Using the + Operator
# This operator combines two lists into a new list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2  # The result is [1, 2, 3, 4, 5, 6]


#Using the extend() Method

#This method adds the elements of the second list to the end of the first list. Unlike the + operator, this method modifies the original list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # list1 is now [1, 2, 3, 4, 5, 6]




#Example:
#Consider two lists of network devices. If there is a need to create a combined list of these devices, the + operator or the extend() method can be used:

network_devices1 = ['Switch1', 'Router2', 'Firewall3']
network_devices2 = ['Switch4', 'Router5', 'Firewall6']
all_network_devices = network_devices1 + network_devices2  # Using the + operator
# or
network_devices1.extend(network_devices2)  # Using the extend() method









#6.7.1 Lab Concatening lists :

#Two lists of ports need to be combined into a single list.
#  Alter the existing "all_ports" list to concatenate the two port lists by using the + operator.
#  Additionally, extend "ports1" to include the values of "ports2" using the extend() method on line 



ports1 = [80, 443, 22, 21, 25, 53, 110, 143, 3389]
ports2 = [8080, 8443, 3306, 5432, 1521, 27017, 5900, 6667, 8081]
# do not edit above this line

# concatenate using + operator
all_ports = ports1 + ports2

# concatenate using extend() method
ports1.extend(ports2)

# do not edit below this line
print(all_ports)
print(ports1)
print(ports1 == all_ports)

# Expected output
# [80, 443, 22, 21, 25, 53, 110, 143, 3389, 8080, 8443, 3306, 5432, 1521, 27017, 5900, 6667, 8081]
# [80, 443, 22, 21, 25, 53, 110, 143, 3389, 8080, 8443, 3306, 5432, 1521, 27017, 5900, 6667, 8081]
# True