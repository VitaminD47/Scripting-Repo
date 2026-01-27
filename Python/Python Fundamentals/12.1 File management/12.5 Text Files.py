# 12.5 Text Files :
# Working with text files in Python involves several steps:

# Opening a File: Use the open() function with the filename and mode as arguments. The mode ‘r’ is for reading, ‘w’ for writing, and ‘a’ for appending.
# Reading from a File: The read() method reads the entire file, readline() reads a single line, and readlines() reads all lines into a list.
# Writing to a File: The write() method writes a string to the file.
# Closing a File: The close() method closes the file, freeing up system resources.
# Example:
def read_config_commands(config_file):
    # Open the file in read mode
    file = open(config_file, 'r')
    
    # Read all lines into a list
    commands = file.readlines()
    
    # Close the file
    file.close()
    
    # Remove newline characters
    commands = [command.strip() for command in commands]
    
    return commands


# In this example, a function read_config_commands is defined to read network configuration commands from a text file.
# The open() function opens the file, readlines() reads all lines into a list, and close() closes the file. 
# The commands are then cleaned up to remove newline characters and returned as a list. 
# This function could be used in a network automation script to read configuration commands from a file and apply them to network devices.
# It’s important to note that error handling and logging would typically be added for robustness.
# Also, it’s recommended to use the with statement when working with files to ensure they are properly closed after use.
#  This can prevent resource leaks in larger applications.







# 12.5.1 Lab : FORMATIVE | Text Files

# Complete the function "txt_to_list()" to read the contents of a text file, append each line of text to a list, and return the list of file contents. 
# Newline characters, whitespace, and other undesired trailing characters should be removed with ".strip()". 
# For example, `print("this is a string \n".strip())` outputs "this is a string".


def txt_to_list(file_path):
    file = open(file_path,'r')

    filetolist = file.readlines()

    file.close()
    
    filetolist = [newlines.strip() for newlines in filetolist]
    
    return filetolist















# You may alter the code below to view your return value(s).
# Only the txt_to_list function will be graded for this assessment.

print(txt_to_list("text-files/log.txt"))
# Expected return:
#  ['2024-01-28 10:15:32 - User login successful', 
# '2024-01-28 11:20:45 - Firewall rule updated', '2024-01-28 12:35:17 - Network switch rebooted',
#  '2024-01-28 13:40:22 - Server backup started', '2024-01-28 14:55:11 - VPN configuration changed',
#  '2024-01-28 15:10:39 - Intrusion detection system alerted', '2024-01-28 16:25:04 - Software update applied to routers']

# this is all one list, just used newlines for easier readability