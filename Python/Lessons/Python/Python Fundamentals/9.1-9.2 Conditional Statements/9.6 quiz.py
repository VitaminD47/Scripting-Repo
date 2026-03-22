# 9) What is the output of the Python code?


def is_device_up(device_ip):
    return False

device_ip = "192.168.1.1"

if not is_device_up(device_ip):
    output = f"Device {device_ip} is down."
else:
    output = f"Device {device_ip} is up."

print(output)

# The not keyword in Python reverses the truth value of the condition. 
# Since is_device_up(device_ip) returns False, the not keyword makes this True, so the script prints that the device is down.