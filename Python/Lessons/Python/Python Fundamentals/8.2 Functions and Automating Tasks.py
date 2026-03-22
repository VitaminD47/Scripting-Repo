# 8.2 Automating Tasks with Python
# Why Automate Tasks?
# Administrators often choose to automate tasks using Python for several compelling reasons:

# Efficiency and Time Savings
# Python allows administrators to automate repetitive tasks, saving valuable time and reducing the potential for manual errors.
#  Automated scripts can perform tasks much faster and consistently than manual intervention.

# Consistency
# Automation ensures consistency in task execution.
#  Scripts follow predefined logic, reducing the chances of human error and ensuring that tasks are carried out uniformly across systems.

# Scalability
# As the scale of IT environments grows, automation becomes essential.
#  Python's versatility makes it suitable for small-scale scripts as well as large-scale automation projects,
# providing a consistent approach across different-sized infrastructures.

# Task Complexity
# Python's rich ecosystem of libraries and modules simplifies handling complex tasks. 
# Administrators can leverage pre-built functions and libraries to address various challenges, from network configuration to data processing.

# Interoperability
# Python integrates well with different technologies and platforms, making it suitable for diverse IT environments. 
# It supports various protocols, APIs, and interfaces, allowing administrators to interact with and automate a wide range of systems and devices.

# Scripting and Automation APIs
# Python is a scripting language with powerful automation capabilities. 
# Many applications and systems expose APIs that Python scripts can interact with, enabling seamless integration and automation of various processes.

# Community Support
# Python boasts a large and active community of developers.
# This means administrators can find support, resources, and pre-existing scripts for common tasks, accelerating the development of automation solutions.

# Cost Savings
# Automation can lead to significant cost savings by reducing the need for manual labor, 
# minimizing errors that can lead to costly downtime, and optimizing resource utilization.

# Adaptability and Future-Proofing
# Python's popularity and open-source nature ensure its continued relevance.
#  Administrators can easily find resources to learn, adapt, and enhance their automation scripts over time, making them well-prepared for evolving IT landscapes.

# Documentation and Auditability
# Automated scripts can serve as documentation for procedures and tasks. 
# Additionally, the automated nature of these scripts facilitates auditing and tracking changes, ensuring accountability in system management.

# Overall, Python's simplicity, readability, and extensive ecosystem make it an ideal choice for administrators 
# looking to streamline and enhance their IT management processes through automation.







# Configuration Management


# Configuration management can be automated using Python by leveraging libraries and frameworks that 
# facilitate interactions with network devices, servers, or infrastructure components.


#  One popular tool for network automation and configuration management is Netmiko, a multi-vendor library for managing network devices.

# Example:
# Here's an example using Python and Netmiko to automate the configuration of a network device.
# In this case, let's consider configuring an interface on a Cisco router:

from netmiko import ConnectHandler

# Define the device parameters
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
     'password': 'password',
     'secret': 'enable_password',
}

# Connect to the device
net_connect = ConnectHandler(**device)
net_connect.enable()

# Define the configuration commands
interface_config = [
     'interface GigabitEthernet0/0',
     'ip address 192.168.2.1 255.255.255.0',
     'no shutdown',
     'exit',
 ]

# Send configuration commands to the device
output = net_connect.send_config_set(interface_config)

# Display the output
print(output)

# Disconnect from the device
net_connect.disconnect()



# In this example:
# The device dictionary contains information about the network device, such as its type, IP address, and login credentials.

# The script uses Netmiko to connect to the device (ConnectHandler), enable privileged exec mode, and define a list of configuration commands for a specific interface.

# The send_config_set method sends the configuration commands to the device, and the output is captured.

# The output is printed, displaying the results of the configuration commands.

# Finally, the script disconnects from the network device.


# This example showcases a basic configuration task, but Python scripts can be extended to automate more complex configuration management tasks,
# including the management of multiple devices, handling configuration templates, and incorporating error-handling mechanisms.

# Netmiko supports a variety of network devices, making it a versatile choice for configuration management in network automation.







##IMPORTANT NOTES ON OBJECTS/CLASSES FROM GPT##

#On line 80, ConnectHandler(**device) is not actually a function call, but instead a class that creates the object net_connect.
#The syntax is identical to a standard function call more commonly seen with built in functions.
# The "**" in **device unpacks the defined device dictionary and passes it as arguments to the ConnectHandler class.







# Task Scheduling Example


