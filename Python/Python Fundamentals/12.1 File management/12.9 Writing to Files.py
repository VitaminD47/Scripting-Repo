# Writing to an Existing File
# In Python, writing to an existing file can be done using the built-in open() function with the 'a' or 'w' mode. 
# The 'a' mode appends to the end of the file, while the 'w' mode overwrites the file. Here’s an example:

with open('filename.txt', 'a') as file:
    file.write('New line to append\n')


# In this code, 'filename.txt' should be replaced with the path to the file you want to write to. 
# The string 'New line to append\n' is the content to be written to the file.

# Example:
# Consider a case where there’s a need to log network device status to a file:

import os

with open('device_ip.txt', 'r') as file:
    device_ip = file.readline().strip()

response = os.system("ping -c 1 " + device_ip)

with open('log.txt', 'a') as file:
    if response == 0:
        file.write(device_ip + ' is up!\n')
    else:
        file.write(device_ip + ' is down!\n')


# In this code, 'device_ip.txt' is a file containing the IP address of the network device. 
# The script reads the IP address, pings the device, and then logs whether the device is up or down to the 'log.txt' file. 
# Please replace 'device_ip.txt' and 'log.txt' with the paths to your files. 
# Note that this script should be run on a system where the ping command is available. 
# The -c 1 option means that only one packet is sent. 
# The '\n' at the end of the string is a newline character, which ensures that each log entry is on a new line.








# Creating a New File
# In Python, creating a new file can be done using the built-in open() function with the 'x', 'a', or 'w' mode. Here’s how each mode works:

# 'x': Creates a new file and opens it for writing. If the file already exists, the operation fails.
# 'a': Opens the file for writing, appending to the end of the file if it exists.
# 'w': Opens the file for writing. If the file exists, it is truncated. If the file does not exist, it is created.
# Here’s an example of creating a new file with each mode:



# 'x' mode
try:
    with open('newfile_x.txt', 'x') as file:
        file.write('Content for the new file\n')
except FileExistsError:
    print('File already exists.')

# 'a' mode
with open('newfile_a.txt', 'a') as file:
    file.write('Content for the new file\n')

# 'w' mode
with open('newfile_w.txt', 'w') as file:
    file.write('Content for the new file\n')



# Example:
# Consider a case where there’s a need to log network device status to a new file:

import os

with open(r'C:\Users\David\OneDrive\Desktop\Script Repository\Python\12.1 File management\device_ip.txt', 'r') as file:
    device_ip = file.readline().strip()

response = os.system("ping -n 1 " + device_ip)

try:
    with open('new_log.txt', 'x') as file:
        if response == 0:
            file.write(device_ip + ' is up!\n')
        else:
            file.write(device_ip + ' is down!\n')
except FileExistsError:
    print('Log file already exists.')


    #verified that this code block works, just need to comment out all above blocks. 


# In this code, 'device_ip.txt' is a file containing the IP address of the network device. 
# The script reads the IP address, pings the device, and then logs whether the device is up or down to the 'new_log.txt' file.

# Please replace 'device_ip.txt' and 'new_log.txt' with the paths to your files. 
# Note that this script should be run on a system where the ping command is available. 

# The -c 1 option means that only one packet is sent. The '\n' at the end of the string is a newline character, which ensures that each log entry is on a new line.
# If the log file already exists, a message is printed instead of raising an error. 

# This is done using a try-except block to catch the FileExistsError exception. 
# This exception is raised when a file operation like creation or renaming fails because the target file already exists. This is specific to the 'x' mode. 



# The 'a' and 'w' modes do not raise this exception because they are designed to work with existing files. 
# The 'a' mode appends to the file and the 'w' mode truncates the file before writing.
# If the file does not exist, both modes will create it. 
# The 'x' mode, on the other hand, will only create a file if it does not already exist.


# If the file does exist, the 'x' mode will raise a FileExistsError exception. 
# This makes the 'x' mode useful when you need to ensure that you are not overwriting an existing file.
# In the network automation example, the 'x' mode is used to create a new log file. 
# If the log file already exists, the script prints a message and does not overwrite the existing log file. 

# This is useful in scenarios where you want to preserve existing log files and avoid accidentally overwriting them.
# However, if you want to append to the log file instead of creating a new one each time, you can use the 'a' mode. 
# If you want to overwrite the log file each time, you can use the 'w' mode. 


# The choice of mode depends on the specific requirements of your network automation task. 

# It’s also worth noting that the os.system() function is used to execute the ping command in the script.
# This function takes a string containing a shell command and executes it. The return value is the exit status of the command. 

# For the ping command, an exit status of 0 means that the ping was successful, while any other value means that the ping failed. 
# This is used in the script to determine whether the network device is up or down. 

# The result is then written to the log file. 
# The os.system() function is a simple way to execute shell commands from a Python script, but it has some limitations and potential security issues.

# For more complex or secure network automation tasks,
# you might want to use a more powerful and secure method of executing shell commands, such as the subprocess module in Python.

# The subprocess module provides more control over how the command is executed and how its output is handled.
# It also avoids some of the security issues with os.system(). However, for simple tasks like the one in the example, os.system() is often sufficient.