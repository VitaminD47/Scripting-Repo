import re

def get_name():
    name = input("Enter your name: ")
    while True:
        while not re.match("^[a-zA-Z]+$", name):
            name = input("Enter your name: ")
        else:
            print(name)
            exit()
    
    
get_name()

#original file name : ex3_7 username version-3 using re with function
#filename changed due to ex 3_8 which demonstrates importing it as a module.

