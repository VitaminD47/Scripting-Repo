# A list of float values measuring the percentage of CPU usage for servers has been collected. Servers with CPU usage greater than 90% should be flagged.

# Complete the Python function identify_high_cpu. 
# The function should accept a list of floats representing the percentage of CPU usage for servers,
#  determine which servers have higher than 90% CPU usage, and return the list of high-usage servers by index value.



def identify_high_cpu(cpu_list):
    high_usage = []
    for i,cpu in enumerate(cpu_list):
        if cpu > 90.0:
            high_usage.append((i))
            
    return high_usage
        
# remember we can use multiple variables in a for loop. however in this case we only wanted to add one to the new list which is i. i represents the index here.
# the enumerate function will give us the index and value, but we purposely omit the actual value and just keep the index when calling the .append method
    
# You may alter the code below to test your solution or print help documentation.
# Only the identify_high_cpu function will be graded for this assessment.

cpu_list = [85.0, 92.5, 88.0, 95.2]
print(identify_high_cpu(cpu_list))
# help(help)