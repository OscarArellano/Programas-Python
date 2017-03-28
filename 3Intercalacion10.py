#Programa que obtiene la intercalacion de
#10 numeros impares empezando desde el 13

def inter_impares():
    n = 13
    h = ''
    while n <= 31:
        if n%2 != 0:
            h += ' %i' % n
            n += 1
            return


print 'INTERCALACIÓN DE NÚMEROS IMPARES'
print '\n'

inter_impares()
print h





   
    





