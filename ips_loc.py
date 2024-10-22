import json

def get_ips(loc):
    with open (f'src/sitios/{loc}.json', "r") as file:
        data = json.load(file)
        for key, value in data.items(): #Se itera para extraer los valores del diccionarii principal (key->XR)
            routers = []
            ipadd = []
            for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                routers.append(router)
                ipadd.append(ip)
            d_type = ipadd[0] #Se obtiene valor de data_type en la lista
            ipadd.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
            return key,d_type,ipadd #regresa los valores XR, data_type y lista de equipos.
