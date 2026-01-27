#create code that requires user input, here it's asking for a user's name.

print('Please enter your name: ')
name = input()
print('Thank you,', name)

# this one immediately goes to input and uses an f- string.
name = input('Please enter your name: ')
print(f'Hi, {name}.')