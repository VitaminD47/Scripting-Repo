import re

sh_ver ='''
-----------------------------------------------------------------
Technology    Technology-package           Technology-package
              Current       Type           Next reboot
------------------------------------------------------------------
appx             None             None             None
uc               uck9             RightToUse       uck9
security         None             None             None
ipbase           ipbasek9         Permanent        ipbasek9

cisco ISR4351/K9 (2RU) processor with 1687137K/6147K bytes of memory.
Processor board ID FDO3132B2Z4
3 Gigabit Ethernet interfaces
31 Serial interfaces
1 Channelized E1/PRI port
32768K bytes of non-volatile configuration memory.
4194304K bytes of physical memory.
3223551K bytes of flash memory at bootflash:.

Configuration register is 0x2102
'''

# Only match Cisco router model number from show version output.
rt_model = re.findall("[A-Z]{3}\d{4}[/]\w+", sh_ver)
my_router = rt_model[0]
print(my_router)