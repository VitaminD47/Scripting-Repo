# 12.13 Comparing Files:

# The filecmp module in Python is a utility for comparing files and directories. 

# It provides functions to compare files and directories, and to report detailed information about the differences.

#  Its primary use is in searching for duplicate files and in comparing directory trees.

# Here is an example of network automation using the filecmp module:

# Compare two configuration files
import filecmp

first_config = r'C:\Users\David\OneDrive\Desktop\Script Repository\Python\12.1 File management\switch_config1.txt'
second_config =r'C:\Users\David\OneDrive\Desktop\Script Repository\Python\12.1 File management\switch_config2.txt'

if filecmp.cmp(r'C:\Users\David\OneDrive\Desktop\Script Repository\Python\12.1 File management\switch_config1.txt', r'C:\Users\David\OneDrive\Desktop\Script Repository\Python\12.1 File management\switch_config2.txt'):
    print('The configuration files are the same. Contents of file below:')
    with open(r'C:\Users\David\OneDrive\Desktop\Script Repository\Python\12.1 File management\switch_config1.txt') as file:
        lines = file.readlines()
        print("".join(lines))
    
    

else:
    print('The configuration files are different. Inspect for differences below:')
    f1 = open(first_config, 'r')
    print(f1.read())
    f1.close()
    f2 = open(second_config, 'r')
    print(f2.read())
    f2.close()


# In this example, filecmp.cmp('/path/to/config1.txt', '/path/to/config2.txt') compares two configuration files. 
# If the files are the same, it prints ‘The configuration files are the same.’ If the files are different, it prints ‘The configuration files are different.’ 
# This can be useful in network automation tasks, such as checking if a network device’s configuration has changed. 

# Note that the filecmp module automatically handles the intricacies of file comparison,
# allowing network engineers to focus on the automation task at hand, rather than the details of file comparison.