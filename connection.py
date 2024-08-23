import os
import csv
from netmiko import ConnectHandler
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
user=os.getenv("USERNAME")
pswd=os.getenv("PASSWORD")


now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H-%M-%S")

with open ("sitios/urraza.csv", "r") as filecsv:
    data = csv.reader(filecsv)
    next(data)
    IPaddxr = []
    IPaddlf = []
    IPaddsp = []
    IPaddapic = []
    for item in data:
       IPaddxr.append(item[0])    
       IPaddlf.append(item[1])
       IPaddsp.append(item[2])
       IPaddapic.append(item[3])

IPaddxr = list(filter(None,IPaddxr))
IPaddlf = list(filter(None,IPaddlf))
IPaddsp = list(filter(None,IPaddsp))
IPaddapic = list(filter(None,IPaddapic))


devicexr_list = []
devicelf_list = []
devicesp_list = []
deviceapic_list = []

def router_info():
       for ip in IPaddxr:
              if(ip==""):
                     break
              else:
                     ciscoxr_device = {
                            'device_type': 'cisco_xr',
                            'host': ip,
                            'username': user,
                            'password': pswd,
                            'port': 22,
                            'verbose': True
                            }
                     devicexr_list.append(ciscoxr_device)
       print(devicexr_list)
"""
                     for device in devicexr_list:
                            connection = ConnectHandler(**device)
                            print('Entering the device: '+ device)

                            with open('commands\CISCO-XR.txt') as f:
                                   devices = f.read().splitlines()
        
                            outputline=""
                            for cmdline in devices:
                                   output = connection.send_command(cmdline)
                                   outputline = (outputline+'\n'+output)
                            print(outputline)

                            # creating the backup filename (hostname_date_backup.txt)
                            prompt = connection.find_prompt()
                            hostname = prompt[0:-1]
                            # print(hostname)

                            # getting the current date (year-month-day)

                            # creating the backup filename (hostname_date_backup.txt)
                            filename = f'{hostname}_{dt_string}_backup.txt'

                            # writing the backup to the file
                            with open(filename, 'w') as backup:
                                   backup.write(outputline)
                                   print(f'Backup of {filename} completed successfully')
                                   print('#' * 30)

                            print('Closing connection')
                            connection.disconnect()
"""