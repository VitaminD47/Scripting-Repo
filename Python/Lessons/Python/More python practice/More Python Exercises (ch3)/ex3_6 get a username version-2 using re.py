import re

name = input("Enter your name: ")
while True:
    while not re.match("^[a-zA-Z]+$", name):
        name = input("Enter your name: ")
    else:
        print(name)
        exit()


# this uses regular expression module. ^[a-zA-Z]+$ means any character starting with a letter with one or more characters
# and ending with a letter. It will not accept numbers or special characters. If the condition in the while loop isn't met, the name prompt will keep being asked.
# once it's provided, the else block will execute and print the name