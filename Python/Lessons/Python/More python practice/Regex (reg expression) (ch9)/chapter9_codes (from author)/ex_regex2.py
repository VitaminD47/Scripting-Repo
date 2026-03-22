import re
#changed file path to reflect my actual file path)
with open(r"C:\Users\David\OneDrive\Desktop\Script Repository\Script-Repo\Python\More python practice (from python automation book)\Regex (reg expression) (ch9)\chapter9_codes (from author)\sh_ver.txt") as f:
    read_file = f.read()

# Only match Cisco router model number from show version output.
rt_model = re.findall(r"[A-Z]{3}\d{4}[/]\w+", read_file)
#print(rt_model)

my_router = rt_model[0]
print(my_router)

