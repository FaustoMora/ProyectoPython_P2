from lib2to3.fixer_util import String

print "Hello world"

        
class Devices:
    def __init__(self, device):
        self.devices=[];

class Device:
    def __init__(self, i, ua, fb, grupo):
        self.id=i;
        self.user_agent=ua;
        self.fall_back=fb;
        self.group=grupo;
        
class Group:
    def __init__(self, i, cap):
        self.id=i;
        self.capability=cap;
        
class Capability:
    def __init__(self, nombre, valor):
        self.name=nombre;
        self.value=valor;


archivo_xml = open( 'C:\\Users\\PC\\Documents\\Aptana Studio 3 Workspace\\Test\\xmlPequeno.xml', 'r' );  
lineas = archivo_xml.read()
#print lineas


dev=[]
wr=""
for letr in lineas:
    if letr =='<' or letr !='>':
        if letr !='<' and letr !='>':
            wr=wr+letr
            if wr=="devices":
                #dev=[]
                ds=Devices(dev)
                wr=""
                if wr=="device ":
                    wr=""
                    idd=""
                    ua=""
                    fb=""
                    grup=[]
                    if wr=="id=" :
                        wr=""
                        if letr =='"' or letr !=' ':
                            if letr !='"' and letr !=' ':
                                wr=wr+letr
                                idd=wr
                                print idd
                    if wr=="user_agent=" :
                        wr=""
                        if letr!="\"":
                            wr=wr+letr
                            ua=wr
                            print ua
                        if letr==" ":
                            wr=""
                            break
                    if wr=="fall_back=" :
                        wr=""
                        if letr!="\"":
                            wr=wr+letr
                            fb=wr
                        if letr==" ":
                            wr=""
                            break
                    devic=Device(idd, ua, fb, grup)
                    print devic
                    ds.dev.append(devic)
                    if wr=="group":
                        wr=""
                        cap=[]
                        if wr=="id=":
                            wr=""
                            if letr =='"' or letr !=' ':
                                if letr !='"' and letr !=' ':
                                    wr=wr+letr
                                    idg=wr
                                    wr=""
                    
                                    g=Group(idg,cap)
                                    print g                                
                                    devic.group.append(g)
                    if wr=="capability":
                        wr=""
                        
                        if wr=="name=":
                            wr=""
                            if letr =='"' or letr !=' ':
                                if letr !='"' and letr !=' ':
                                    wr=wr+letr
                                    nombre=wr
                                    wr=""
                        if wr=="value=":
                            wr=""
                            if letr =='"' or letr !=' ':
                                if letr !='"' and letr !=' ':
                                    wr=wr+letr
                                    valor=wr
                                    wr=""
                                    c=Capability(nombre, valor)
                                    print c
                        g.capability.append(c)
print dev