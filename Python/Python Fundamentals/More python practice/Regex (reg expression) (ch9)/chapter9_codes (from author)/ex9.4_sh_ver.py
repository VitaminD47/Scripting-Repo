import re
with open("/home/pynetauto/ex_regex/sh_ver.txt") as f:
    read_file = f.read()

# Only match Cisco router model number from show version output.
rt_model = re.findall("[A-Z]{3}\d{4}[/]\w+", read_file)
print(rt_model)

my_router = rt_model[0]
print(my_router)

