#A while loop in Python is a control flow structure that repeatedly executes a block of code as long as a certain condition is True.

#Example:
subnet = "192.168.1."
ip_addresses = []
i = 1

while i < 256:
    ip_addresses.append(subnet + str(i))
    i += 1

for ip in ip_addresses:
    print(ip) 


#This script generates a list of all possible IP addresses in the 192.168.1.0/24 subnet and then prints each IP address.


 # Incrementing in a while Loop
 # The increment in a while loop is a step that increases a counter variable.
 # It’s necessary to prevent the loop from running indefinitely, ensuring that the loop condition eventually becomes False, thus terminating the loop.
 # Here’s an example:

i = 0
while i < 5:
    print(i)
    i += 1  # Increment








# The break Statement
# The break statement in Python is used to exit a loop prematurely. It’s used when there’s a need to stop the loop even if the loop’s condition has not become False.

# Example:
subnet = "192.168.1."
ip_addresses = []
i = 0

while True:
    if i > 255:
        break
    ip_addresses.append(subnet + str(i))
    i += 1

for ip in ip_addresses:
    print(ip)
 

# This script generates a list of all possible IP addresses in the 192.168.1.0/24 subnet and then prints each IP address.
# The break statement is used to exit the loop once all IP addresses are printed.








# continue Statement
# The continue statement in Python is used in loops to skip the rest of the current iteration and move directly to the next one.

#Example:
subnet = "192.168.1."
ip_addresses = []
i = 0

while i < 256:
    i += 1
    if i == 100:  # Let's say we want to skip this IP
        continue
    ip_addresses.append(subnet + str(i))

for ip in ip_addresses:
    print(ip)


# This script generates a list of all possible IP addresses in the 192.168.1.0/24 subnet, skipping the IP address 192.168.1.100, and then prints each IP address. 
# The continue statement is used to skip the current iteration of the loop and proceed to the next one when i equals 100.





# else Statement 
    

# The else statement in a Python while loop specifies a block of code to be executed when the loop condition becomes False. 
# The else block executes after the loop finishes, but not if the loop is exited prematurely with a break statement.



# 10.3.1 While Loops Lab

# Complete the function remove_admin() to remove admin usernames from a list through the first n usernames.

# 1) Admin usernames begin with "admin" as the first 5 characters. The function should accept a list of usernames and a numeric value representing a limit. *Done*

# 2)Remove any admin usernames from the list based on the limit value.

#  For example, remove_admin(username_list, 5) would remove admin usernames from the first 5 entries in the username_list. 

#  3) Return the username list with admin accounts now removed with "validated" added as the last entry. Additionally, return the number of admin accounts removed.

# This was my final version, with assistance.

def remove_admin(usernames, limit):
    i = 0
    validated = []
    admin_count = 0

    while i < limit and i < len(usernames):
        if usernames[i][:5] == "admin":
            usernames.pop(i)
            admin_count += 1
            
        else:
                validated.append(usernames[i])
                i += 1

    validated.append("validated")


    
    return validated, admin_count



    # remove "admin" usernames based on limit
    # return validated list with appended "validated" entry
    # return count of removed admin usernames   


# You may alter the code below to view your return value(s).
# Only the generate_users function will be graded for this assessment.

usernames = ['FN84', 'adminPD66', 'OP83', 'IT32', 'OP27', 'OP13', 'IT95', 'adminHR73', 'OP12', 'HR31']
print(remove_admin(usernames, 10))

# Expected return 
# (['FN84', 'OP83', 'IT32', 'OP27', 'OP13', 'IT95', 'OP12', 'HR31', 'validated'], 2)