    #!/usr/bin/env python   
    # -*- coding: latin-1 -*-  

print("1. Cargando el archivo xml")
print  
      
    # abro el archivo en modo de solo lectura y lo  
    # referencio por medio de la variable archivo_xml  
archivo_xml = open( 'C:\\Users\\Usuario\\Desktop\\ProyectoPython\\xmlPequeno.xml', 'r' );  
lineas = archivo_xml.readlines();  
      
    # De este modo se puede leer cada línea, y se pone una coma(,)  
    # después del print line, para que obvie el salto de línea  
    # que pone el print al final, prueba quitando la coma  
numero = 0;  
print(u"2. Imprimiendo el archivo en orden")  
print ("===============================" )
for linea in lineas:  
    numero += 1  
    print (numero,". ",linea,)  
print  
print  
      
