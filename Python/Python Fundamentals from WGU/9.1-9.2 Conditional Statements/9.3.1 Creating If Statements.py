# Lab 9.3.1

# A valid IPv4 address contains four octets separated by a period.
#  Each octet should contain a numeric value between 0 and 255 (inclusive). 
# Complete the function "is_valid_ipv4()". The function should accept a string representing a possible IPv4 address. 
# Use conditional logic within if/else statements to determine if the possible IPv4 address is valid, returning a Boolean value.

# Only the Boolean value returned by is_valid_ipv4() will be graded for this assignment.
# The function should work for any string passed to the function beyond the examples provided.

# always use .split() to split IP addresses. 


def is_valid_ipv4(ip_address):
    split_ip = ip_address.split(".")
    if len(split_ip) != 4:
        return False
    elif not 0 <= int(split_ip[0]) <= 255:
        return False
    elif not 0<= int(split_ip[1]) <= 255:
        return False
    elif not 0<= int(split_ip[2]) <= 255:
        return False
    elif not 0<= int(split_ip[3]) <= 255:
        return False
    else:
        return True
    
ip_address = "10.200.1.2.3.4"
print(is_valid_ipv4(ip_address))

# You may alter the code below to view your return value(s).
# Only the is_valid_ipv4 function will be graded for this assessment.

# valid
#print(is_valid_ipv4("192.168.1.1"))

# not valid
#print(is_valid_ipv4("255.ABC.450"))


# My explanation to GPT of what's happening in the whole function :

# First we define a variable called is_valid_ipv4 that accepts one input. 
# Then we define a variable called split_ip where we perform a split on the input using a dot as the separator.
# We then have our first condition, which is an if statement that checks the length of that split to make sure that it's equaling 4.
#  If it does not equal 4, then we return false and the branch will end. 
# The next thing is we have a series of elif statements that check to make sure that the provided input, which in this case would be split_ip,
# is an integer number within the range of 0 and 255. This continues until we get to the last index, which is 3. 
# Then if any of those are false, the branch will end and return a false Boolean value. 
# Otherwise, our final else statement will execute and just simply return true.