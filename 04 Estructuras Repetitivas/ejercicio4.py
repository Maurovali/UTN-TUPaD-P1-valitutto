CORTE= "0"
sumatoria=0
numero=float("inf")

while numero !=0 :
  numero= int(input("ingrese un numero, con " + CORTE + " termina el calculo"))
  sumatoria=sumatoria+numero

print ("la sumatoria es ", sumatoria)