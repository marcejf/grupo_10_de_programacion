"""
un programa con las operaciones basicas y complejas de aritmetica
"""

#Definir las variables
num1 = float(input("ingrese un numero"))
num2 = float(input("ingrese el siguiente numero:"))

#sumar
suma = num1 + num2 
print(suma)

#resta
resta = num1 -num2

#multiplicasion 
multiplicasion = num1 * num2

#division
if num2 != 0:
   division = num1 / num2 
else: 
    print("no se puede dividir entre cero")

#potencia
potencia = num1 ** num2 
8#radicacion 
 
#radicacion 
radicacion = num1 ** (1/num2) 

#print("el resultado de la suma es /`" ,suma ""
print(f"el resultado de la suma es '´{suma}'")
print(f"el resultado de la resta es :'{resta}'")
print(f"el resultado de la multiplicasion es : '{multiplicasion}'")
print(f"el resultado de la division es :'{division}'")
print(f"el resultado de la potencia es : '{potencia}'")
print(f"el rsultado de la radicasion es : '{radicacion}'")
