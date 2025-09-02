# Off-by-One Errors
# These occur when a loop iterates one time too many or one time too few. 
# For example, if a loop should run 10 times but is set to run 11 times, it can lead to unexpected results.

for i in range(11):  # Should be range(10)
    print(i)



# This Python code is designed to print the numbers 0 - 5. Correct the code. # Fix is to set i < 6 so it prints 0-5 and doesn't stop at 4.
i = 0
while i < 5:
    print(i)
    i += 1 





# Incorrect Boolean Expressions
# These occur when the conditions in an if statement, while loop, or other Boolean expression are not correctly formulated.
# For example, using and instead of or can lead to unexpected results.

x = 4
if x > 0 or x < 5:  # Should be or
    print("x is outside the range 0-5")


# Code Editor 11.4.2: Practice It
# Correct the Python script. There may be multiple issues. # Only change made was to change the strings for the print statements.

x = 3
if x > 0 and x < 5:  
    print("x is inside the range 0-5")
else:
    print("x is outside the range 0-5")






# Misunderstanding of Python’s Order of Operations
# This can lead to unexpected results. For example, misunderstanding how Python’s order of operations works can lead to miscalculations.

result = 1 + 2 * 3  # Result is 7, not 9
print(result)


# Incorrect Use of Assignment Operator
# Using the assignment operator (=) instead of the equality operator (==) in a conditional statement can lead to unexpected results.

if x == 2:  # Should be ==
    print("x is 2")


# Code Editor 11.4.4: Practice It
# Correct the Python script. There may be multiple issues.

var_x = 20

if var_x == 10:
    print("x is 10")
elif var_x == 20:
    print("x is 20")
else:
    print("x is unknown")
    



# 11.4.1: Logic Errors


# The existing function "filter_list()" is intended to filter a numeric list to only include values from 0 to 255 (inclusive). 
# Additionally, the function includes a "limit" parameter allowing a user to identify the maximum number of values to be included within the filtered list.
# Correct the logic errors within the function to achieve the expected behavior.

# Only the set returned by filter_list() will be graded for this assignment. 
# The function should work for any list of integers and integer limit value passed to the function beyond the examples provided.

# Corrections made to line 87 by changing operator signs to <= from <, added an 'and' operator' and >= 0 instead of < 0.
# Correction made to line 90 to operator symbol < num_items to >= num_items. Verified outputs match as expected per print statements below.

def filter_list(input_list, num_items):
    filtered_list = []
    for entry in input_list:
        if entry <= 255 and entry >= 0:
            filtered_list.append(entry)
            if len(filtered_list) >= num_items:
                break
    return filtered_list


# You may alter the code below to view your return value(s).
# Only the filter_list function will be graded for this assessment.

numeric_list = [12, 255, 256, 45, 67, 500, 150, -1, 0]
# print(filter_list(numeric_list, 10))
# Expected return: [12, 255, 45, 67, 150, 0]

#print(filter_list(numeric_list, 3))
# Expected return: [12, 255, 45]