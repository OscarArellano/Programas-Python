#Realiza una funci�n que permita obtener el m�ximo de 3 n�meros.

def maximo_num(A, B, C):
    if(A > B and A > C):
        print '\n'
        print("El numero mayor es " + str(A))
    else:
        if(B > A and B > C):
            print '\n'
            print("El numero mayor es " + str(B))
        else:
            print '\n'
            print("El numero mayor es " + str(C))
            return
    

print 'INGRESAR TRES NUMEROS Y OBTENER EL MAXIMO'

A=int(input("Ingrese primer numero: "))
B=int(input("Ingrese segundo numero: "))
C=int(input("Ingrese tercer numero: "))


maximo_num(A, B, C)





