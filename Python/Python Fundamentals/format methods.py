name = "David"
age = 33
# Using format() method with placeholders. The {} represent placeholder variables that get passed to .format()
message = "My name is {} and I am {} years old.".format(name, age)
print(message)
# Output: "My name is John and I am 25 years old."

#below is my example. One thing to note is the format method, .format(), will automatically convert data types
cisco_switch_9300 = "Cisco 9300L is the model of the switch"
cisco_switch_ip = "10.20.30.101"
full_switch = "{} while the IP is {}.".format(cisco_switch_9300,cisco_switch_ip)
print(full_switch)


#Named arguments, also known as keyword arguments, 
#are arguments that are passed to a function or method by explicitly stating the name of the parameter and its value.
#This allows you to specify arguments in any order, regardless of the order in which they are defined in the function.

# Named arguments in format()

details = "Name: {name}, Age: {age}".format(age=30, name="Alice")
print(details)
# Output: "Name: Alice, Age: 30"


#Index-based formatting example below
#Index-based formatting is a feature of the str.format() method
#where you can specify the order in which values should be formatted
#This is done by placing index numbers (which start from 0) inside the curly braces {}
#that serve as placeholders in the original string.
# Index-based formatting
message = "{0} is a {1} programming language.".format("Python", "versatile")
print(message)
# Output: "Python is a versatile programming language."

#Number Formatting example
#In Python, number formatting is used to control how numbers are displayed. 
#This can be particularly useful when you want to display numbers in a more readable format or control the precision of floating point numbers.
value = 1234567.89
formatted_value = "Formatted Value: {:,.2f}".format(value)
print(formatted_value)
# Output: "Formatted Value: 1,234,567.89"


#Last example from lab 4.8.1. Here I went with the placeholder variation of .format. Could also use indexes i.e {0}, {1}, {2} and get the same output.
device = "laptop"
ip_address = "192.168.1.100"
# do not edit above this line
status = "defective"
status_check = "The {0} at {1} is {2}".format(device, ip_address, status)
print(status_check)

# Expected output
# The laptop at 192.168.1.100 is defective