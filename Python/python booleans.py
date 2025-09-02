

#The existing code identifies if a network issue has been resolved.
# Alter the stored Boolean values of the variables "is_connected" and "has_internet" to trigger the "if network_resolved" code block.

# Solution : Set both variables to True so the network_resolved variable can evaluate to true and execute the if statement block.
is_connected = True
has_internet = True
# do not edit below this line
network_resolved = is_connected and has_internet

if network_resolved:
    print("The device is connected and has internet. Issue resolved")
else:
    if not is_connected:
        print("The device has connection issues")
    if not has_internet:
        print("The device has internet issues")

# Expected output
# The device is connected and has internet. Issue resolved