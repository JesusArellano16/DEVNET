import csv

def get_ips(loc, device):
    with open (f'src/sitios/{loc}.csv', "r") as filecsv:
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

    if device == "RMAC":
        return IPaddxr
    elif device == "LF":
        return IPaddlf
    elif device == "SP":
        return IPaddsp
    elif device == "APIC":
        return IPaddapic