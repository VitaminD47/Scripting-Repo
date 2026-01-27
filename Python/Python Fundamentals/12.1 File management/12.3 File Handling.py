# 12.3 File Handling
# Python provides several built-in functions for handling files, which are crucial in network automation for tasks such as reading configuration files or writing logs.
#  Here are some key functions:


# open(filename, mode): #Opens a file in the specified mode (‘r’ for read, ‘w’ for write, ‘a’ for append, ‘b’ for binary). Returns a file object.
# file.read([size]): #Reads at most size bytes from the file. If size is not specified, it reads the whole file.
# file.readline(): #Reads the next line of the file.
# file.readlines(): #Returns a list of all lines in a file.
# file.write(string): #Writes the string to the file and returns the number of characters written.
# file.close(): #Closes the file.
# Example:


# def log_network_activity(device_ip, username, password, log_file):
    # Connect to the network device 
    # (assuming a function connect_to_device is defined)
    # connection = connect_to_device(device_ip, username, password)
    
    # Get the network activity
    # activity = connection.get_activity()
    
    # Open the log file in append mode
    # file = open(log_file, 'a')
    
    # Write the activity to the file
    # file.write(activity)
    
    # Close the file
    # file.close()


#  In this example, a function log_network_activity is defined to log the activity of a network device. 
#  It connects to the device, gets the activity, and writes it to a log file. 
#  This is a simple illustration of how Python can be used for file handling in network automation.
#  It’s important to note that error handling and logging would typically be added for robustness.
#  Also, it’s recommended to use the with statement when working with files to ensure they are properly closed after use.
#  This can prevent resource leaks in larger applications.