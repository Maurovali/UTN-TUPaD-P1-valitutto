import random
numeroganador=random.randint(1, 10)
numero=float("inf")
contador=0
while numero!=numeroganador:
    numero=int (input("ingrese un numero del 1 al 10 "))
    contador=contador+1
print ("usted ha acertado en ", contador, " intentos ")