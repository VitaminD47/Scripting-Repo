# more practice with for loops, this one prints out each line of text in a variable and puts it on a new line

txt1 = "Seeya later Alligator"
for line in txt1:
    print(line)

# alternatively:
# adding end= to the print statement followed by '' separates the text with a space. default is a newline via \n or by leaving no second argument
txt1 = "Seeya later Alligator"
for line in txt1:
    print(line, end='')