class Device:
    def __init__(self,tipo=None,id_Dv=None,user_agent=None,fall_back=None):
        self.tipo=tipo
        self.id_Dv=id_Dv
        self.user_agent=user_agent
        self.fall_back=fall_back

    def tipo(self):
        return self.tipo

    def id_device(self):
        return self.id_Dv
    
    def user_device(self):
        return self.user_agent
    
    def fall_back_device(self):
        return self.fall_back
    
    def print_device(self):
        print(self.tipo + " " + self.id_Dv + " " + self.user_agent + " " + self.fall_back)
        

class Group:
    def __init__(self,tipo=None,id_Gr=None,id_Dev=None):
        self.tipo=tipo
        self.id_Gr=id_Gr
        self.id_Dev=id_Dev
        
    def tipo(self):
        return self.tipo
    
    def id_group(self):
        return self.id_Gr
    
    def id_device(self):
        return self.id_Dev
    
    def print_group(self):
        print(self.tipo + " " + self.id_Gr + " " + self.id_Dev)
        
class Capability:
    def __init__(self,tipo=None,id_Cap=None,value=None,id_Grp=None):
        self.tipo=tipo
        self.id_Cap=id_Cap
        self.value=value
        self.id_Grp=id_Grp
        
    def tipo(self):
        return self.tipo
    
    def id_capability(self):
        return self.id_Cap
    
    def value(self):
        return self.value
    
    def id_grupo(self):
        return self.id_Grp
    
    def print_capability(self):
        print(self.tipo + " " + self.id_Cap + " " + self.value + " " + self.id_Grp)
        
