# this is example that shows how to filter/manipulate the following string without using regex (re) module


# goal is to turn remove colons, convert to all capital letters, split at the whitespace and add them to list. 
# then remove whitespaces using the strip() method and make an updated list.
# use len() to identify names and MAC addresses based on length of lists items. If item has 14 chars, it's a switch name so add to sw list.
# If 12, MAC address so add to MAC list. During the MAC appending add ****** to replace second half of MAC (asterisks).

sw_mac = '''pynetauto-sw01 84:3d:c6:05:09:11 pynetauto-sw17 80:7f:f8:80:71:1b pynetauto-sw05 f0:62:81:5a:53:cd'''

sw_mac = sw_mac.replace(":","").upper() # step 1
print(sw_mac) # Output should look like : PYNETAUTO-SW01 843DC6050911 PYNETAUTO-SW17 807FF880711B PYNETAUTO-SW05 F062815A53CD

list1 =sw_mac.split(" ") # step 2
print(list1) # This turns into list and separates sw and mac strings. 
           # Output is : ['PYNETAUTO-SW01', '843DC6050911', 'PYNETAUTO-SW17', '807FF880711B', 'PYNETAUTO-SW05', 'F062815A53CD']

list2 = [(i.strip()) for i in list1] # list comprehension, this removes trailing spaces. remember .append doesn't work in list comprehension.
print(list2)

sw_list = []
mac_list = []
for i in list2:  # using a for loop to build out two more lists based on length conditions
    if len(i) == 14:
        sw_list.append(i)
    if len(i) == 12:
        i = i[:6] + "******"
        mac_list.append(i)

print(sw_list)
print(mac_list)

sw_mac_dict = dict(zip(sw_list,mac_list)) #converting both lists to a dictionary (key, value pair)
for k,v in sw_mac_dict.items():
    print(k,v)