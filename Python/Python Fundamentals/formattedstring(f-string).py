item = "book"
quantity = 3
order_summary = f"You ordered {quantity} {item}s."
print(order_summary)

# Output: "You ordered 3 books."    f-strings are formatted strings, they are used to embed an expression within a string and look a bit cleaner.
#      Lowercase f is added before the string, while the
#  {}  brackets inside the expression point to the variables of the same name

#Another example below this done in zybooks lab 4.7.1 
octet1 = 192
octet2 = 168
octet3 = 1
octet4 = 100
# do not edit above this line
oct_convert_string = str(octet1) + str(octet2) + str(octet3) + str(octet4)
formatted_ip = f"{octet1}.{octet2}.{octet3}.{octet4}"
print(formatted_ip)

# Expected output
# 192.168.1.100
# All octets are first integer data types which must be converted to a string
# The conversion is done in line 16
# In line 17, a new variable formatted_ip is created, then all octet variables ared joined together and a . is appended
