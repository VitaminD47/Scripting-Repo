# List of network devices in the form of a dictionary. Dictionary is represented by { } and refers to key-value pairs i.e hostname:router1, ip: 192.168.1.1, etc.
devices = [
    {"hostname": "router1", "ip": "192.168.1.1", "type": "router"},
    {"hostname": "switch1", "ip": "192.168.1.2", "type": "switch"},
    {"hostname": "firewall1", "ip": "192.168.1.3", "type": "firewall"},
    # ... (more devices)
]
 
# Retrieve information about the second device (index 1)
second_device = devices[0]
 
# Access specific details using indexing
hostname = second_device["hostname"]
ip_address = second_device["ip"]
device_type = second_device["type"]
 
# Display the information
print(f"Device: {hostname}, IP: {ip_address}, Type: {device_type}")


# Negative Indexing
# Negative indexing in Python allows you to access elements from the end of a sequence, such as a list. 
# The index -1 corresponds to the last element, -2 to the second-to-last, and so on.
# It provides a convenient way to access elements without needing to know the length of the sequence.

#Example: Negative Indexing in Python Lists

network_devices = ['router', 'switch', 'firewall', 'server', 'printer']
 
last_device = network_devices[-1]   # 'printer' (last element)
second_last_device = network_devices[-2]   # 'server' (second-to-last element)
print(last_device)
print(second_last_device)


#Example 2

#Suppose you have a list of commands to execute on a network device, and you want to retrieve the last command:

commands = ['show interfaces', 'show ip route', 'config terminal', 'interface GigabitEthernet0/1', 'shutdown']
 
# Retrieve the last command using negative indexing
last_command = commands[-1]
 
# Display the last command
print(f"Last Command: {last_command}")


# Slicing example i.e [start:stop:step]. Step in this example defaults to 1. The syntax is always sequence[start:stop:step]    sequence refers to the list variable
ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]
# Get the first three IP addresses
first_three_ips = ip_addresses[0:5]
print(first_three_ips)  # Output: ['192.168.1.1', '192.168.1.2', '192.168.1.3']

#you can also do this with negative indexes. example below

ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]
# Get the last three IP addresses
last_three_ips = ip_addresses[-3:]
print(last_three_ips)  # Output: ['192.168.1.3', '192.168.1.4', '192.168.1.5']





#6.3.1 Example accessing list items
#A large list of network devices has been stored in the variable "network_devices".
#  Alter the variable declarations on lines 5, 8, and 11 to create new lists from the existing "network_devices" list using slicing.

network_devices = ['Switch39', 'Router49', 'Server27', 'Switch58', 'Router44', 'Server31', 'Server34', 'Switch84', 'Hub43', 'Switch80', 'Router20', 'Hub67', 'AccessPoint89', 'Firewall53', 'Server15', 'Router68', 'Router56', 'AccessPoint27', 'Router90', 'Hub33', 'Server51', 'Server12', 'AccessPoint17', 'Firewall73', 'AccessPoint28', 'Switch37', 'Switch92', 'AccessPoint99', 'AccessPoint60', 'Hub10', 'Server56', 'AccessPoint13', 'Hub5', 'Switch65', 'Router4', 'Firewall38', 'Server25', 'AccessPoint57', 'Firewall63', 'Switch17', 'AccessPoint92', 'Hub88', 'AccessPoint23', 'Firewall88', 'Switch74', 'Firewall38', 'Hub84', 'Router30', 'Router79', 'Switch56']     
# do not edit above this line

# first 10 devices
first_ten = network_devices[0:10]

# last 8 devices
last_eight = network_devices[-8:]

# every tenth device starting with the second device
every_tenth = network_devices[1::10]

# do not edit below this line
test_value = "AccessPoint23"
print(f"first_ten | {len(first_ten)} elements; {test_value in first_ten}")
print(f"last_eight | {len(last_eight)} elements; {test_value in last_eight}")
print(f"every_tenth | {len(every_tenth)} elements; {test_value in every_tenth}")

# Expected output
# first_ten | 10 elements; False
# last_eight | 8 elements; True
# every_tenth | 5 elements; False