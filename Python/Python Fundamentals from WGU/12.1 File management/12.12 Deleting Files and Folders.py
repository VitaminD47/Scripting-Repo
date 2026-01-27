# 12.12 Deleting Files and Folders

# In Python, deleting a file can be done using the remove() function from the os module. Here’s an example:

import os

# Specify the file path
file_path = 'filename.txt'

# Check if the file exists
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
else:
    print('The file does not exist.')


# In this code, 'filename.txt' should be replaced with the path to the file you want to delete.
# The os.path.exists() function is used to check if the file exists before attempting to delete it.
# This prevents an error if the file does not exist.




# Another Example:
# Consider a case where there’s a need to delete a log file after it has been processed:

import os

# Specify the file path
log_file_path = 'log.txt'

# Check if the log file exists
if os.path.exists(log_file_path):
    # Delete the log file
    os.remove(log_file_path)
else:
    print("can't find file.")

    # In this code, 'log.txt' is a file containing logs from network devices. The script checks if the log file exists, and if it does, deletes it. 
    # Please replace 'log.txt' with the path to your log file. 

    # This could be useful in a scenario where the log file is processed and the data is stored elsewhere, so the original log file is no longer needed.
    # As always, be careful when deleting files, as this operation cannot be undone. 

    # It is good practice to always check if a file exists before attempting to delete it, as shown in the examples above.

    # This can prevent errors and make your code more robust. 
    # It’s also worth noting that the os module provides many other useful functions for working with files and directories,
    # such as os.rename() for renaming files and os.rmdir() for removing directories. 




    # Deleting a Folder :
# In Python, deleting a folder can be done using the rmdir() function from the os module. Here’s an example:

import os

# Specify the folder path
folder_path = ('deleteme')

# Check if the folder exists
if os.path.exists(folder_path):
    # Delete the folder
    os.rmdir(folder_path)
else:
    print('The folder does not exist.')
 

# In this code, 'foldername' should be replaced with the path to the folder you want to delete. 
# The os.path.exists() function is used to check if the folder exists before attempting to delete it. 
# This prevents an error if the folder does not exist.



# Example:
# Consider a case where there’s a need to delete a folder containing logs for a network device after they have been processed:

import os

# Specify the folder path
log_folder_path = 'logs'

# Check if the log folder exists
if os.path.exists(log_folder_path):
    # Delete the log folder
    os.rmdir(log_folder_path)
else:
    print('The log folder does not exist.')


# In this code, 'logs' is a folder containing logs from network devices. 
# The script checks if the log folder exists and, if it does, deletes it. Please replace 'logs' with the path to your log folder. 

# This could be useful in a scenario where the log files are processed and the data is stored elsewhere, so the original log folder is no longer needed.
# As always, be careful when deleting folders, as this operation cannot be undone. 

# It is good practice to always check if a folder exists before attempting to delete it, as shown in the examples above.
# This can prevent errors and make your code more robust. Note that the os.rmdir() function can only remove empty directories.



# If the directory is not empty, you will get an error. To remove a directory that is not empty, you can use the shutil.rmtree() function instead. 

# This function removes a directory and all its contents. 
# However, use this function with caution, as it deletes everything in the directory without asking for confirmation. 

