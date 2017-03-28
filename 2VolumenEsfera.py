#programa que calcule el area de una esfera

import math

def vol_esfera():
    proceso_volumen = (math.pi * radio_esfera**3)/3
    return proceso_volumen


print 'CALCULAR EL VOLUMEN DE UNA ESFERA'

radio_esfera=float(input("Ingrese el radio de la esfera: "))


volumen=vol_esfera()

print '\n'
print "El volumen de la esfera es: ",volumen
