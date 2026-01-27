# 12.7 Comma Separated Files : 
# Comma Separated Values (CSV) files are a type of text file commonly used to store tabular data. 
# Each line in the file represents a row in the table, and the values in each row are separated by commas.

# Python provides the csv module to read and write CSV files. Here’s how to work with CSV files in Python:

# Opening a File: Use the open() function with the filename and mode as arguments. The mode ‘r’ is for reading, and ‘w’ is for writing.

# Creating a CSV Reader or Writer: Use the csv.reader() or csv.writer() function to create a reader or writer object.

# Reading from a File: Use the next() function to read a row from the file. Each row is returned as a list of strings.

# Writing to a File: Use the writerow() function to write a row to the file. The row should be a list of strings.
# Example:

import csv

def read_device_info(device_file):
    # Open the file in read mode
    file = open(device_file, 'r')
    
    # Create a CSV reader
    reader = csv.reader(file)
    
    # Read the header row
    headers = next(reader)
    
    # Read the rest of the rows
    devices = [row for row in reader]
    
    # Close the file
    file.close()
    
    return headers, devices


# In this example, a function read_device_info is defined to read network device information from a CSV file. 
# The open() function opens the file, csv.reader() creates a CSV reader, next() reads the header row, and a list comprehension reads the rest of the rows.
# Finally, the close() method is used to close the file. 
# The headers and devices are then returned as lists of strings. 


# This function could be used in a network automation script to read device information from a file and use it to configure the devices.
# It’s important to note that error handling and logging would typically be added for robustness. 
# Also, it’s recommended to use the with statement when working with files to ensure they are properly closed after use. 
# This can prevent resource leaks in larger applications.





# 12.7.1 : Comma Separated Files


# Complete the function "csv_to_list()" to read the contents of a csv file,  
# append each row of the csv to either a header list or a list of value rows, 
# and return both the header list and list of value rows. 

# Only the lists returned by csv_to_list() will be graded for this assignment. 
# The function should work for any csv file passed to the function beyond the examples provided.



import csv

def csv_to_list(file_path):
    file_read = open(file_path, 'r')
    
    # Create CSV Reader object
    csv_reader = csv.reader(file_read)
    
    # Read header row
    header_row = next(csv_reader)

    # Read all remaining rows in csv file using a list comprehension. remember this is an embedded for loop that takes each value as a string, then returns it as a list
    all_rows = [row for row in csv_reader]

    # Close file
    file_read.close()

    return header_row, all_rows






# You may alter the code below to view your return value(s).
# Only the csv_to_list function will be graded for this assessment. #note this wont work as the file doesn't exist on my pc. working on that...
    # added file. 
    
    # Important note, python will throw this syntax error: 
    # "SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape"

    # If you pass a standard windows file path, it won't be interpreted correctly. There are a few options for this :
    # 1) Use / (forward slashes in the directory path)
    # 2) Type r in front of the string to have python interpret it as a raw string 
    # 3) Use the backslashes, but add an extra one i.e \\ for each backslash entry in the string


print(csv_to_list(r"C:\Users\David\OneDrive\Desktop\Script Repository\csv files\firewall_rules.csv"))
# Expected return:
#  (['Rule ID', 'Source IP', 'Destination IP', 'Protocol', 'Action'], 
# [['1', '192.168.1.100', '192.168.1.200', 'TCP', 'Allow'],
#  ['2', '192.168.2.0/24', 'Any', 'UDP', 'Deny'],
#  ['3', 'Any', '192.168.3.0/24', 'ICMP', 'Allow'], 
# ['4', '10.0.0.0/8', '192.168.1.0/24', 'TCP', 'Allow']])

# added newlines to separate each row in the returned list for easier readability