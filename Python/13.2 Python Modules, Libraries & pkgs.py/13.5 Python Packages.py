# 13.5 Python Packages

# Listing installed Python packages can be done using pip, the Python package installer. 

# The command pip list is used in the command line interface, which returns a list of all installed packages along with their versions. 

# To check if a specific package is installed, pip show package_name can be used.

# If the package is installed, this command will display information about it. 
# If not, it will not return any output. These commands help manage and track the packages used in a Python environment.

# Installing a Package

# Python packages can be installed using pip, the Python package installer. 
# The command pip install package_name is used in the command line interface. 
# For instance, to install the netmiko package, which is commonly used in network automation, the command would be pip install netmiko. 

# It’s recommended to use a virtual environment to avoid conflicts between packages. 
# If the package is already installed, it can be upgraded using pip install --upgrade package_name. 
# Always ensure pip is upgraded to the latest version before installing packages.

# Using a Package
# To use a Python package, it must first be imported into the Python script using the import statement.
# Once imported, the functions, classes, or variables defined in the package can be accessed using the dot notation.

# Example:
# Consider the netmiko package, which is commonly used in network automation. Here’s an example of using it to establish an SSH connection to a Cisco device:

from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip':   '10.0.0.1',
    'username': 'admin',
    'password': 'password',
}

connection = ConnectHandler(**device)

output = connection.send_command('show ip int brief')
print(output)

connection.disconnect()
 

# In this script, the ConnectHandler class from the netmiko package is used to establish an SSH connection to a device. The send_command method is then used to send a command to the device and print the output. This demonstrates how a package can be used to perform network automation tasks. Note that actual device IP, username, and password should be replaced with real ones when running this script.

# Removing a Package

# Python packages can be removed using pip, the Python package installer. 
# The command pip uninstall package_name is used in the command line interface. 

# For instance, to uninstall the netmiko package, which is commonly used in network automation, the command would be pip uninstall netmiko. 
# This command will ask for confirmation before proceeding with the uninstallation. 
# To skip the confirmation, use the -y option: pip uninstall -y package_name. 

# Always ensure pip is upgraded to the latest version before uninstalling packages. 
# Note that uninstalling a package will remove it from the system, and it will no longer be available for import in Python scripts.
