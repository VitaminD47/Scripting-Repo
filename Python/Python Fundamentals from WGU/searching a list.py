#Searching a List 
#In Python, the 'in' keyword is used to check if a specified item is present in a list, tuple, string, or other iterable object. 
#If the item is found, it returns True; otherwise, it returns False.

#Example:
#Suppose you want to search for a specific IP address within a list. You can use the in keyword is used to search for a specific IP address in a list:


ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]
search_ip = "192.168.1.3"
# Check if the IP address is in the list
ip_present = search_ip in ip_addresses
print(ip_present)  # Output: True

