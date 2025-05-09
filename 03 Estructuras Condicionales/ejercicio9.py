magnitud_terremoto=float (input ("indique magnitud terremoto segun escala Richter "))

if magnitud_terremoto < 3: 
    print ("Muy Leve")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4:
    print ("leve")
elif magnitud_terremoto >= 4 and magnitud_terremoto < 5:
    print ("moderado")
elif magnitud_terremoto >= 5 and magnitud_terremoto < 6:
    print ("fuerte")
elif magnitud_terremoto >= 6 and magnitud_terremoto < 7:
    print ("muy fuerte")
else:
    print ("extremo " "(puede causar graves daños)")
