#Padding and Alignment
# In Python, padding and alignment are used to format strings for better readability and presentation. Here’s a brief explanation:

#Padding: Padding refers to adding characters to a string to reach a certain length. This is often used for output formatting and alignment. 

#There are three common types of padding:

#Left Padding: Characters are added to the start of the string. 
#Right Padding: Characters are added to the end of the string. 
#Center Padding: Characters are added to both ends of the string until it reaches a specified length.
#Alignment: Alignment refers to the way text is positioned within a given space. In Python, you can align strings using the format() method with alignment operators:

# < : Forces the field to be left-aligned within the width.
# > : Forces the field to be right-aligned within the width.
# ^ : Forces the field to be centered within the width.#

# Padding and alignment example

text = "Python"
formatted_text = "{:^10}".format(text)
print(formatted_text)
# Output: "  Python  "