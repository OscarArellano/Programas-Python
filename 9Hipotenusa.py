#Programa que solicita dos argumentos de tipo Double para calcular 
#la hipotenusa de un triángulo rectángulo y 
#retorne un valor de tipo Double.

import math

def hipo_triangulo():
    CatOpu = float(input("Ingresa Cateto Opuesto: "))
    CatAdy = float(input("Ingresa Cateto Adyacente: "))
    hipo = math.sqrt((CatOpu**2 + CatAdy**2))
    return hipo


print 'HIPOTENUSA DE UN TRIANGULO'

hipotenusa=hipo_triangulo()

print '\n'
print 'La hipotenusa es: ', hipotenusa
