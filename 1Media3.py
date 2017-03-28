#Programa que permita obtener la media de 3 numeros

def calcular_media(A, B, C):
    resultado = (  A + B + C)/ float(3)
    return resultado
    
print 'INGRESAR TRES NUMEROS'

A=int(input("Ingrese primer numero: "))
B=int(input("Ingrese segundo numero: "))
C=int(input("Ingrese tercer numero: "))

media= calcular_media(A, B, C)
print '\n'
print 'Media aritmetica es: ', media 

    




