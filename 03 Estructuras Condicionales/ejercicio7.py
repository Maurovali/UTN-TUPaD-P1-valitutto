palabra_frase= str (input("ingrese una frase o variable "))
letra= palabra_frase [-1]
terminacion= ["a", "e" ,"i" ,"o","u"]
if letra in terminacion:
    print (palabra_frase, "¡")
else:
    print (palabra_frase)
