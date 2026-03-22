import re

expr = 'I was born in 2,009 and I am 15 years old. I started my primary school in 2,010'
p = re.compile(r'[1-9](?:\d{0,2})(?:,\d{3})*(?:\.\d*[1-9])?|0?\.\d*[1-9]|0')

m = p.findall(expr)

print(m)