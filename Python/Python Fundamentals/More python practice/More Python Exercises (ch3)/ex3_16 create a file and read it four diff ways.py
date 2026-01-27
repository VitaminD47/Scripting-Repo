#1.

with open ('test123.txt', 'w') as f:
    f.write('This is line1.\nThis is line 2.\nThis is line3.\n')


with open('test123.txt', 'r') as f:
    lines = f.readlines()
    print(lines)

with open('test123.txt', 'r') as f:
    lines = list(f)
    print(lines)


f = open('test123.txt', 'r')
lines = f.readlines()
print(lines)
f.close()

f = open('test123.txt', 'r')
lines = list(f)
print(lines)
f.close()