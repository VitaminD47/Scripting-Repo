# This is a python string slicer example, where the first four of the user input get capitalized (per [:4] in message), 
# and the remaining (from index 4 on) are lower case


message = input("Enter a phrase: ")
# do not edit above this line
first_four = message[:4:2].upper()
remaining = message[4::2].lower()
print(first_four + remaining)


# Expected output for "Modern Networking"
# MODErn networking
# note : the default value for step is 1. Step refers to the spacing between indexes step is the last character in the [] sequence. 
# the first value in the sequence is from, the second is to, and last is step. e.g [:4] would indicate going up to the first 4 indexes. [2:] would start FROM 2n
# You can also reverse the output of a string with [::-1], because it reads the indexes from last to first