with open('test123.txt', 'w') as f:
    f.write(' this is a lower casing line.\n')

with open('test123.txt', 'r') as f:
    print(f.read())
    

with open('test123.txt', 'w') as f:
    f.write('THIS IS AN UPPER CASING LINE. \nThisISACamelCasingLine.\n')

with open ('test123.txt', 'r') as f:
    print(f.read())


with open('test123.txt', 'r') as f:
    print(f.readlines())


with open('test123.txt', 'w') as f:
    f.write('i  have  overwritten  the contents of this file  .')
    

with open('test123.txt', 'r') as f:
    print(f.readlines())


#with open ('test123.txt', 'r') as f:
 #   print(f.read().upper().strip().replace(" ", ""))  # this replaces the spaces with no spaces



with open('test123.txt', 'r') as f:
    x = (f.read().lower().strip())
    y = set(x.split())
    print(y)
    print(len(y))





