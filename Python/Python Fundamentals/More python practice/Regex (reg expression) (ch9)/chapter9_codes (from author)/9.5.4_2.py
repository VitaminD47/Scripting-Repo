import re

expr = 'I was born in 2,009 and I am 15 years old. I started my primary school in 2,010'
p = re.compile(r"""
[1-9]           # Match a single digit between 1-9
(?:\d{0,2})     # Match digit equatl to [0-9] between 0 and 2 times
(?:,\d{3})*     # Match the character ,(Comma) literally, match a digit equal to [0-9] \
                  exactly 3 times) Zero and unlimited times
(?:\.\d*[1-9])? # Match the character. (Dot) literally, match a digit equal to [0-9] \
                   zero and unlimited times, match a single digit between [1-9]) \
                   zero and one time.
|               # OR
0?\.\d*[1-9]    # Match 0 zero or one time, match . (Dot) literally, match a digit \ 
                   equal to [0-9] zero or unlimited times, and match a digit between [1-9]
|               # OR
0               # Match one 0
""", re.VERBOSE)

m = p.findall(expr)

print(m)