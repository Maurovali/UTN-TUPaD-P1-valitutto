numero1= int(input("ingrese un numero entero"))
numero2= int(input("ingrese segundo numero entero"))
sumatoria=0
if numero1 < numero2:
    
    for contador in range (numero1,numero2+1):
        sumatoria=sumatoria+contador
       
    print("la suma es ",sumatoria)
else:
    for contador in range (numero2,numero1+1):
        sumatoria=sumatoria+contador
    print("la suma es ",sumatoria)

    