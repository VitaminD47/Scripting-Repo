# A database contains user data uploads with varying submission times. 
# To process the latest information first, a function is needed to identify the most recent upload time.

# Complete the Python function find_latest. 
# The function should accept an unordered list of user upload time strings, 
# convert each string value into a datetime object using the provided date_format pattern, 
# and return the most recent upload time as a datetime object.

from datetime import datetime

def find_latest(submissions):
    # Specify a date format
    date_format = '%m/%d/%Y %I:%M %p'
    # Convert string values into datetime objects. 
    for time in submissions:
        new_submission = datetime.strptime(time, date_format)
        
    # Determine and return latest
    latest_submission = datetime.strptime(submissions[0],date_format)
    for time in submissions:
        current = datetime.strptime(time, date_format)
        if current > latest_submission:
            latest_submission = current

#remember to create new variables when needed like we did in second for loop. we needed something to compare against
# passing submissions[0] works because it's targeting the first string of newly created latest_submission. you cannot pass the full list to strptime, it won't accept it.
# the 'current' variable created in the second for loop is just another datetime object conversion needed for comparison.
# so, what's happening is each str in 'current' is compared to the first index of 'latest_submission'
# as a result, 'latest_submission' will result in the highest value.

    return latest_submission
# You may alter the code below to test your solution or print help documentation.
# Only the find_latest function will be graded for this assessment.

submission_timestamps = ['12/15/2023 08:45 AM', '12/14/2023 03:30 PM', '12/16/2023 11:20 AM', '12/13/2023 06:15 PM']
print(find_latest(submission_timestamps))
#help(datetime.strptime)