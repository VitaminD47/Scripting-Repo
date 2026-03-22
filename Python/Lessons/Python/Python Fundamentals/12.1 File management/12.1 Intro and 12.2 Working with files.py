#12.2 Working with Files :
#Working with files is a necessary skill because network devices interact with files such as:

# Configuration files
# Configuration templates
# Files containing connection options
# Other script files 
# Python is a popular choice for file automation in network automation due to several reasons:

# Readability: Python’s clear and readable syntax makes it easy to write scripts for file automation.
# Standard Library: Python’s extensive standard library includes modules for file manipulation, such as os and shutil.
# Third-Party Libraries: Libraries like paramiko for SSH connections and netmiko for network device automation extend Python’s capabilities.
# Cross-Platform Compatibility: Python scripts can run on various operating systems, making it ideal for network environments with diverse hardware.

# Example:
import paramiko

def automate_config(device_ip, username, password, config_file):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Connect to the network device
    ssh.connect(device_ip, username=username, password=password)
    
    # Open the configuration file
    with open(config_file, 'r') as file:
        commands = file.read().splitlines()
    
    # Execute each command
    for command in commands:
        ssh.exec_command(command)
    
    # Close the connection
    ssh.close()
  

# In this example, a function automate_config is defined to automate the process of configuring a network device. 
# It takes the IP address of the device, the username and password for authentication, and a file containing the configuration commands as inputs. 
# The function reads the commands from the file and executes them on the network device via SSH. 
# This is a simple illustration of how Python can be used for file automation in network automation. 
# It’s important to note that error handling and logging would typically be added for robustness.



# Attributions and References
# Working with files. Python for network engineers. (2023, May 31). https://pyneng.readthedocs.io/en/latest/book/07_files/index.html

