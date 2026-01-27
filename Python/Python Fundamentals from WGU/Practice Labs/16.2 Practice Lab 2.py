def minutes_to_hours(minutes):
    hours = float(minutes)/60
    return hours
    

# You may alter the code below to test your solution or print help documentation.
# Only the minutes_to_hours function will be graded for this assessment.

mins = 300
print(minutes_to_hours(mins))
# help(help)

# Instructions below :

# The function should accept an integer representing the execution time of a process in minutes, 
# convert the value from minutes to hours, and return a float representing the execution time in hours.
# There are 60 minutes in an hour. 
# The function should utilize float division and not integer division.