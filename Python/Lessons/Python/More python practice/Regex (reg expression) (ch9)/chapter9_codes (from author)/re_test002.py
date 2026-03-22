import re

string = '0x2142 Configuration register is 0x2102'

p = re.compile('\dx\d{4}')
x = p.match(string)
print(x)
