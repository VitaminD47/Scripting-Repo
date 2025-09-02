# Looping Through a String 
# Looping through a string in Python is straightforward due to Python’s built-in support for string iteration. Here’s the basic syntax:

#for character in string:
    # code to be executed


# In this structure, string is the string that needs to be iterated over, and character is the variable that takes the value of each character in the string for each iteration.

# Example:
ip_address = "192.168.1.1"
octets = ip_address.split(".")
octet_count = 0

for octet in octets:
    if octet.isdigit() and 0 <= int(octet) <= 255:
        octet_count += 1

print(f"The IP address {ip_address} has {octet_count} octets.")





# break Statement
# The break statement in Python is used to exit or “break” a for or while conditional loop.
# When the loop encounters the break statement, the control flow is immediately interrupted and the program proceeds to the next line of code outside the loop.

# This script splits the IP address string into octets using the dot as a separator, then iterates over each octet. 
# If the octet is not a number or not between 0 and 255 (inclusive), the script prints a message indicating that the IP address is not valid and breaks the loop. 
# If the loop completes without hitting the break statement, the script prints a message indicating that the IP address is valid.

# Example:
ip_address = "622.168.1.1"
octets = ip_address.split(".")

for octet in octets:
    if not octet.isdigit() or not 0 <= int(octet) <= 255:
        print(f"{ip_address} is not a valid IP address.")
        break
else:
    print(f"{ip_address} is a valid IP address.")


# continue Statement
# The continue statement in Python is used within a loop (for or while) to skip the rest of the current iteration and move directly to the next one.
#  When the continue statement is encountered, the program control jumps to the top of the loop, and the next iteration begins.

# Example:
ip_address = "192.168.1.1"
octets = ip_address.split(".")

for octet in octets:
    if not octet.isdigit() or not 0 <= int(octet) <= 255:
        print(f"{ip_address} is not a valid IP address.")
        continue
    print(f"Octet {octet} is valid.")






# range() Function
# The range() function in Python is used to generate a sequence of numbers within a given range.
# It’s commonly used in for loops when there’s a need to repeat an action a specific number of times.

# The syntax of the range function is as follows:

# range(start, stop, step)
# start: (Optional) An integer number specifying at which position to start. Default is 0.
# stop: An integer number specifying at which position to stop (not included).
# step: (Optional) An integer number specifying the incrementation. Default is 1.
# Example:
subnet = "192.168.1."
ip_addresses = [subnet + str(i) for i in range(1,256)]

for ip in ip_addresses:
    print(ip)


# This script generates a list of all possible IP addresses in the 192.168.1.0/24 subnet and then prints each IP address.


# else in for Loops
# The else statement in a Python for loop specifies a block of code to be executed when the loop has finished, i.e., 
# when all items in the sequence have been iterated over. 
# If the loop is exited prematurely with a break statement, the else block will not be executed.

# Here’s the syntax:

#for variable in iterable:
    # code to be executed
#else:
    # code to be executed after the loop has finished


# Example:
    device_list = ['Switch1', 'Router2', 'Firewall1']
search_device = 'Router2'

for device in device_list:
    if device == search_device:
        print('Device found:', device)
        break
else:
    print('Device not found:', search_device)


# In this script, the for loop iterates over the device_list. 
# If the search_device is found in the list, it prints a message and breaks the loop.
# If the loop finishes without finding the search_device (i.e., it wasn’t exited prematurely with a break), 
# the else statement is executed, and it prints that the device was not found. 






# pass Statement
#The pass statement in Python is a placeholder statement that is used when the syntax requires a statement, but no action needs to be taken. It is often used in places where code will eventually go, but has not been written yet.

# Here’s the syntax:

#for variable in iterable:
    # code to be executed
#    pass  # no action taken


# Example:
# Consider a task where one needs to iterate over a list of network devices, but doesn’t need to perform any action for certain devices. Here’s how a Python for loop with a pass statement can be used:

device_list = ['Switch1', 'Router2', 'Firewall1']

for device in device_list:
    if device == 'Router2':
        pass  # no action taken for 'Router2'
    else:
        print('Device:', device)


# In this script, the for loop iterates over the device_list. If the device is ‘Router2’, the pass statement is executed and no action is taken.
#  For all other devices, the device name is printed.




#10.4.1 Constructing For Loops lab :

# Company survey results include a department code, which has been stored in a list for counting responses by department.

# 1) Complete the function department_count() to count the number of entries per department, returning a dictionary of department counts and return a count of invalid entries.
#  
# The existing list department_codes lists all valid codes. 

# If an entry is not in department_codes and is not the value "TEST", the entry is invalid. # could add a 'continue' here?

# The returned dictionary should use the department code as the key and the count as the value.

# Only the department count dictionary and invalid count returned by department_count() will be graded for this assignment.
#  The function should work for any list of codes passed to the function beyond the examples provided.







def department_count(entries):
    department_codes = ["HRD", "ENG", "MKT", "FIN", "IT"]
    department_counts = {}
    invalid_count = 0

    for entry in entries:
        if entry =="TEST":
            continue
        elif entry in department_codes:
             department_counts[entry] = department_counts.get(entry, 0) + 1 # this was done to initialize department_counts with a value of 0 or else increment fails.
        else: 
            invalid_count += 1
            
            
            

        
    # count entries per department
    # return department_counts dictionary
    # return invalid_count, excluding "TEST" values
    
    return department_counts, invalid_count







# You may alter the code below to view your return value(s).
# Only the generate_users function will be graded for this assessment.

entries = ['HRD', 'MKT', 'HRD', 'IT', 'ENG', 'HRD', 'TEST', 'HRD', 'TEST', 'HRD', 'HRD', 'TEST', 'IT', 'TEST', 'HRD', 'TEST', 'IT', 'TEST', 'ENG', 'MKT', 'TEST', 'IT', 'IT', 'HRD', 'GUEST']
print(department_count(entries))

# Expected return
# ({'HRD': 7, 'MKT': 2, 'IT': 5, 'ENG': 2}, 1)