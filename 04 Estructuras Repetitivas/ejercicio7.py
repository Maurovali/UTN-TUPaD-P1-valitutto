numero1=0
numero2=int(input("ingrese un numero entero "))
sumatoria=0
if numero2 > numero1:
    
    for contador in range (numero1,numero2+1):
        sumatoria=sumatoria+contador
       
    print("la suma es ",sumatoria)
else:
    
    print("ud. no ha ingresado un numero entero ")

    