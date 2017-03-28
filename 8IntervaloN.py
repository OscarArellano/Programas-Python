#Realiza un programa que permita generar
#un intervalo de n numeros entre 20 y 60

            
def inter_numeros():
    n = int(input('Ingresar numero: '))
    h = ''
    while h >= 20 and n <= 60:
        h += ' %i' % n
        n += 1
        print h
        if n <= 20:
            print 'No esta en el intervalo'
            return
       
print "Introducir numero que sea mayor o igual a 20"   

inter_numeros()


