# 12.11 Checking for File Existence :
# In Python, checking if a file exists can be done using the os.path.exists() function from the os module. 
# Here’s an example:


import os

# Specify the file path
file_path = 'filename.txt'

# default path for me is C:\Users\David\OneDrive\Desktop\Script Repository\Python>, 
# which means it doesn't have to be entered in the string above
# otherwise it would be the full path i.e C:\Users\David\OneDrive\Desktop\Script Repository\Python>\filename.txt

# Check if the file exists
if os.path.exists(file_path):
    print('The file exists.')
else:
    print('The file does not exist.')


# Another example : 

# Consider a case where there’s a need to check if a configuration file for a network device exists:

import os

# Specify the file path
config_file_path = 'config.txt'

# Check if the configuration file exists
if os.path.exists(config_file_path):
    print('The configuration file exists.')
else:
    print('The configuration file does not exist.')


# In this code, 'config.txt' is a file containing configuration data for a network device.
# The script checks if the configuration file exists. 
# Please replace 'config.txt' with the path to your configuration file.

# This could be useful in a scenario where the script needs to load configuration data from a file,
# and it needs to check if the file exists before attempting to read from it. 

# As always, it is good practice to check if a file exists before attempting to perform operations on it. 
# This can prevent errors and make your code more robust.

# It’s also worth noting that the os module provides many other useful functions for working with files and directories,
# such as os.remove() for deleting files and os.rename() for renaming files. 

