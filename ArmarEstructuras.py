from Clases import *
from Funciones import *
import re
from fileinput import close
import Funciones

def CrearEstructuras():
    contdev=0
    contgroup=0
    listaDevices=[]
    archivo_xml = open('C:\\Users\\Lost Legion\\Desktop\\ESPOL\\Lenguajes de Programacion\\ProyectoPython\\wurfl-2.3.xml','r');
    lineas = archivo_xml.readlines();    
    for linea in lineas:
        respuesta=ProcesarLinea(linea)
    
        if 'CrearListaDevices' in respuesta:
            print("Devices Encontrados")
        
        elif 'CrearDevice' in respuesta:
            linea=linea.replace('<device',"")
            linea=linea.replace('>',"")
            linea=linea.split('\" ')
        #print(linea)
            if len(linea) < 4:
                dev=Device(linea[0].split('=')[1].replace('\"',""),linea[1].split('=')[1].replace('\"',""),linea[2].split('=')[1].replace('\"',""))
                listaDevices.append(dev)
            else:
                dev=Device(linea[0].split('=')[1].replace('\"',""),linea[1].split('=')[1].replace('\"',""),linea[2].split('=')[1].replace('\"',""),linea[3].split('=')[1].replace('\"',""))
                listaDevices.append(dev)
            contgroup=0
        
        elif 'CrearListaGrupos' in respuesta:
            linea=linea.replace('<group',"")
            linea=linea.replace('>',"")
            linea=linea.split()
            group=Group(linea[0].split('=')[1].replace('\"',""))
            listaDevices[contdev].groups_list.append(group)
        
        elif 'CrearCapability' in respuesta:
            linea=linea.replace('<capability',"")
            linea=linea.replace('>',"")
            linea=linea.split()
            capability=Capability(linea[0].split('=')[1].replace('\"',""),linea[1].split('=')[1].replace('\"',""))
            listaDevices[contdev].groups_list[contgroup].capabilities_list.append(capability)
        
        elif 'CerrarListaGrupos' in respuesta:
            contgroup += 1
        
        elif 'CerrarDevice' in respuesta:
            contdev += 1
        
        elif 'CerrarListaDevices' in respuesta:
            print("No hay mas dispositivos")
        
        #elif 'SaltarLinea' in respuesta:
        # print(linea)
        
        archivo_xml.close()

    for device1 in listaDevices:
        for group1 in device1.groups_list:
                print(group1.id)
    print
    print(len(listaDevices))
       
    
    result_gr = buscarDevice_Group(listaDevices, 'product_info')
        
    for res_gr in result_gr:        
        print (res_gr .id)
    print(len(result_gr))
    
    print(listaDevices[0].actual_device_root)
    
    result = buscarDevice_CapabilityAtributo(listaDevices, "mobile_browser")
    
    #for res in result:        
        #print (res.id)
    print(len(result))
    print(Funciones.buscarDevice_Lista(listaDevices, 'generic'))
        
    #1574
    result_not = buscarDevice_NoCapabilityAtributo(listaDevices, "fausto_mora")

    #for res2 in result_not:        
        #print (res2.id)
    print(len(result_not))
    
    print(len(listaDevices)) 
    


def ProcesarLinea(linea=""):
    if '<devices>' in linea:
        return 'CrearListaDevices'
    elif '<device ' in linea:
    #print('\tDevice')
        return 'CrearDevice'
    elif '<group ' in linea:
    #print('\t\tGrupo')
        return 'CrearListaGrupos'
    elif '<capability ' in linea:
    #print('\t\t\tCapa')
        return 'CrearCapability'
    elif '</group>' in linea:
    #print('\t\tCerrarGroup')
        return 'CerrarListaGrupos'
    elif '</device>' in linea:
    #print('\tCerrarDev')
        return 'CerrarDevice'
    elif '</devices>' in linea:
    #print('CerrarListaDev')
        return 'CerrarListaDevices'
    else:
        return 'SaltarLinea'

