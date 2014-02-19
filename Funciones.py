import Clases

def fall_back_Device_Linked(listdev=None,devsrc=None,devfb=None,capability=None):
	if devfb!= None:
		dev=device_has_capability(devfb,capability.name,capability.value)
		if dev != None:
			#print("Succeful")
			return devsrc
		else:
			if devfb.fall_back == "root":
				#print(devfb.fall_back)
				return None
			else:
				#print(devfb.fall_back)
				for devfb1 in listdev:
					if devfb1.id == devfb.fall_back:
						#print(devfb.fall_back+devfb1.id)
						#newdev = Device(devfb1.id,devfb1.user_agent,devfb1.fall_back,devfb1.groups_list)
						return fall_back_Device_Linked(listdev,devsrc,devfb1,capability)

			
def device_has_capability(dev=None,nombre=None,value=None):
	#print(dev.id)
	if nombre!= None and value!=None:
		for gr in dev.groups_list:
			for cap in gr.capabilities_list:
				#print(cap.value)
				if cap.name == nombre and cap.value == value:
					#print("%s %s"%(cap.name,cap.value))
					return True
	return None
#def contar_lista():
#def buscarDevice_Atrinuto():
    
#def buscarDevice_Group():
#def buscarDevice_Capability():
#def buscarDevice_Group_Capability():
    
#def buscarGroup_Atributo():
#def buscarGroup_Capability():

def buscarDevice_CapabilityAtributo(lista, nombre=None,Value=None):
	#print("%s %s"%(nombre,Value))
	result_set=[]
	if nombre!= None and Value!=None:
		#print("YES")
		for each_item in lista:
			for gr in each_item.groups_list:
				for cap in gr.capabilities_list:
					#print(cap.value)
					if cap.name == nombre and cap.value == Value:
						#print("%s %s"%(cap.name,cap.value))
						result_set.append(each_item)           
	elif nombre!=None or Value!=None:
		for each_item in lista:
			if nombre == None:
				for gr in each_item.groups_list:
					for cap in gr.capabilities_list:
						if cap.value == Value:
							result_set.append(each_item)
			elif Value == None:
				for gr in each_item.groups_list:
					for cap in gr.capabilities_list:
						if cap.name == nombre:
							result_set.append(each_item)
	return result_set
	