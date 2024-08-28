from netmiko import ConnectHandler
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H-%M-%S")

device_list = []

def router_info(user, pswd, IPadd, device):
       for ip in IPadd:
              if(ip==""):
                     break
              else:
                     cisco_device = {
                            'device_type': device,
                            'host': ip,
                            'username': user,
                            'password': pswd,
                            'port': 22,
                            'verbose': True
                            }
                     device_list.append(cisco_device)
       print(device_list)
"""
                     for device in device_list:
                            connection = ConnectHandler(**device)
                            print('Entering the device: '+ device)

                            with open('src/commands/CISCO-XR.txt') as f:
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
                            filename = f'prev_{hostname}_{dt_string}_backup.txt'

                            # writing the backup to the file
                            with open(filename, 'w') as backup:
                                   backup.write(outputline)
                                   print(f'Backup of {filename} completed successfully')
                                   print('#' * 30)

                            print('Closing connection')
                            connection.disconnect()
"""