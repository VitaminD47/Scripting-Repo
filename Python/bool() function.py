# Bool() is used to explicitly convert values to Boolean i.e true or false

#Truthy values are non-zero numbers and non-empty strings.
# Falsy values are zero, None and empty strings.
bool(10)
# ^ This would evaluate to true. Nothing is shown because no print statement. It has to be nested. Shown below :
print(bool(-35))
print(bool(250))
print(bool("Massive Freak"))
#Below are false statements. 0, None, 0.0, '', [], {} should all return false in the output
print(bool(0))  
print(bool(None))

