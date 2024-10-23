import json
import connection

def get_ips(user, pswd, loc):
    with open (f'src/sitios/{loc}.json', "r") as file:
        data = json.load(file)
        for key, value in data.items(): #Se itera para extraer los valores del diccionarii principal (key->XR)
            keys = []
            keys.append(key)
           
            if(key == "XR"):
                router_xr = []
                ipadd_xr = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_xr.append(router)
                    ipadd_xr.append(ip)
                d_type_xr = ipadd_xr[0] #Se obtiene valor de data_type en la lista
                ipadd_xr.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                connection.router_info(user, pswd, ipadd_xr, d_type_xr, key)

            elif(key == "APIC"):
                router_apc = []
                ipadd_apc = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_apc.append(router)
                    ipadd_apc.append(ip)
                d_type_apc = ipadd_apc[0] #Se obtiene valor de data_type en la lista
                ipadd_apc.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                connection.router_info(user, pswd, ipadd_apc, d_type_apc, key)

            elif(key == "SPINE"):
                router_sp = []
                ipadd_sp = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_sp.append(router)
                    ipadd_sp.append(ip)
                d_type_sp = ipadd_sp[0] #Se obtiene valor de data_type en la lista
                ipadd_sp.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                connection.router_info(user, pswd, ipadd_sp, d_type_sp, key)

            elif(key == "LEAF"):
                router_lf = []
                ipadd_lf = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_lf.append(router)
                    ipadd_lf.append(ip)
                d_type_lf = ipadd_lf[0] #Se obtiene valor de data_type en la lista
                ipadd_lf.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                connection.router_info(user, pswd, ipadd_lf, d_type_lf, key)

            elif(key == "IOS"):
                router_ios = []
                ipadd_ios = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_ios.append(router)
                    ipadd_ios.append(ip)
                d_type_ios = ipadd_ios[0] #Se obtiene valor de data_type en la lista
                ipadd_ios.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                connection.router_info(user, pswd, ipadd_ios, d_type_ios, key)
