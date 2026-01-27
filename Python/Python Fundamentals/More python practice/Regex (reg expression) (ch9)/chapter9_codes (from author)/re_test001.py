import re

string = 'Configuration register is 0x2102'

x = re.search('\dx\d{4}', string)
print(x)
