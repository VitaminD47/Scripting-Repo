def format_rgb(rgb1):
    str_values = []
    for value in rgb1:
        str_values.append(str(value))
    joined = ",".join(str_values)
    return f"rgb({joined})"

# You may alter the code below to test your solution or print help documentation.
# Only the format_rgb function will be graded for this assessment.

rgb_sample = [255, 165, 13]
print(format_rgb(rgb_sample))
#help(help)

#alternatively, for the for loop you can use a list comprehension. that would be this :

    #str_values = [str(value) for value in rgb1]

# this creates the empty list and appends to it automatically under the hood without having to specify in the regular for loop.
#I would argue this is better overall

