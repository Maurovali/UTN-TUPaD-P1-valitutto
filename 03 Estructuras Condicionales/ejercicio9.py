magnitud_terremoto=float (input ("indique magnitud terremoto segun escala Richter "))

if magnitud_terremoto < 3: 
    print ("Muy Leve" "(imperceptible)")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print ("leve" "(ligeramente perceptible)")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print ("moderado" "(sentido por personas pero generalmente no causa daños)")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print ("fuerte" "(puede causar daños en estructuras debiles)")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print ("muy fuerte" "(puede causar daños significativos)")
else:
    print ("extremo" "(puede causar graves daños)")
