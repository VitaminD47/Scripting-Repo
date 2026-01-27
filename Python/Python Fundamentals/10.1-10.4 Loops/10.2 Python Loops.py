
#What Are Loops?
#Python loops are control flow structures used to repeatedly execute a block of code. There are two types of loops in Python: for and while.

# A for loop is used to iterate over a sequence (like a list, tuple, dictionary, string, or range) or other iterable object.
# A while loop is used to repeatedly execute a block of code as long as a certain condition is True.



# Loops are used when there’s a need to perform a task multiple times, such as processing items in a list one by one or
# running a block of code until a certain condition is met.

# Example:
subnet = "192.168.1."
ip_addresses = [subnet + str(i) for i in range(1, 256)]

for ip in ip_addresses:
    print(ip)


# This script generates a list of all possible IP addresses in the 192.168.1.0/24 subnet and then prints each IP address.


#Lab 10.2.1 on Loops :

# Complete the function "generate_users()" to generate sequentially numbered usernames starting at 1 until an indicated end value. 
# The function should accept a string and a numeric value, generate usernames beginning with 
# the string and ending with increasing numeric values (e.g., "test_account1", "test_account2", "test_account3"), 
# returning the usernames as a set to preserve uniqueness. 


# This worked well : 

def generate_users(username_string, num_accounts):
   username_string = [username_string + str(i) for i in range(1,num_accounts + 1)] 
   
   for name in username_string:
    return set(username_string)





username_list =  "gta"
print(generate_users(username_list, 40))



# You may alter the code below to view your return value(s).
# Only the generate_users function will be graded for this assessment.

#print(generate_users("test_account", 4))