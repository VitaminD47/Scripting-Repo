# Python code​​​​​​‌‌​‌‌‌‌​​​​‌​​​‌‌​‌‌​‌​‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
  
    hexNum = hexNum.upper()

    for v in hexNum:
        if not 1 <=len(hexNum) <=3:
            return None

    for char in hexNum:
        if char not in hexNumbers:
            print(f"{char} is not valid.")
            return None
    
    if len(hexNum) == 3:
        return (hexNumbers[hexNum[0]] * 256 +
                hexNumbers[hexNum[1]] * 16 +
                hexNumbers[hexNum[2]])

    return hexNum

print(hexToDec("A2F"))

## another easier version 


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    if len(hexNum) == 3:
        return hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]]
    
    if len(hexNum) == 2:
        return hexNumbers[hexNum[0]] * 16 + hexNumbers[hexNum[1]] 

    if len(hexNum) == 1:
        return hexNumbers[hexNum[0]] 

    return hexNum

# a version that includes a loop which can cover any string length :


def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    converted = 0
    exponent = len(hexNum - 1 )
    for char in hexNum:
        converted = converted + (hexNumbers[char] * (16 ** exponent))
    return converted
    
#review this later
