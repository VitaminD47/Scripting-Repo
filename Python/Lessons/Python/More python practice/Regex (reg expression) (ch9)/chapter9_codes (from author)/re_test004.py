import re

string = '''
Interface              IP-Address      OK? Method Status                Protocol
Vlan1                  unassigned      YES NVRAM  up                    up
Vlan20                 10.20.20.11     YES NVRAM  up                    up
FastEthernet0          unassigned      YES NVRAM  down                  down
GigabitEthernet1/0/1   unassigned      YES unset  up                    up
GigabitEthernet1/0/2   unassigned      YES unset  down                  down
GigabitEthernet1/0/3   unassigned      YES unset  up                    up
Te1/0/1                unassigned      YES unset  up                    up
Te1/0/2                unassigned      YES unset  up                    up
Port-channel1          unassigned      YES unset  up                    up
Loopback0              10.0.0.123      YES NVRAM  up                    up
'''

intf = re.findall(r"(G\w+\d\/\d\/\d)", string)
print(intf)

s2 = re.findall(r"^.+$", string)
print(s2)