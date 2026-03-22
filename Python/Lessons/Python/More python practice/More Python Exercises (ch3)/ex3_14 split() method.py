txt1 = "Seeya later Alligator"
print(txt1.split())

txt1 = "Seeya later Alligator" # split at first instance of e
print(txt1.split('e',1))


txt2 = (txt1.split('e',1)) 
print(txt2[0]) # extracting only letter s, hence index 0  

txt3 = (txt1.split('a',3)) #split at every a 3 times
print(txt3)

print(txt3[1])  # extracts the letter l, as it's at index 1 in the created list from txt1 when split.() was performed
