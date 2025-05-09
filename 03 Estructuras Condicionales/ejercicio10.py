hemisferio= str(input("indique en cual hemisferio se encuentra (S/N) "))
hemisferio=hemisferio.lower()
mes= str(input("indique mes "))
mes=mes.lower()
dia= int (input ("indique dia "))

if hemisferio == "n" and (mes in ("enero", "febrero") or (mes=="diciembre" and dia >= 21) 
                        or (mes== "marzo" and dia<21)):
    print("usted esta en invierno")
elif hemisferio == "n" and (mes in ("abril", "mayo") or (mes=="marzo" and dia >= 21) 
                        or (mes== "junio" and dia<21)):
    print("usted esta en primavera")
elif hemisferio == "n" and (mes in ("julio", "agosto") or (mes=="junio" and dia >= 21) 
                        or (mes== "septiembre" and dia<21)):
    print("usted esta en verano")
elif hemisferio == "n" and (mes in ("octubre", "noviembre") or (mes=="septiembre" and dia >= 21) 
                        or (mes== "diciembre" and dia<21)):
    print("usted esta en otoño")
else:
    if hemisferio == "s" and (mes in ("enero", "febrero") or (mes=="diciembre" and dia >= 21) 
                        or (mes== "marzo" and dia<21)):
        print("usted esta en verano")
    elif hemisferio == "s" and (mes in ("abril", "mayo") or (mes=="marzo" and dia >= 21) 
                        or (mes== "junio" and dia<21)):
        print("usted esta en otoño")
    elif hemisferio == "s" and (mes in ("julio", "agosto") or (mes=="junio" and dia >= 21) 
                        or (mes== "septiembre" and dia<21)):
         print("usted esta en invierno")
    elif hemisferio == "s" and (mes in ("octubre", "noviembre") or (mes=="septiembre" and dia >= 21) 
                        or (mes== "diciembre" and dia<21)):
          print("usted esta en primavera")
    
