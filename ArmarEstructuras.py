from Clases import *
from Funciones import *
import sys
import re

def CrearEstructuras():
    sys.setrecursionlimit(15100)
    i=0
    contdev=0
    contgroup=0
    listaDevices=[]
    archivo_xml = open('wurfl-2.3.xml','r');
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
            dev=Device(linea[0].split('=')[1].replace('\"',""),linea[1].split('=')[1].replace('\"',""),linea[2].split('=')[1].replace('\"',"").replace("\n",""))
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
            linea=linea.replace('/>',"")
            linea=linea.split()
            #print(linea[0].split('=')[1].replace('\"',""),linea[1].split('=')[1].replace('\"',""))
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
    #print(listaDevices[0].id)
    #for device1 in listaDevices:
    #    for group1 in device1.groups_list:
    #            print(group1.id)
    #print
    #print(len(listaDevices))
    
#    result = buscarDevice_CapabilityAtributo(listaDevices, "cookie_support","false")
 #   len(result)
  #  for res in result:        
   #     print(res.id)
    #print(len(result))
    lista=[]
    for dev in listaDevices:
        #newdev=Device(dev.id,dev.user_agent,dev.fall_back,dev.groups_list)
        result=fall_back_Device_Linked(listaDevices,dev,dev,Capability("cookie_support","false"))
        if result!=None:
            i+=1
            print(i)
            print(result.id)
            lista.append(result)
    print(len(lista))
    

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

