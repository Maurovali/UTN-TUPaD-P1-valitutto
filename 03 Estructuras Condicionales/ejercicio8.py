nombre= str (input ("ingrese su nombre "))
opcion_escritura= str (input ("1. Si quiere su nombre en mayúsculas. 2. Si quiere su nombre en minúsculas o3. Si quiere su nombre con la primera letra mayúscula "))
if opcion_escritura == ("1"): 
    print (nombre.upper())
elif opcion_escritura == ("2"):
    print (nombre.lower())
else:
    print (nombre.title())