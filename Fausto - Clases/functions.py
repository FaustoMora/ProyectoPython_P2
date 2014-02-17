import classes

#variables que necesitamos
#el programa no esta validado para los fallbacks
#no estan validados los cierres de etiquetas

list_device=[]
list_group=[]
list_capability=[]
device_id='';
group_id='';
capability_id='';

try:
    with open('texto.txt') as aux:
    
        for each_linea in aux:
            #elimino los mas y menos y el interlineado
            linea = (each_linea.strip('<').strip('>\n'))
            #pregunto por los device... como siempre hay un device primero este siempre se cumple       
            if 'device' in linea:
                print(True)
                data_dev=linea.split(' ')
                list_device.append(classes.Device(data_dev[0],data_dev[1],data_dev[2],data_dev[3]))
                device_id=data_dev[1]
                print(data_dev)
                print(device_id)
            
            #pregunto por los group y guardo el device_id
            elif 'group' in linea:
                print(True)
                data_gr=linea.split(' ')
                list_group.append(classes.Group(data_gr[0],data_gr[1],device_id))
                group_id=data_gr[1]
                print(data_gr)
                print(group_id)
                
            #pregunto por los capability y guardo el group_id    
            elif 'capability' in linea:
                print(True)
                data_cap=linea.split(' ')
                list_capability.append(classes.Capability(data_cap[0],data_cap[1],data_cap[2].strip('/'),group_id))
                print(data_cap)
                
#por si no se encuentra el archivo manejo el error
except:
    print('Error de archivo')
            
            

#funcion para imprimir la lista
def imprimirLista(lista):
    for each_item in lista:
        if isinstance(each_item,classes.Device):
            classes.Device.print_device(each_item)
        if isinstance(each_item,classes.Group):
            classes.Group.print_group(each_item)
        if isinstance(each_item,classes.Capability):
            classes.Capability.print_capability(each_item)

#imprimimos todas nuestras tres listas     
imprimirLista(list_device)
imprimirLista(list_group)
imprimirLista(list_capability) 
  

    
    
    