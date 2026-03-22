# 9.2.1 If/Else Statements Lab :

#An existing dictionary records usernames as keys and the operating system of that user's device as the associated value. 
#Use if/else statements to complete the function "os_counts()". 
#The function should accept a dictionary of usernames and operating systems,
# determine which operating systems are present as well as counts of how many users are using each operating system,
# and return a dictionary of operating system counts (e.g., {'Windows': 4, 'MacOS': 3, 'Linux': 3})

# Only the dictionary returned by os_counts() will be graded for this assignment. The function should work for any dictionary of usernames and operating systems passed to the function beyond the examples provided.

def os_counts(os_dict):
    os_list = list(os_dict.values()) # This becomes [4, 3, 3] on the second function call, which breaks the output. Removing line #40 fixes this.
    if "Windows" in os_list:
        print("Windows OS is present")
    else:
        print("No Windows OS is present")

    if "Linux" in os_list:
        print("Linux is present")
    else:
        print("No Linux is present")
    if "MacOS" in os_list:
        print("MacOS is present")
    else:
        print("MacOS is not present")
    
     
    os_count_dict = {
    "Windows": os_list.count("Windows"), #all of these become = 0 because they aren't in the list [4, 3, 3]
    "Linux": os_list.count("Linux"),
    "MacOS": os_list.count("MacOS")
 }
 
    return os_count_dict
    
    
user_laptop_os = {"user1": "Windows", "user2": "MacOS", "user3": "Linux", "user4": "Windows", "user5": "Windows", "user6": "Linux", "user7": "MacOS", "user8": "Windows", "user9": "MacOS", "user10": "Linux", "user11": "Linux", "user12": "Windows", "user12": "Linux", "user13":"Linux"}

# Important info to explain error I was getting
#user_laptop_os = os_counts(user_laptop_os)
#the output of the statement here on line 38 becomes {'Windows': 4, 'Linux': 3, 'MacOS': 3}, which is intended. However, because of the print statement on line 44,
# the function gets called again and this messes up the input because it is now passing the values of [4, 3, 3] which is not expected, it is expecting strings instead.

# You may alter the code below to view your return value(s).
# Only the os_counts function will be graded for this assessment.

print(os_counts(user_laptop_os))





