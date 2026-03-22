# this is ideal script flow for pattern matching per the author, pg 385
import re
p = re.compile("Enter_re_here") # p = pattern. this is the regular expression pattern itself.
expr = 'string_to_search_here' # data/expression to search for
m = p.match(expr) # matching patterns using pattern. this is the function that uses expr as input
if m:
    print('Match found: ', m.group()) # conditional to print if a match is found
else:
    print('Match not found')
### end

# practice below 