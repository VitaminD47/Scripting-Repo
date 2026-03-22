###
# this creates and writes a file called 2020_router_purchase.csv with 7 lines (rows) using csv module
import csv
with open (r'C:\Users\David\Documents\2020_router_purchase.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    filewriter.writerow (['Site', 'Router_Type', 'IOS_Image', 'No_of_routers', 'Unit_price($)', 'Purchase_Date'])
    filewriter.writerow (['NYNY', 'ISR4351/K9', 'isr4300-universalk9.16.09.05.SPA.bin', 4, '$ 9100.00', '1-Mar-20'])
    filewriter.writerow (['LACA', 'ISR4331/K9', 'isr4300-universalk9.16.09.095.SPA.bin',2,'$5162.00', '1-Mar-20'])
    filewriter.writerow (['LDUK', 'ISR4321/K9', 'isr4300-universalk9.16.09.095.SPA.bin',1,'$2370.00', '3-Apr-20'])
    filewriter.writerow (['HKCN', 'ISR4331/K9', 'isr4300-universalk9.16.09.095.SPA.bin',2,'$5162.00', '17-Apr-20'])
    filewriter.writerow (['TKJP', 'ISR4351/K9', 'isr4300-universalk9.16.09.095.SPA.bin',1,'$9100.00', '15-May-20'])
    filewriter.writerow (['MHGM', 'ISR4331/K9', 'isr4300-universalk9.16.09.095.SPA.bin',2,'$5162.00', '30-Jun-20'])

# file can be read by opening with excel, or cia command line with python like this : 

with open(r'C:\Users\David\Documents\2020_router_purchase.csv','r') as f:
       routers = f.read()
       print(routers)
          
       