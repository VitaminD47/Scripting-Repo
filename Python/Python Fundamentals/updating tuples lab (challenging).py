#From zybooks lab 6.10.1 :

#A list of network devices is comprised of tuple elements, with each tuple identifying a device type, manufacturer, model, and IP address.
#Each device has been unpacked into the existing variables "device1" through "device4". 

#Alter the values in the tuple "device2", updating the manufacturer from "Cisco" to "HPE" and the model from "Catalyst 9300" to "Aruba 3810M". 
#Update "network_devices" with the updated "device2".
#Then create a new tuple "device5" using the information stored in the list "device5_info" and append to "network_devices".

network_devices = [
    ("Router", "Cisco", "ISR 4000", "10.0.0.1"),
    ("Switch", "Cisco", "Catalyst 9300", "10.0.0.2"),
    ("Firewall", "Palo Alto Networks", "PA-220", "10.0.0.3"),
    ("Access Point", "Aruba", "AP-505", "10.0.0.4"),
]
device1, device2, device3, device4 = network_devices

device5_info = ["Load Balancer", "F5 Networks", "BIG-IP 4200", "10.0.0.5"]
# do not edit above this line
network_devices[1] = ("Switch", "HPE", "Aruba 3810M", "10.0.0.2")

# update device2 and reflect change in network_devices



# create tuple device5 from device5_info
# append to end of network_devices
device5 = tuple(device5_info)
network_devices.append(device5)


# do not edit below this line
print("network_devices ", type(network_devices))
for device in network_devices:
  print(device, type(device))

# Expected output
# network_devices  <class 'list'>
# ('Router', 'Cisco', 'ISR 4000', '10.0.0.1') <class 'tuple'>
# ('Switch', 'HPE', 'Aruba 3810M', '10.0.0.2') <class 'tuple'>
# ('Firewall', 'Palo Alto Networks', 'PA-220', '10.0.0.3') <class 'tuple'>
# ('Access Point', 'Aruba', 'AP-505', '10.0.0.4') <class 'tuple'>
# ('Load Balancer', 'F5 Networks', 'BIG-IP 4200', '10.0.0.5') <class 'tuple'>