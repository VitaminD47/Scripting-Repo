#
# 1)What type of Python programming error is described by the scenario?

# A Python program is expected to read and process data from a file. However, the program crashes during execution because the file it’s trying to read does not exist.

# Answer) Runtime error.

# Runtime errors occur during the execution of a program, often caused by operations that are mathematically illegal or 
# by attempting to access a resource that isn’t available, such as reading a file that doesn’t exist. 
# The scenario described is a runtime error because the program crashes during execution due to trying to read a non-existent file


# 2) In the Python debugging process, what is the purpose of the pdb tool?

# Answer) To step through the code line by line, inspect variables, and set breakpoints at specific lines of code

# The pdb tool in Python is a built-in debugger that allows stepping through the code line by line,
# inspecting variables, and setting breakpoints at specific lines of code.



# 3) Which Python debugging technique would be most useful for identifying bottlenecks in the code that may be causing performance issues?


# Answer ) Profiling

# For performance issues, Python’s cProfile module can help identify bottlenecks in the code.
# This makes profiling the most suitable technique among the options for identifying performance bottlenecks.



# 4) A developer writes a Python program in an IDE. The program compiles and runs without crashing, but the output is not what the developer expected.
#  What type of error is this?

# Answer ) Semantic error. 

# Semantic errors occur when the code compiles and runs without crashing, but it doesn’t produce the expected results.
# This could be due to logic errors in the code. 
# The scenario described is a semantic error because the program runs without crashing, but the output is not as expected.



# 5) Which Python debugging tool is best suited for identifying potential issues in the code that might lead to errors?

# Answer ) Linters

# Linters, such as pylint and flake8, are tools that can catch potential issues in the code that might lead to errors. 
# They analyze the code for potential errors and deviations from coding standards.




# 6 ) Which Python code snippet will result in a syntax error?

# Answer ) for i in range(5)
#               print(i)

# This code snippet will result in a syntax error because it is missing a colon at the end of the `for` statement. 
# In Python, colons are used to start a new block of code (like after defining a function or starting a loop).
# Forgetting to include a colon can lead to a syntax error.




# 7) A developer writes a Python program that includes a loop. 
# The loop is intended to run 5 times, but the developer mistakenly sets it to run 6 times. What type of Python error is this?

# Answer) Off-by-one error. 

#Off-by-one errors occur when a loop iterates one time too many or one time too few. 
# In the scenario described, the loop is intended to run 5 times, 
# but the developer mistakenly sets it to run 6 times, which is an off-by-one error.




# 8) A developer writes a Python program that includes a conditional statement.
# The developer intends to check if a variable x is equal to 2, but mistakenly uses the assignment operator (=) instead of the equality operator (==).
# What type of branching error is this?

# Answer) Incorrect use of the assignment operator occurs when the assignment operator (=) is used instead of the equality operator (==) in a conditional statement.




# 9) In Python programming, which scenario is an example of a “Modifying a List While Iterating Over It” error?


# Answer) A loop that modifies the list it is iterating over, causing it to skip elements or go out of range

# This scenario accurately describes a “Modifying a List While Iterating Over It” error. 
# In this case, the loop changes the list elements during iteration, leading to unexpected behavior such as skipping elements or going out of range.


# 10 ) Which scenario is an example of a “NameError”?

# Answer) A local or global name is not found in the code

# This scenario accurately describes a “NameError”. In this case, the code tries to use a variable or function name that has not been defined.

# 11) Which input validation method would be most appropriate to ensure that a username only contains letters, numbers, and underscores?

# Answer) Pattern matching

# Pattern matching uses regular expressions to match input patterns.
#  This would be the appropriate method to ensure a username only contains letters, numbers, and underscores.
#  As per the provided text, the re.match(r'^\w+$', username) function is used to validate that a username only contains letters, numbers, and underscores.
#  If the username contains any other characters, it raises a ValueError