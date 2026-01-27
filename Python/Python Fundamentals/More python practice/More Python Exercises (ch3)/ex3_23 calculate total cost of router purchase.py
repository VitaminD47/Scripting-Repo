# this is done without any modules

total = 0.0


with open(r'C:\Users\David\Documents\2020_router_purchase.csv', 'r') as f:
    headers = next(f) # this skips the first line header information. we do this to avoid potential calculation errors
    for line in f:
        line = line.strip() #stripping to remove all the white spaces
        devices = line.split (',') # splitting here at all instances of ,
        devices[4] = devices[4].strip('$') # removing the white spaces where $ is present at index 4
        devices[4] = float(devices[4]) #converting each line at index 4 to a float value
        devices[3] = int(devices[3])  # converting each line at index 3 to an integer value
        total += devices[3] * devices[4]
    print('Total cost: $', total)

# result should be $ 78842.0