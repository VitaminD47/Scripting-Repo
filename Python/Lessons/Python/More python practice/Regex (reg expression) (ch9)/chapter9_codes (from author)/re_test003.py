import re

list = ["Cisco switch", "HP switch", "Juniper switch"]

for i in list:
    v = re.match("(C\w+)\W(s\w+)", i)
    if v:
        print((v.groups()))