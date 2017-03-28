#Programa que permite rotar una lista

def rotar_lista(lista):
    lista=lista[::-1]
    print 'Rotacion 1: ',lista
    
       

lista = raw_input('Ingrese el dato a invertir: \n')
if lista > 2:
    print "La lista es: ",lista
else:
    print "Ingresar minimo 2 numeros"
    
       
rotar_lista(lista)


      
    

        
        

