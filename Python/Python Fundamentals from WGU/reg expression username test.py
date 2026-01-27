import re
def validate_username(username):
    if not re.match(r'^\w+$', username):
        raise ValueError("Username can only contain letters, numbers, and underscores")
    else:
        print("Username is valid!")
    

validate_username("Flamingo*")



## This is a function that uses the re, regular expression, module and then defines a function to check input matches the conditions on line 3. If it doesn't,
# A value error is raised. Otherwise (the else statement), it'll say the username is valid.

# Per GPT, the regular expression pattern is explained as this : 


# re.match(pattern, string)	Tries to match the pattern at the very start of string. It returns a match object if it succeeds, or None if it fails.

# r'^\w+$'	A raw regular-expression pattern:

#  ^ → start of the string

#  \w → any “word” character ([A-Za-z0-9_])  can be numbers or any letters or underscores but not special characters

#  + → one or more of the preceding token

#  $ → end of the string

# Together this means “the entire string must be made up of one or more letters, digits, or underscores.”

# if not re.match(...):	If the pattern doesn’t match the whole username (i.e., re.match returned None), execute the next line.

# raise ValueError(...)	Immediately stop and raise an exception with the given message.