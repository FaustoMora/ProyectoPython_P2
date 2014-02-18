import Clases


def buscarDevice_CapabilityAtributo(lista, nombre=None,Value=None):   
    result_set=[]

    if nombre!=None or Value!=None:
        for each_item in lista:
            if nombre == None:
                for gr in each_item.groups_list:
                    for cap in gr.capabilities_list:
                        if cap.value == Value:
                            result_set.append(each_item)
            if Value == None:
                for gr in each_item.groups_list:
                    for cap in gr.capabilities_list:
                        if cap.name == nombre:
                            result_set.append(each_item)
            else:
                for gr in each_item.groups_list:
                    for cap in gr.capabilities_list:
                        if cap.name == nombre and cap.value == Value:
                            result_set.append(each_item)           
        return result_set
    else:
        return None            

def buscarDevice_Group(lista, nombre_id=None):
    result_set=[]
    if nombre_id != None:
        for each_item in lista:
            for each_group in each_item.groups_list:
                if each_group.id == nombre_id:
                    result_set.append(each_item)
        return result_set
    else:
        return None

def buscarDevice_NoCapabilityAtributo(lista, nombre=None,Value=None):   
    result_set=[]

    if nombre!=None or Value!=None:
        for each_item in lista:
            if nombre == None:
                for gr in each_item.groups_list:
                    for cap in gr.capabilities_list:
                        if cap.value != Value and not buscarDevice_Lista(result_set, each_item.id):
                            result_set.append(each_item)
            if Value == None:
                for gr in each_item.groups_list:
                    for cap in gr.capabilities_list:
                        if cap.name != nombre and not buscarDevice_Lista(result_set, each_item.id):
                            result_set.append(each_item)
            else:
                for gr in each_item.groups_list:
                    for cap in gr.capabilities_list:
                        if cap.name != nombre and cap.value != Value and not buscarDevice_Lista(result_set, each_item.id):
                            result_set.append(each_item)           
        return result_set
    else:
        return None    
    
def buscarDevice_Lista(lista, ID):
    if lista == [] :
        return False
    else:    
        for each_dev in lista:
            if each_dev.id == ID:
                return True
            
