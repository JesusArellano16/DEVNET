import json
import connection
import sign

def get_ips(user, pswd, loc):
    with open (f'src/sitios/{loc}.json', "r") as file:
        data = json.load(file)
        for key, value in data.items(): #Se itera para extraer los valores del diccionarii principal (key->XR)
            keys = []
            keys.append(key)
           
            if(key == "XR"):
                beg_router = 15
                router_xr = []
                ipadd_xr = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_xr.append(router)
                    ipadd_xr.append(ip)
                d_type_xr = ipadd_xr[0] #Se obtiene valor de data_type en la lista
                ipadd_xr.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                print("Respaldo RMACs: ", ipadd_xr)
                connection.router_info(user, pswd, ipadd_xr, d_type_xr, key, beg_router)
                sign.signature()

            elif(key == "APIC"):
                userapc = "apic#TACACS_DOMAIN\\"+"\\"+user
                router_apc = []
                ipadd_apc = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_apc.append(router)
                    ipadd_apc.append(ip)
                d_type_apc = ipadd_apc[0] #Se obtiene valor de data_type en la lista
                ipadd_apc.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                print("Respaldo APICs: ", ipadd_apc)
                connection.router_info(userapc, pswd, ipadd_apc, d_type_apc, key)
                sign.signature()

            elif(key == "SPINE"):
                usersp = "apic#TACACS_DOMAIN\\"+"\\"+user
                router_sp = []
                ipadd_sp = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_sp.append(router)
                    ipadd_sp.append(ip)
                d_type_sp = ipadd_sp[0] #Se obtiene valor de data_type en la lista
                ipadd_sp.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                print("Respaldo SPINE: ",ipadd_sp)
                connection.router_info(usersp, pswd, ipadd_sp, d_type_sp, key)
                sign.signature()

            elif(key == "LEAF"):
                userlf = "apic#TACACS_DOMAIN\\"+"\\"+user
                router_lf = []
                ipadd_lf = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_lf.append(router)
                    ipadd_lf.append(ip)
                d_type_lf = ipadd_lf[0] #Se obtiene valor de data_type en la lista
                ipadd_lf.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                print("Respaldo LEAF: ", ipadd_lf)
                connection.router_info(userlf, pswd, ipadd_lf, d_type_lf, key)
                sign.signature()

            elif(key == "IOS"):
                router_ios = []
                ipadd_ios = []
                for router, ip in value.items(): # Se itera para convertir en lista los valores (values->'R1':'10.1.1.1'}) del diccionario pricipal
                    router_ios.append(router)
                    ipadd_ios.append(ip)
                d_type_ios = ipadd_ios[0] #Se obtiene valor de data_type en la lista
                ipadd_ios.pop(0) #Se elimina el valor de data_type y quedan solo las IPs de los equipos
                print("Respaldo Router: ", ipadd_ios)
                connection.router_info(user, pswd, ipadd_ios, d_type_ios, key)
                sign.signature()