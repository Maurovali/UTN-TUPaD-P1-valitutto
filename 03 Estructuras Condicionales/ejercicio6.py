
from statistics import mode, median, mean
import random
numeros_aleatorios= [random.randint (1,100) for i in range (50)]
moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana and ( mediana < moda):
    print ("sesgo positivo")
elif  media < mediana and ( mediana < moda):
    print ("sesgo negativo")
else:
    print ("sin sesgo")
