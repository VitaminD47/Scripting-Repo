sw_mac = '''pynetauto-sw01 84:3d:c6:05:09:11 
pynetauto-sw17 80:7f:f8:80:71:1b 
pynetauto-sw05 f0:62:81:5a:53:cd'''

import re # Import Python re (Regular Expression) module

sw_mac = sw_mac.replace(":", "").upper() # Remove colons & capitalize
pattern = re.compile("([0-9A-F]{6})" "([0-9A-F]{6})") # Create pattern to match
                                                      # macth 6 Hex numbers twice
print(pattern.sub("\g<1>******", sw_mac)) # Substitute group 1 pattern