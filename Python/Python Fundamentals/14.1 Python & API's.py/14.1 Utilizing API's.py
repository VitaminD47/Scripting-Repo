# 14.1 Utilizing API's

# Application Programming Interfaces (APIs) are sets of rules and protocols for building software and applications. 
# They allow different software systems to communicate and share data. 


# Interfacing with APIs using Python is beneficial as 
# it enables automation, data extraction, and interaction with online services and resources, enhancing the functionality and efficiency of Python applications.

# Let’s consider a network automation task of updating the configuration of a network device using an API. Here’s how Python can be used for this task:

import requests
import json

# Step 1: Read data from the API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

# Step 2: Store the data as a file
with open('config.json', 'w') as file:
    json.dump(data, file)

# Step 3: Manipulate the data
#quick reminder for below, the indexes 0 and 1 are used to access the indexes inside the list that is returned.
# the .json() method on line 18 returns the json page as a list of dictionaries i.e [ {user1: dave, pass:test}, {user2: rave, pass:dayz}]
# you can't access a list item via string i.e 'dave', 'user1', etc. Only index (indices)
data[0]['userId'] = "test"
data[1]['userId'] = "test2"
# Step 4: Store the updated data as a file
with open('config.json', 'w') as file:
    json.dump(data, file)

# Step 5: Push the changes back to the API
response = requests.put(url, data=json.dumps(data))
print(data)

# This code first reads the configuration of a network device from an API and stores it as a JSON file. 
# It then updates a setting in the configuration and stores the updated configuration as a JSON file.
# Finally, it pushes the updated configuration back to the API.


# Please replace "http://network-device-api/config" and 'setting' with the actual API endpoint and setting name. 
# Also, error checking is omitted for brevity. In a real-world scenario, each API call should be checked for errors.





# Another example of accessing an API in Python

# Here is the code being executed:

#import requests

#def get_posts():
 #   response = requests.get('https://jsonplaceholder.typicode.com/posts')
  #  if response.status_code == 200:
   #     posts = response.json()
     #   for post in posts:
    #        print(f"Post ID: {post['id']}, Title: {post['title']}")

#get_posts()
