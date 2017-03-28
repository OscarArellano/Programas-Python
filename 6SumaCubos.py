#programa que permita generar un intervalo de la suma
#de los cubos de los primeros n números


def sumaCubos(num):
    return num **3
    s = 0
    while num > 0:
        s = s + num % 10
        num = num // 10
        return s
    
n = int(input("Cantidad de numeros: "))#cantidad de numeros
sumaT = 0 #suma total
while n > 0:
    num = int(input("Numero: "))
    sumaT = sumaT + sumaCubos(num)
    n = n - 1

    print "Reultado del numero al cubo: ",num**3
    print "Suma de los Numeros al cubo: ",sumaT




