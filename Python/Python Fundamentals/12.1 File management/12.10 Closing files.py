# 12.10 Closing a File
# In Python, closing a file can be done using the close() method. Here’s an example:

file = open('filename.txt', 'r')
# Perform file operations
file.close()


# In this code, 'filename.txt' should be replaced with the path to the file you want to open. 
# The file is opened for reading with the 'r' mode. 
# After performing the necessary file operations, the close() method is called to close the file.

# Closing files in Python is necessary for several reasons:

# It frees up system resources that were tied up with the file.
# It ensures that changes made to the file are saved.
# Some changes made to a file in Python may not be immediately written to disk; closing the file ensures that these changes are not lost.
# It prevents further modifications to the file. Once a file is closed, attempting to write to it will result in an error.

# Example:
# Consider a case where there’s a need to log network device status to a file and then close it:

import os

file = open('device_ip.txt', 'r')
device_ip = file.readline().strip()
file.close()

response = os.system("ping -c 1 " + device_ip)

file = open('log.txt', 'a')
if response == 0:
    file.write(device_ip + ' is up!\n')
else:
    file.write(device_ip + ' is down!\n')
file.close()

# In this code, 'device_ip.txt' is a file containing the IP address of the network device. 
# The script reads the IP address, pings the device, and then logs whether the device is up or down to the 'log.txt' file. 
# Please replace 'device_ip.txt' and 'log.txt' with the paths to your files. Note that this script should be run on a system where the ping command is available.
# The -c 1 option means that only one packet is sent. note : -c won't work on windows, need to use -n. -c works for linux/mac
# The '\n' at the end of the string is a newline character, which ensures that each log entry is on a new line.
#  After each file operation, the file is closed using the close() method.



# However, it’s worth noting that Python provides a more efficient way to handle opening and closing files using the with statement,
# which automatically closes the file once the nested block of code is completed.
# This is generally recommended as it’s more concise and eliminates the risk of forgetting to close the file, 
# which could lead to the issues mentioned above. Here’s how the above code would look using the with statement:


import os

with open('device_ip.txt', 'r') as file:
    device_ip = file.readline().strip()

response = os.system("ping -c 1 " + device_ip)

with open('log.txt', 'a') as file:
    if response == 0:
        file.write(device_ip + ' is up!\n')
    else:
        file.write(device_ip + ' is down!\n')

# In this version of the code, there’s no need to call close() explicitly - it’s handled automatically by the with statement. 
# This is a more pythonic way to work with files and is generally preferred for its simplicity and effectiveness. 
# It’s especially useful in larger scripts or applications where managing the opening and closing of multiple files can become complex. 
# The with statement ensures that files are properly closed after they are no longer needed, which helps to prevent resource leaks and other potential issues