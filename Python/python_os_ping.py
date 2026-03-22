import os
hName = "amazon.com" # host site, could come from database, file, user, etc
sResp = os.system("ping -n 2 " + hName)

# determine response
if sResp == 0:
    print(hName),'is up and running'
else: 
    print(hName),'is currently down'

    

#test#

