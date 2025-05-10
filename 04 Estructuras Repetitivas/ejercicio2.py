numero= int(input("ingrese un numero entero"))
cont=0
if numero == 0:
    cont = 1
else:
    while numero > 0:
          numero= (numero//10)
          cont=cont+1
print ("el numero ingresado tiene",cont, "digitos")
