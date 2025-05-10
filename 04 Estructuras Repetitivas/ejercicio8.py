numerospares=0
numerospositivos=0
for i in range (0,10):
    numero= int(input("ingrese un numero entero "))
    if numero %2 ==0:
        numerospares=numerospares+1
    if numero > 0:
        numerospositivos=numerospositivos+1
print (" hay ", numerospares, "numeros pares en sus ingresos y ", (10-numerospares), "numeros impares")
print (" hay ", numerospositivos, "numeros positivos en sus ingresos y ", (10-numerospositivos), "numeros negativos")