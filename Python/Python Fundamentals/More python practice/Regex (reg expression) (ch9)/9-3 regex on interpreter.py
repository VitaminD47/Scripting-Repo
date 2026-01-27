import re
with open(r"C:\Users\David\OneDrive\Desktop\Script Repository\Script-Repo\Python\More python practice (from python automation book)\Regex (reg expression) (ch9)\chapter9_codes (from author)\sh_ver.txt") as f:
    read_file = f.read()

print(read_file)
rt_model = re.findall(r"\b[A-Z]{3}\d{4}/\w+\b", read_file)
print(rt_model)