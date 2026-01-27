# problem types to review : dictreader and writer objects, as well as datetime
# I ran out of time here and forgot how to put these together these problems
#one problem wanted me to raise an exception if the .csv file was not found i.e if filename was not 'config.csv'
# review how to read .csv files
# remember objects need to be made first
# I kept trying to return it but was only getting the object's memory value

# 29AUG25 Note:
# review read/write of .csv objects as well as try/except blocks. 
# review how to replace values in a list [] based on conditions
# review date time object creation and modification





# review how to change the values in a list within a for loop
# the problem was to create a network device toggler and reassign or flip values of "disabled" to "enabled" and vice versa
# spent a long time on this and could not get it to work
# first I tried removing each instance, then appending to a new list
# the .remove() method only removes one instance of the item, even when trying to loop
# then I tried using if statements i.e :
# if stat in status_list == "enabled":
#   stat = "disabled"
# if stat in status_list == "disabled":
#   stat = "enabled"

# could not get this to work even after double checking available methods with help() function

#2 Consider the below code : 

ip_addresses_string = "192.168.1.1, 192.168.1.2, 192.168.1.3, 192.168.1.4"
ip_list = [ip.strip()for ip in ip_addresses_string.split(',')]
converted = [[int(octet) for octet in ip.split('.')] for ip in ip_list]
#converted_flat = [int(octet) for ip in ip_list for octet in ip.split('.')]

print(ip_addresses_string)
print(ip_list)
print(converted)
#print(converted_flat)

#ip1_bin = ''.join([format(int(x), '08b') for x in ip1.split('.')])
#convert_test = int(stringer)
#converted = [int(octet) for octet in splitter]
#stringer = [str(ip)for ip in splitter]




# Example: Using list constructor in network automation
device_names_string = "router1,switch1,firewall1,router2,switch2"

# Convert comma-separated string to a list
device_names_list = list(device_names_string.split(",") )



# Resulting list
#print(device_names_list)

