def update_log_list(log_list):
    replace_webserver = {"level":"ERROR"}
    replace_database = {"timestamp":"2023-12-07T12:30:00",}
    for entry in log_list:
        if entry.get("app")=="webserver":
            entry.update(replace_webserver)
        if entry.get("app")=="database":
            entry.update(replace_database)
          
    return log_list
        

   #this one took me over 3 hrs...lol

   # can also use this for the for loop without the .get() method. it will return an error though if the key isn't found. 
   #for entry in log_list:
    if entry["app"] == "webserver":
        entry["level"] = "ERROR"
    if entry["app"] == "database":
        entry["timestamp"] = "2023-12-07T12:30:00"

#!!! Remember that you cannot call methods on a list like .get() or .update(), only on dictionaries or variables.


# [{'app': 'webserver', 'level': 'ERROR', 'message': 'Critical error', 'timestamp': '2023-12-07T11:55:00'},
# {'app': 'database', 'level': 'ERROR', 'message': 'Database connection lost', 'timestamp': '2023-12-07T11:50:00'}]

# A list of application logs have been collected. 
# Each log's details are stored in a dictionary with the keys app, level, message, and timestamp. 
# Updates to the log details are needed based on the following requirements:


# Change the log level to "ERROR" for the log with application name webserver. 
# Update the timestamp to "2023-12-07T12:30:00" for the log with application name database.

# Complete the Python function update_log_list. 
# The function should accept a list of dictionaries representing log files, 
# update the values in the log files based on the two requirements, and return the updated list of log files.



log_sample = [
    {"app": "webserver", "level": "changeme", "message": "Critical error", "timestamp": "2023-12-07T11:55:00"},
    {"app": "database", "level": "ERROR", "message": "Database connection lost", "timestamp": "changeme"}]
print(update_log_list(log_sample))