while True:

palabra = input("ingrese una palabra")
LetraInicial = input("ingrese la letyra inicial")

if palabra[2].lower() == LetraInicial.lower():
   print(f"la palabra {palabra} comienza con la letra {LetraInicial} ingresada") 
else:
    print(f"la palabra {palabra} no comienza con la letra {LetraInicial} ingresada")   