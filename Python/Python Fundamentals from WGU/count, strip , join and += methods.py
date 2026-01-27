# What does count() do? It counts the number of occurences in a substring given a string. example below
string_test = [1,2,3,4,5,5,6]
string_test.count(5)
count = string_test.count(5)
print(count) # print here should be 2, as in 2 instances of 5. Note I had to define count, in reg terminal it would just evaluate on it's own without defining count.

# (strip) method will remove leading and trailing whitespaces from a string

# += operator is shorthand for string concatenation and assignment
# example below
greeting = "Hello"
greeting += ", world!"
print(greeting)

# This is easier than the alternative, which would be greeting = greeting + ", world!"

#another example right here :
msg = ""
msg += "Device: R1\n"
msg += "Status: Online\n"
msg += "IP: 192.168.1.1\n"
msg += "Type: Cisco"
print(msg)


# the .join() method will join strings from an iterable such as a list

example_list = ["learning ", "python ", "is ", "sick"]
joined_list = "".join(example_list)
print(joined_list)

#join needs "" at a minimum to act as a glue of sorts. if you put "," the string gets joined with commas, if you do "\n" it'll do a newline for every string item