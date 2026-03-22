f = open(r'C:\Users\David\Documents\2020_router_purchase.csv', 'r')
x = f.read().split('\n')
print(x) # or can do type x if in python interpreter mode i.e >>> (if I ran python from a terminal window)
y = x[2] # read x at index 2
z = y.split(',') # split at every instance of , inside y. remember split breaks the string into a list.
price_4331 = z[4]
print(price_4331)

#