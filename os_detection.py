import os
import platform

def os_det():
    OS = os.name
    p = platform.platform()
    if OS == 'posix':
        print('Linux based operating system\n {}'.format(p))
    elif OS == 'nt':
        print('Windows operating system\n {}'.format(p))
    else :
        print('Operatin system could not be determined\n {}'.format(p))
