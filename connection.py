from netmiko import ConnectHandler
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H-%M-%S")

#device_list = []

def router_info(user, pswd, IPadd, device, ciscoos,beg_prompt=0,fin_prompt=-1):
       device_list = []
       for ip in IPadd:
              cisco_device = {
                     'device_type': device,
                     'host': ip,
                     'username': user,
                     'password': pswd,
                     'port': 22,
                     'verbose': True
                     }
              device_list.append(cisco_device)
       #print(device_list)
       for device in device_list:
              connection = ConnectHandler(**device)
              print(f'Entering the device: {device["host"]}')
              print('-' * 45)
              with open(f'src/commands/CISCO-{ciscoos}.txt') as f:
                     devices = f.read().splitlines()
        
              outputline=""
              for cmdline in devices:
                     output = connection.send_command(cmdline,read_timeout=120)
                     outputline = (outputline + '\n[' + cmdline + ']:\n' +output)
                     print(cmdline)
              print(outputline)

              # creating the backup filename (hostname_date_backup.txt)
              prompt = connection.find_prompt()
              hostname = prompt[beg_prompt:fin_prompt]
              #print(hostname)

              # getting the current date (year-month-day)

             # creating the backup filename (hostname_date_backup.txt)
              filename = f'prev_{hostname}_{dt_string}_backup.txt'

              # writing the backup to the file
              with open(filename, 'w') as backup:
                     backup.write(outputline)
                     print('#' * 69)
                     print(f'Backup of {filename} completed successfully')
                     print('#' * 69)

              print('Closing connection....')
              connection.disconnect()
              print('\n' * 2)