# Task scheduling in Python can be automated using the schedule library, which provides a simple interface for scheduling and running periodic tasks.
# Below is an example that demonstrates how to use the schedule library to schedule a Python function to run at specific intervals:

# First, you need to install the schedule library if you haven't already:

 #pip install schedule 

# Now, you can create a Python script with an example of task scheduling:

import schedule
import time

def my_task():
     print("Executing my_task at", time.strftime("%Y-%m-%d %H:%M:%S"))

# Schedule the task to run every 1 minute
schedule.every(1).minutes.do(my_task)

# Alternatively, you can schedule the task using a cron-like syntax
# schedule.every().hour.at(":30").do(my_task)

# Run the scheduler continuously
while True:
     schedule.run_pending()
     time.sleep(1)

# In this example:
# The schedule library is imported

# The my_task function is defined, which prints a message indicating when it's executed.

# The schedule.every(1).minutes.do(my_task) line schedules the my_task function to run every 1 minute.

# You can adjust the scheduling interval based on your needs.

# The script enters a loop (while True) where schedule.run_pending() checks if any scheduled tasks need to be executed and then sleeps for 1 second.

# This script demonstrates a simple recurring task, but the schedule library provides flexibility for more complex scheduling scenarios.

# You can schedule tasks based on various intervals, days of the week, or even using a cron-like syntax.

# Task scheduling is useful for automating periodic operations, such as data backups, system monitoring,
# or any other repetitive tasks in network automation or other domains.









# Cloud Automation
# Cloud automation using Python can be achieved through the use of cloud provider SDKs (Software Development Kits) or APIs (Application Programming Interfaces).
# Each major cloud provider (e.g., AWS, Azure, Google Cloud) offers SDKs that allow developers to interact with and automate cloud resources.
# Below is an example using the Boto3 library, which is the official Python SDK for Amazon Web Services (AWS).

# First, you need to install the Boto3 library if you haven't already:
# pip install boto3

# Now, you can create a Python script to automate a simple AWS task, such as creating an S3 bucket:

import boto3

# AWS credentials (replace with your own credentials)

aws_access_key = 'YOUR_ACCESS_KEY'
aws_secret_key = 'YOUR_SECRET_KEY'
region_name = 'us-east-1'

# Create an S3 client

s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region_name)

# Specify the bucket name
bucket_name = 'my-unique-bucket-name'

# Create an S3 bucket
try:
     response = s3.create_bucket(Bucket=bucket_name)
     print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
     print(f"Error creating bucket: {e}")

# In this example:
# Replace YOUR_ACCESS_KEY and YOUR_SECRET_KEY with your AWS access key and secret key.

# The script uses the Boto3 library to create an S3 client with the specified credentials and region.

# It specifies a unique bucket name and attempts to create an S3 bucket using s3.create_bucket().

# This is a basic example, and cloud automation can involve more complex tasks, such as provisioning virtual machines,
# configuring networking, or deploying serverless functions.

# The process is similar for other cloud providers; you would use their respective SDKs
# (e.g., google-cloud-sdk for Google Cloud or azure-mgmt-compute for Azure) and follow similar patterns for automation.

# Always ensure you securely manage your credentials,
# consider using environment variables or IAM roles where applicable,
# and follow best practices for security and compliance in cloud automation.



## RECAP NOTES FROM GPT ON 7/6/25 ##

# A brief recap of what we covered today:

# ✅ Netmiko Script (Cisco Example)
# from netmiko import ConnectHandler: Imports the ConnectHandler class.

# net_connect = ConnectHandler(**device): Creates an object using parameters from the device dictionary (via ** unpacking).

# .enable() and .send_config_set(): Are methods (functions) tied to the net_connect object.

# This is object-oriented programming: ConnectHandler is a class, and net_connect is an object.

# ✅ Object vs. Variable
# net_connect is both:

# A variable (holds something)

# An object (an instance of a class with methods and properties)

#✅ Library Use
# Libraries like Netmiko or boto3 must be imported at the top of the script (import ...) to use their classes/methods.

# These libraries are written by other developers, often software engineers or specialists in the area (like networking or cloud).

#✅ boto3 (AWS Example)
# import boto3: Brings in the AWS SDK for Python.

# boto3.client(): Built-in method to create a service client (like for S3).

# s3.create_bucket(): Method to create a bucket on AWS using that client.

# try/except block: Catches errors if the AWS call fails.


#✅ Miscellaneous
# **device: Double-asterisk unpacks a dictionary into keyword arguments.

# You usually run AWS-related scripts locally, and they interact with AWS remotely over the internet using your credentials.