edad= int(input ("ingrese su edad "))
if  edad < 12:
    print ("pertenece a la categoria niño")
elif edad >= 12 and edad < 18:
    print ("pertenece a la categoria adolescente")
elif edad >= 18 and edad < 30:
    print ("pertenece a la categoria adulto joven")
else:  
    print ("pertenece a la categoria adulto")
