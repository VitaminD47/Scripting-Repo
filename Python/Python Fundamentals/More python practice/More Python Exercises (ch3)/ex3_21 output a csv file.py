##this is just another example on how to read/output the file, but without the csv module. this uses a for loop for all lines.

f = open(r'C:\Users\David\Documents\2020_router_purchase.csv', 'r')
for line in f:
    print(line.strip())

f.close()

# use .strip() to remove the leading/trailing whitespaces, newlines and tabs.

