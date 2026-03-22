# 12.6 Binary Files - 
# Working with binary files in Python involves similar steps as with text files, but the mode parameter to the open() function includes ‘b’ for binary:

# Opening a File: Use the open() function with the filename and mode as arguments. The mode ‘rb’ is for reading in binary mode, and ‘wb’ is for writing in binary mode.
# Reading from a File: The read() method reads the entire file and returns the bytes.
# Writing to a File: The write() method writes bytes to the file.
# Closing a File: The close() method closes the file, freeing up system resources.
# Example:
def read_firmware_image(firmware_file):
    # Open the file in binary read mode
    file = open(firmware_file, 'rb')
    
    # Read the entire file
    firmware_data = file.read()
    
    # Close the file
    file.close()
    
    return firmware_data


# In this example, a function read_firmware_image is defined to read a firmware image from a binary file.
# The open() function opens the file in binary read mode, read() reads the entire file into a bytes object, and close() closes the file.

# The firmware data is then returned as a bytes object.
# This function could be used in a network automation script to read a firmware image from a file and upload it to network devices.

# It’s important to note that error handling and logging would typically be added for robustness.
# Also, it’s recommended to use the with statement when working with files to ensure they are properly closed after use.
# This can prevent resource leaks in larger applications.