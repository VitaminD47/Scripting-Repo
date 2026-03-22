# 12.8 Reading Files
# Reading Parts of a File 
# In Python, it’s possible to read parts of a file using the read() method with a size argument, which specifies the number of bytes to read. If the size argument is not provided, the read() method reads the entire file.

# Example:
def read_part_of_log(log_file, size):
    # Open the file in read mode
    file = open(log_file, 'r')
    
    # Read the specified number of bytes
    part_of_log = file.read(size)
    
    # Close the file
    file.close()
    
    return part_of_log


# In this example, a function read_part_of_log is defined to read a specified number of bytes from a log file.
# The open() function opens the file, read(size) reads the specified number of bytes, and close() closes the file. 
# The part of the log is then returned as a string. 
# This function could be used in a network automation script to read parts of a log file for analysis or troubleshooting. 
# It’s important to note that error handling and logging would typically be added for robustness. 

# Also, it’s recommended to use the with statement when working with files to ensure they are properly closed after use. 

#example of the ''with'' usage here :

#with open("myfile.txt", "r") as f:
    data = f.read()
# f is automatically closed after this block


# example of creating and writing to a file :

#with open("sample2.txt", "w") as file:
 #   file.write("Hello, Python!\nThis file was created using the with statement.")


# Reading Lines in a File : 
# In Python, reading a single line from a file can be accomplished using the built-in open() function and the readline() method. 

# Here’s an example:

#with open('filename.txt', 'r') as file:
    first_line = file.readline()


# In this code, 'filename.txt' should be replaced with the path to the file you want to read from.
# The 'r' argument means the file is opened in read mode. 
# The readline() method reads a single line from the file.


# Example:
# Consider a case where there’s a need to read a network device IP address from a file and then ping it. 
# Here’s a simple example using the os module for the ping:


with open(r'C:\Users\David\OneDrive\Desktop\Script Repository\Python\12.1 File management\ping_defaultgateway.txt', 'w') as file:
          file.write("10.0.0.1")





import os

with open(r'C:\Users\David\OneDrive\Desktop\Script Repository\Python\12.1 File management\ping_defaultgateway.txt', 'r') as file:
    device_ip = file.readline().strip()  # strip() is used to remove the newline character at the end
    response = os.system("ping -n 1 " + device_ip)

    if response == 0:
        print(device_ip, 'is up!')
        
    else:
        print(device_ip, 'is down!')


# In this code, 'device_ip.txt' is a file containing the IP address of the network device.
# The script reads the IP address, pings the device, and then prints whether the device is up or down. 
# Please replace 'device_ip.txt' with the path to your file. 
# Note that this script should be run on a system where the 
# ping command is available. The -c 1 option means that only one packet is sent. Note -c only works for linux/mac, use -n for windows.



# Another method using the subprocess module can be used below :
#import subprocess

# device_ip = "10.0.0.16"  # Replace with your test IP

#result = subprocess.run(["ping", "-n", "1", device_ip], capture_output=True, text=True)

#if "TTL=" in result.stdout:
   # print(device_ip, "is up!")
#else:
   # print(device_ip, "is down!")
