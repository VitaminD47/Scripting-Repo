sw_mac = '''pynetauto-sw01 84:3d:c6:05:09:11 pynetauto-sw17 80:7f:f8:80:71:1b pynetauto-sw05 f0:62:81:5a:53:cd'''
import re

sw_mac = sw_mac.replace(":","").upper()
pattern = re.compile("([0-9A-F]{6})" "([0-9A-F]{6})")
print(pattern.sub("\g<1>******", sw_mac))
