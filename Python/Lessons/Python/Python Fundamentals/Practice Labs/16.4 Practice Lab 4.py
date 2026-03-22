def validate_id(id):
    if len(id)==8:
        department_code=id[0:3]
        employee_number=id[3:]
        #the 2 if statements below are a way to nest and/or continue the conditional statements, remember to close each one out with an else 
        # both if statements are needing to be true so that is why this is done. remember we would use elif following an if to execute under the condition that the if is false.
        #that is not the case here.
        #they could also be one long line and not be nested but it would be cluttered.
        if type(department_code)== str and department_code.isupper(): 
            if employee_number.isnumeric() and len(employee_number) == 5: # the .isnumeric() is important because a string is passed, not an int. 
                return True
            else:
                return False
        else:
            return False
    else:
        return False        
            
                
    




# Instruction : 
# A business requires that each employee ID begins with a department identifier and 
# ends with an individual identifier (e.g., "HRD00123", "ENG00567").
#  The department identifier is a 3-letter department code in all uppercase.
#  The individual identifier is a 5-digit numeric value.

# Complete the Python script to create a custom function name validate_id.
# The function should accept a string parameter representing an employee ID, 
# Determine if the ID meets the requirements, and return a Boolean value, with True returned if all requirements are met
# and False returned if any requirement is not met.

# Only the validate_id function will be graded for this assessment.

print(validate_id("HRD00123"))
# help(help)