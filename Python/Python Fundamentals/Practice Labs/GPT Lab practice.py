

"""def extract_numbers(currentlist):
    extractedlist = []
    for s in currentlist:
        if s.isnumeric():
            extractedlist.append(s)
        else:
            pass
    return extractedlist
        

        
    

print(extract_numbers(["42", "hello", "1001", "abc", "222", "12999","007"]))"""""

def format_rgb(onelist):
    formatted_list = []
    # Check input is 3 items
    if not isinstance(onelist,list) or len(onelist) != 3:
        return "Input must be a list of 3 values."
       

    for color in onelist:
        if not isinstance (color,int) or not (0 <= color <=255):
            return "All values must be integers between 0 and 255."
        
        formatted_list.append(str(color))
       
               
        
    return f"rgb({",".join(formatted_list)})"


mythree =  [105,165,13]

print(format_rgb(mythree))

#practiced on 8/6/2025 
# remember isinstance is preferred over type


"""so I see a few problems with what I had : 
1. The for loops should have been separated and not nested as it can break the logic.
2. The isinstance function is the preferred method for checking an object type, not the type function which is used when looking for a boolean value. 
3. The str function was nested in the .append() method which was cleaner and saves writing another line for a variable, but either way would work. """


