#Programa que por medio de la recursion 
#calcula la suma de los cuadrados de n numeros.
 
print "CALCULAR LA SUMA DE CUADRADOS MEDIANTE LA RECURSION"
def recursion_cuadrado(x,n):

	if(n>0):
		# Se va llamando a ella misma mientras el valor sea superior a 0
		x=recursion_cuadrado(x,n-1)
		x=x*(n**2)
	else:
		x=1
	return x
 
try:
	numero = int(raw_input("inserta un numero: "))
	# Ejecutamos la función recusiva para el calculo
	calculo=recursion_cuadrado(1,numero)
	print "La suma de los cuadrados de %s es: %s" % (numero,calculo)
except:
	print "\nTiene que ser un valor numerico" 
    

 
