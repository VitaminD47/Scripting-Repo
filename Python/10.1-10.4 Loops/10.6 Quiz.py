#10.6 Loops Quiz Review

# What is the output of the Python code?

def is_device_up(device_ip):
    return False

device_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for device_ip in device_ips:
    if is_device_up(device_ip):
        output = f"Device {device_ip} is up."
    else:
        output = f"Device {device_ip} is down."

    
    print(output)


# Answer choices below :

# “Device 192.168.1.1 is up.”


# “Device 192.168.1.1 is down.”


# “Device 192.168.1.1 is down. Device 192.168.1.2 is down. Device 192.168.1.3 is down.” ---Correct answer


# “Device 192.168.1.1 is up. Device 192.168.1.2 is up. Device 192.168.1.3 is up.”


# The function is_device_up(device_ip) returns False for all device_ip, so the else block is executed for each IP in the list


#2) What is the output of the Python code?

def is_device_up(device_ip):
    return False

device_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
i = 0

while i < len(device_ips):
    device_ip = device_ips[i]
    
    if is_device_up(device_ip):
        output = f"Device {device_ip} is up."
    else:
        output = f"Device {device_ip} is down."
    
    print(output)
    i += 1

    # Answer ) “Device 192.168.1.1 is down. Device 192.168.1.2 is down. Device 192.168.1.3 is down.”

    # The function is_device_up(device_ip) returns False for all device_ip, so the else block is executed for each IP in the list






# 3) What is the output of the following Python code?

i = 0
while i < 3:
    print(i)
    i += 1



# Answer : 0, 1, 2 because the while loop condition is i < 3, so the loop will print 0, 1, and 2 before terminating.



# 4)  What is the output of the Python code?

def is_device_up(device_ip):
    if device_ip == "192.168.1.2":
        return False
    return True

device_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
i = 0

while i < len(device_ips):
    device_ip = device_ips[i]
    
    if not is_device_up(device_ip):
        output = f"Device {device_ip} is down. Stopping check."
        break
    
    output = f"Device {device_ip} is up."
    print(output)
    i += 1

    # The function is_device_up(device_ip) returns True for “192.168.1.1” and False for “192.168.1.2”. 
    # So, the script prints that “192.168.1.1” is up and then prints that “192.168.1.2” is down and breaks the loop




    # 5) What is the output of the Python code?

def is_device_up(device_ip):
    if device_ip == "192.168.1.2":
        return False
    return True

device_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
i = 0

while i < len(device_ips):
    device_ip = device_ips[i]
    
    if not is_device_up(device_ip):
        print(f"Device {device_ip} is down. Skipping to next device.")
        i += 1
        continue
    
    print(f"Device {device_ip} is up.")
    i += 1

    # The function is_device_up(device_ip) returns True for “192.168.1.1” and “192.168.1.3”, and False for “192.168.1.2”. 
    # So, the script prints that “192.168.1.1” and “192.168.1.3” are up, and that “192.168.1.2” is down and skips to the next device
    # Then it prints "Device 192.168.1.3" is up since the script used a continue and not a break.





    # 6) What is the output of the Python code?

i = 0

while i < 3:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("Loop finished")


# The break statement is executed when i becomes 2, so 2 is not printed and the loop is exited prematurely. 
# Therefore, the else block is not executed and “Loop finished” is not printed.

# Result should be 0, 1




#7) What is the output of the Python code?

ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

for ip in ip_addresses:
    print(ip)

# Answer 192.168.1.1
      #  192.168.1.2
      #  192.168.1.3

# All will be printed on a new line via \n but it won't be displayed in the print output.






# 8) Which statement describes the difference between a for loop and a while loop in Python?

# Answer 
# A for loop is used for iterating over a sequence or other iterable objects, 
# while a while loop is used when a set of statements needs to be executed until a condition is false


 #   A for loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
 #   The set of statements is executed once for each item in the list. The loop continues until it has gone through each item in the sequence.
 #   A while loop is used when a set of statements needs to be executed until a condition is false



 
 # 9) What is the output of the Python code?

for i in range(2, 10, 2):
    print(i)



# 2  = Start, 10 = end (not included, just up to it), 2 = step interval i.e spacing

# Answer ) Output should be 2 4 6 8 on new lines







# 10) What is the output of the Python code?

for i in range(3):
    if i == 2:
        break
    print(i)
else:
    print("Loop finished")

    # Answer : 0 1  (on a new line each number)
    # The break statement is executed when i becomes 2, so 2 is not printed and the loop is exited prematurely.
    # Therefore, the else block is not executed and “Loop finished” is not printed.



# 11) What is the output of the Python code?

for i in range(3):
    pass
print(i)


#Answer ) 2

# The for loop iterates over all items in the range, and the pass statement does nothing for each iteration.
# After the loop, i is the last item in the range, which is 2


