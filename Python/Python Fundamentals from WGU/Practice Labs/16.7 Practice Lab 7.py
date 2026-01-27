# Modify this function.

# def line_count(filename):
#  f = Open(filename,'r') 
#  contents = f.read
#  lines = contents.split("\n")
#  f.close()
#  return len(line)

# After modification :
def line_count(filename):
    f = open(filename,'r') #changed spelling of open to be lowercase, added 'r' argument which means open in read mode
    contents = f.read()
    lines = contents.split("\n")
    total_lines = len(lines) #added this variable to hold the actual length of lines
    f.close()
    return total_lines #changed return line to the new total_lines variable, so it doesn't return the length of the filename itself 
                        # i.e "test.txt" total length is 8, not the actual file contents.
                        # Now it reads the total number of lines after being split.



# You may alter the code below to test your solution or print help documentation.
# Only the line_count function will be graded for this assessment.

print(line_count('test.txt')) # print won't work unless proper file exists and actual path is passed
# help(help)



# An existing function line_count is meant to open a text file, read the contents, and return the number of lines in the file. Several existing issues throw errors, and the function is not working as intended.

# Update the code within the Python function line_count. 
# The function should accept a string identifying the name of a text file, 
# read the contents of the text file, determine the number of lines in the text file, 
# and return the number of lines in the text file.
# For simplicity, assume each line except the last ends with a newline character.