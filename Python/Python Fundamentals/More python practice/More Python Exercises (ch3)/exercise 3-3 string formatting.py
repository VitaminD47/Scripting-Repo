name, age, height = 'Hugh', 15, 174.5
detail = f"His name is {name}, he is {age} and {height} cm tall."
print(detail)

#^ this is formatted string, or f-string. I prefer this over what the book shows which shows .format() method (seen below)

Name, age, height = 'Hugh', 15, 174.5
detail = ('His name is {}, he is {} and {} cm tall.'.format(name, age, height))
print(detail)